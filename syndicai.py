import torch
from PIL import Image 
from helpers import draw_box, url_to_img, img_to_bytes


class PythonPredictor:
    def __init__(self, config):
        """ Download pretrained model. """
        pass

    def predict(self, payload):
        """ Run a model based on url input. """

        # Inference
        response = model(payload["url"])
        return response
