from flask import Flask, request, jsonify, send_file, render_template
import re

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
import pickle

STOPWORDS = set(stopwords.words("english"))

app= Flask(__name__)


## Test Route
@app.route("/test",methods=["GET"])
def test():
    return "Test request received successfully. Service is running."


@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")



@app.route("/predict",methods=["GET"])
def predict():
    return render_template("predict.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
