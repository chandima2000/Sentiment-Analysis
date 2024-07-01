from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas as pd
import re
from sklearn.ensemble import RandomForestClassifier

STOPWORDS = set(stopwords.words("english"))


def single_prediction(predictor, scaler, tfidf, text_input):

    corpus = []
    stemmer = PorterStemmer()
    review = re.sub("[^a-zA-Z]", " ", text_input)
    review = review.lower().split()
    review = [stemmer.stem(word) for word in review if not word in STOPWORDS]
    review = " ".join(review)
    corpus.append(review)
    X_prediction = tfidf.transform(corpus).toarray()
    X_prediction_scl = scaler.transform(X_prediction)
    y_predictions = predictor.predict_proba(X_prediction_scl)
    y_predictions = y_predictions.argmax(axis=1)[0]

    return "Positive" if y_predictions == 1 else "Negative"


   

