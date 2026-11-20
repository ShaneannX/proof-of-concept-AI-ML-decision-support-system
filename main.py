from src.preprocess import *
from src.model import *
from src.evaluation import *
from src.decision_rules import *
from src.feature_engineering import *
import pandas as pd

### Preprocess the data
df = process_csv('data/A2 Mortgage Credit Risk Dataset.csv')

application_id = df['application_id'].copy() # copy application_id column to use for later reference

df = remove_unnesscery_columns(df, ['application_id'])

df = handle_categorical_data(df)

df = replace_missing_values(df)

# features = feature_correlation(df) # Visualize the correlation between features

features = [ # List of features in order of importance based on feature importance analysis
    "credit_score",
    "missed_payments_24m",
    "previous_default_flag",
    "credit_utilisation_pct",
    "term_years",
    "annual_income_gbp",
    "employment_years",
    "requested_loan_gbp",
    "loan_to_value_pct",
    "deposit_gbp",
    "debt_to_income_ratio",
    "employment_type_Employed",
    "property_value_gbp",
    "employment_type_Self-employed",
    "employment_type_Contractor",
    "savings_gbp",
    "application_channel_Broker",
    "application_channel_Online",
    "interest_rate_pct",
    "monthly_debt_commitments_gbp",
    "application_channel_Branch"
]

final_features = []
for i in range(18): # Loop through the first 18 features in the list
    final_features.append(features[i])
features = None

X, y = get_features_and_target(df, 'repayment_difficulty_12m', features=final_features) # Get features and target for model training

## Train the model

X_train, X_test, y_train, y_test = split_data(X,y)

X_train_scaled, X_test_scaled = scale_data(X_train, X_test)

model = train_model(X_train_scaled, y_train)



# importance_df = feature_importance(X, model) # Visualize the importance of features


evaluation_results = model_evaluation(model, X_test_scaled, y_test)

print(f"Evaluation results: accuracy={evaluation_results['accuracy']}, precision={evaluation_results['precisions']}, recall={evaluation_results['recall']}, f1={evaluation_results['f1']}, confusion_matrix={evaluation_results['matrix']}")
results = {
    "application_id": [],
    "recommendation": [],
    "reasoning": [],
}
for i in range(len(X_test_scaled)):
    risk_score = model.predict_proba([X_test_scaled[i]])[0][1] # Get the risk score for the current test instance
    risk_score = round(risk_score * 100, 2) # Convert the risk score to a percentage
    credit_score = round(X_test.iloc[i]['credit_score']) # Get the credit score for the current test instance
    default_flag = X_test.iloc[i]['previous_default_flag'] # Get the previous default flag for the current test instance
    debt_to_income = round(X_test.iloc[i]['debt_to_income_ratio'], 2) # Get the debt-to-income ratio for the current test instance
    credit_util = X_test.iloc[i]['credit_utilisation_pct'] # Get the credit utilisation for the current test instance
    missed_payments = X_test.iloc[i]['missed_payments_24m'] # Get the missed payments in the last 24 months for the current test instance
    loan_to_value = X_test.iloc[i]['loan_to_value_pct'] # Get the loan-to-value ratio for the current test instance

    risk_decision_result = risk_classification(risk_score)
    credit_score_decision_result = credit_score_classification(credit_score)
    previous_default_flag_decision_result = previous_default_flag_classification(default_flag)
    debt_to_income_decision_result = debt_to_income_classification(debt_to_income)
    credit_utilisation_decision_result = credit_utilisation_classification(credit_util)
    missed_payment_decision_result = missed_payment_classification(missed_payments)
    loan_to_value_decision_result = load_to_value_classification(loan_to_value)

    recommendation_result = recommendation(risk_decision_result)
    reasoning_result = reasoning(risk_decision_result, credit_score_decision_result, previous_default_flag_decision_result, debt_to_income_decision_result, credit_utilisation_decision_result, missed_payment_decision_result, loan_to_value_decision_result)
    reasoning_text ="\n".join(reasoning_result)

    results["application_id"].append(application_id.iloc[i])
    results["recommendation"].append(recommendation_result)
    results["reasoning"].append(reasoning_text)

# Below are some commented-out print statements that can be used for debugging or analysis purposes. They provide insights into the risk scores and other relevant metrics.
# print(f"Minimum Risk Score: {min(risks)}")
# print(f"Maximum Risk Score: {max(risks)}")
# print(f"Average Risk Score: {sum(risks)/len(risks)}")
# print(df["credit_score"].describe())
# print(df["loan_to_value_pct"].describe())
# print(df["debt_to_income_ratio"].describe())
# print(df["credit_utilisation_pct"].describe())
# print(df['credit_score'].mean())
df_results = pd.DataFrame(results) # Create a DataFrame from the results dictionary to store the evaluation results and decisions for each application
df_results.to_csv('data/results.csv', index=False) # Save the results DataFrame to a CSV file for further analysis or reporting