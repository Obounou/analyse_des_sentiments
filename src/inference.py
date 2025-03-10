from transformers import AutoTokenizer
import torch
from model import model

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return torch.argmax(outputs.logits, dim=1).item()