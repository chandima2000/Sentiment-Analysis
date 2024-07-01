from flask import Flask, request, jsonify, render_template
from utils.utils import single_prediction
from sklearn.ensemble import RandomForestClassifier 

import pickle


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



@app.route("/get-predict",methods=["POST"])
def prediction():
    
    predictor = pickle.load(open(r"models/rfmodel.pkl", "rb"))
    scaler = pickle.load(open(r"models/scaler.pkl", "rb"))
    tfidf = pickle.load(open(r"models/tfidfVectorizer.pkl", "rb"))

    try:
         text_input = request.json["text"]
         predicted_sentiment = single_prediction(predictor, scaler, tfidf, text_input)

         return jsonify({"prediction": predicted_sentiment})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000, debug=True)
