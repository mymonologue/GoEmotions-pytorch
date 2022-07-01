import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline



class PythonPredictor:
    def __init__(self, config):
        """ Download pretrained model. """
        model = AutoModelForSequenceClassification.from_pretrained("monologg/bert-base-cased-goemotions-original")
        tokenizer = AutoTokenizer.from_pretrained("monologg/bert-base-cased-goemotions-original")
        sentiment_classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
        self.sentiment_classifier = sentiment_classifier
        

    def predict(self, payload):
        """ Run a model based on url input. """

        # Inference
        text_to_classify = "I love Beyonce"
        response = self.sentiment_classifier(text_to_classify)
      
        return response
