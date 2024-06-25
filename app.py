# app.py
from datasets import load_dataset

def load_pubmed_dataset():
    try:
        # Load the PubMed Summarization dataset with custom code execution
        dataset = load_dataset("scientific_papers", "pubmed", trust_remote_code=True)
        print(f"Dataset loaded with {len(dataset['train'])} training samples.")
        return dataset
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
