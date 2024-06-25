# summarizer.py
from transformers import pipeline
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

summarizer = pipeline("summarization")

def summarize_text(text):
    logger.info(f"Text length: {len(text)}")
    try:
        if len(text.strip()) > 0:  # Check if text is non-empty and strip any extra whitespace
            summary = summarizer(text, max_length=1000, min_length=30, do_sample=False)
            return summary[0]['summary_text']
        else:
            raise ValueError("Text is empty or contains only whitespace")
    except Exception as e:
        logger.error(f"Error during summarization: {str(e)}")
        raise e
