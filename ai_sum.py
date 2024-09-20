from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')


model_name = 'facebook/bart-large-cnn'  # or 't5-small', 't5-base', etc.
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)


summarizer = pipeline('summarization', model=model, tokenizer=tokenizer, device=0)  # device=0 for the first GPU

text = """
Your text goes here. It can be multiple paragraphs long, and the model will try to generate a shorter summary.
"""
