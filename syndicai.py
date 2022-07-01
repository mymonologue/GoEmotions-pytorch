import torch


class PythonPredictor:
    def __init__(self, config):
        """ Download pretrained model. """
        pass

    def predict(self, payload):
        """ Run a model based on url input. """

        # Inference
        response = self.model(payload["text"])
        return response
