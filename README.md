Mortgage Credit Risk Decision Support System
Overview
This project is an AI-powered mortgage credit risk decision-support system developed in Python.

The system uses a Logistic Regression machine learning model to analyse mortgage applicant data and predict the probability of repayment difficulties. The predicted probability is converted into a risk score which is then interpreted using rule-based decision logic to provide understandable recommendations and explanations.

The system is intended to support mortgage risk assessment and should not be used as a replacement for human decision making.

Features:
Mortgage dataset processing
Missing value handling using mean imputation
Categorical feature encoding
Feature scaling using StandardScaler
Logistic Regression model training
Feature correlation analysis
Feature importance analysis
Feature selection testing
Risk score generation
Rule-based decision support
CSV export of results
Unit testing of decision rules

Project Structure:
project/
│
├── data/
│   ├── A2 Mortgage Credit Risk Dataset.csv
│   └── results.csv
│
├── src/
│   ├── preprocess.py
│   ├── model.py
│   ├── evaluation.py
│   ├── feature_engineering.py
│   ├── decision_rules.py
│
├── Test/
│   └── decision_rules_test.py
│
├── main.py
├── requirements.txt
└── README.md

Installation:

Clone the repository: git clone https://github.com/ShaneannX/proof-of-concept-AI-ML-decision-support-system.git

Navigate to the project directory: cd proof-of-concept-AI-ML-decision-support-system

Install dependencies: pip install -r requirements.txt

Run the application: python main.py

The application will:

1. Load the mortgage dataset.
2. Preprocess the data.
3. Train the Logistic Regression model.
4. Evaluate model performance.
5. Generate risk scores.
6. Apply decision-support rules.
7. Export results to: data/results.csv

Machine Learning Model:
The system uses Logistic Regression to predict: repayment_difficulty_12m

Model performance is evaluated using:
Accuracy
Precision
Recall
F1 Score
Confusion Matrix

Decision Support Rules:

The machine learning model produces a repayment risk score which is converted into:

High Risk
Medium Risk
Low Risk

Additional decision rules provide reasoning based on:

Credit Score
Previous Default History
Debt-to-Income Ratio
Credit Utilisation
Missed Payments
Loan-to-Value Ratio

Testing:
Logical decision rules are tested using Python unit tests.
Command to run unit test: pytest

Technologies Used:
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
PyTest
