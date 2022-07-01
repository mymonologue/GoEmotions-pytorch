import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline



class PythonPredictor:
    def __init__(self, config):
        """ Download pretrained model. """
        model = AutoModelForSequenceClassification.from_pretrained("monologg/bert-base-cased-goemotions-original")
        tokenizer = AutoTokenizer.from_pretrained("monologg/bert-base-cased-goemotions-original")
        classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
        self.model = model
        self.tokenizer = tokenizer
        self.classifier = classifier
        

    def predict(self, payload):
        """ Run a model based on url input. """

        # Inference
        
        response = self.classifier(payload["text"])
        return response
