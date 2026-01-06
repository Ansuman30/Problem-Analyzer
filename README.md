
# AUTO JUDGE

This is the tool which would help any competitive programmer or DSA solver to analyze the difficulty of problem before solving . They have to put in description about the question and they would get whether question is HARD,MEDIUM or EASY and what is its difficulty score out of 10.




## DATASET USED

Dataset used is https://github.com/AREEG94FAHAD/TaskComplexityEval-24 .
## APPROACH AND MODEL USED

Basic approach was to club all the textual information into one column then began doing feature engineering to find out some important features like length of problem, mathematical symbols used,no of words used in the problem.

TF-IDF was done on textual information to make embeddings which would be understandable by the ML model. Separate Model one for classiification and another for regression was done. Models like RandomForest Classifier and Regressor and XGBoost Classifier and Regressor were used and the best model was chosen based on hyperparameter tuning.


## EVALUATION METRICS 

Best R2 for RandomForest: 0.1321
Best R2 for XGBoost: 0.1179
Saved Best Regressor: RandomForestRegressor


Best Accuracy for RandomForest: 0.5081
Best Accuracy for XGBoost: 0.5056
Saved Best Classifier: RandomForestClassifier
## Run Locally

Clone the project

```bash
  git clone https://github.com/Ansuman30/Problem-Analyzer
```

Create a virtual env

```bash
  python -m venv venv
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run website.py
```

Additionally the website has been hosted for easy use on this url :https://problem-analyzer-b6m2q3v2sepo4ewmnywoue.streamlit.app/


## WEB INTERFACE

Web Interface is created using streamlit one needs to submit Problem Description,Input Description,Output Description, Sample Input/Output.


## Demo

Link of the demo video-https://youtu.be/BpZirPuegkE



Ansuman Sahu
Production and Industrial Engineering 
