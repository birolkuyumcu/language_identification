# coding: utf-8

import pickle
import logging
from fastapi import FastAPI
from model import Model

title = "FastAPI Teplate"
description="API for template ML model"
ver = "1.0"

app = FastAPI(title= title,description= description , version=ver)

# Initialize logging
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='logs.log')

model = None

@app.on_event("startup")
def load_model():
    global model
    model = Model()

@app.get('/{query}')
def answer_to_query(query : str): 
    try:
        prediction = model.predict(query)
        return {"prediction": prediction}
    except:
        my_logger.error("Something went wrong!")
        return {"prediction": "error"}