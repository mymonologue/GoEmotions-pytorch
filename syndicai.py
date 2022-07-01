import torch
import run_goemotions


class PythonPredictor:
    def __init__(self, config):
        """ Download pretrained model. """
        pass

    def predict(self, payload):
        """ Run a model based on url input. """

        # Inference
        response = run_goemotions(payload["text"])
        return response
