from django.apps import AppConfig
import html
import pathlib
import os

# from fire.prediction import FireClassificationPredictor

class MainConfig(AppConfig):
    name = 'main'
    # MODEL_PATH = Path("model")
    # MAIN_PRETRAINED_PATH = Path("model/uncased_L-12_H-768_A-12/")
    # LABEL_PATH = Path("label/")
    # predictor = FireClassificationPredictor(model_path = MODEL_PATH/"multilabel-emotion-fastbert-basic.bin", 
    #                                         pretrained_path = FIRE_PRETRAINED_PATH, 
    #                                         label_path = LABEL_PATH, multi_label=True)  
