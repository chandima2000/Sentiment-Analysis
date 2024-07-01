# Sentiment-Analysis using Amazon-Alexa-Reviews Dataset

## Introduction
- This is an `End to End NLP Project`
- This project focuses on classifying input text using Natural Language Processing (NLP) techniques. 
- The dataset contains customer reviews, ratings and their corresponding feedback labels. The main goal is to build a machine learning model to predict the Sentiment based on the input text.
- The Model predict the given text input as Positive text or Negative text.
## Project Description

- The project covers `Exploratory Data Analysis(EDA), Data Preprocessing and Model Training.
- The project use NLTK library for Natural Language Processing.

#### Exploratory Data Analysis(EDA): 
- The EDA part is done using Jupyter Notebook.

#### Data Preprocessing
- Remove null values.
- Implemented Upsampling technique because dataset is imbalanced.
- Used PorterStemmer technique.
- Used TF-IDF Vectorizer to create bag of words.
- Used MinMax Scaler.

#### Model Training
- Used Random Forest classifier algorithm.

### Backend
- Flask web Framework
### Frontend
- HTML
- Tailwind CSS
- JavaScript

### Dataset

- Source: - https://www.kaggle.com/datasets/sid321axn/amazon-alexa-reviews

- Description: The dataset contains 3150 instances with 5 parameters.


## Steps to run on Windows

* Prerequisites: [Python 3.12](https://www.python.org/downloads/)
* Open GIT CMD >> navigate to working directory >> Clone this Github Repo

      git clone https://github.com/skillcate/sentiment_analysis_with_sklearn_pipeline.git  
* Open Windows Powershell >> navigate to new working directory (cloned repo folder)
* Create a virtual environment
  * install virtual environment
 
        pip install virtualenv
        
  * create virtual environment by the name ENV
        
        virtualenv ENV
        
  * activate ENV

        .\ENV\Scripts\activate
        
* Install project dependencies

      pip install -r .\requirements.txt
      
* Run the project

      python app.py
      
* Look for the local host address on Powershell screen, something like: 127.0.0.1:5000 >> Type it on your Web Browser >> Website will load

## Contributing
All contributions are welcome. Feel free to open issues or submit pull requests.
