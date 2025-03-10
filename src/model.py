from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
import torch

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
