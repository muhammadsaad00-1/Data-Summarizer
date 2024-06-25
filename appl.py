# streamlit_app.py
import streamlit as st
from app import load_pubmed_dataset
from summarizer import summarize_text
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    st.title("PubMed Article Summarizer")

    # Initialize session state variables
    if 'dataset_loaded' not in st.session_state:
        st.session_state.dataset_loaded = False
    if 'dataset' not in st.session_state:
        st.session_state.dataset = None
    if 'summary' not in st.session_state:
        st.session_state.summary = ""

    # Load dataset
    st.header("Load PubMed Dataset")
    if st.button("Load Dataset"):
        try:
            dataset = load_pubmed_dataset()
            st.session_state.dataset = dataset
            st.session_state.dataset_loaded = True
            st.success("Dataset loaded successfully!")
        except Exception as e:
            st.error(f"Failed to load the dataset. Error: {str(e)}")
            st.session_state.dataset_loaded = False
            logger.error(f"Error loading dataset: {str(e)}")

    # Show sample article and summary
    if st.session_state.dataset_loaded and st.session_state.dataset is not None:
        if len(st.session_state.dataset['train']) > 0:
            sample = st.session_state.dataset['train'][0]
            sample_text = sample['article']
            st.subheader("Sample Article")
            st.text_area("Article", sample_text, height=300, key='sample_text')

            if st.button("Summarize Sample Article"):
                try:
                    if len(sample_text.strip()) > 0:  # Check if sample_text is non-empty and strip any extra whitespace
                        summary = summarize_text(sample_text)
                        st.session_state.summary = summary
                    else:
                        st.error("Sample text is empty or contains only whitespace. Cannot summarize.")
                except Exception as e:
                    st.error(f"Failed to summarize the article. Error: {str(e)}")
                    logger.error(f"Error summarizing article: {str(e)}")

            st.subheader("Summary")
            st.text_area("Summary", st.session_state.summary, height=150)
        else:
            st.error("The dataset is empty.")
    else:
        st.warning("Load the dataset to view and summarize an article.")

if __name__ == "__main__":
    main()
