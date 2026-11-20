from src.decision_rules import *

def test_risk_decision():
    assert risk_classification(35) == "High-Risk (35)"
    assert risk_classification(20) == "Medium Risk (20)"
    assert risk_classification(10) == "Low-Risk (10)"

def test_credit_score_decision():
    assert credit_score_classification(750) == "Strong Credit Score (750)"
    assert credit_score_classification(700) == "Average Credit Score (700)"
    assert credit_score_classification(600) == "Bad Credit Score (600)"

def test_previous_default_flag_decision():
    assert previous_default_flag_classification(1) == "Previous default recorded"
    assert previous_default_flag_classification(0) == "No previous default recorded"

def test_debt_to_income_decision():
    assert debt_to_income_classification(60) == "High debt-to-income ratio (60)"
    assert debt_to_income_classification(30) == "Medium debt-to-income ratio (30)"
    assert debt_to_income_classification(10) == "Low debt-to-income ratio (10)"

def test_credit_utilisation_decision():
    assert credit_utilisation_classification(60) == "High usage of credit utilisation (60)"
    assert credit_utilisation_classification(40) == "Medium usage of credit utilisation (40)"
    assert credit_utilisation_classification(20) == "Low usage of credit utilisation (20)"
    assert credit_utilisation_classification(0) == "No credit utilisation recorded (0)"

def test_missed_payment_decision():
    assert missed_payment_classification(3) == "3 missed payments in the previous 24 months"
    assert missed_payment_classification(0) == "No missed payments in the previous 24 months"

def test_load_to_value_decision():
    assert load_to_value_classification(90) == "High loan-to-value ratio (90)"
    assert load_to_value_classification(70) == "Moderate loan-to-value ratio (70)"
    assert load_to_value_classification(50) == "Low loan-to-value ratio (50)"

def test_recommendation():
    assert recommendation("High-Risk") == "Recommendation: High risk detected. Further review required. Consider additional checks or denial of application."
    assert recommendation("Medium Risk") == "Recommendation: Medium risk detected. Manual review required. Proceed with caution and consider additional checks."
    assert recommendation("Low-Risk") == "Recommendation: Low risk detected. Application can be processed with standard checks."

def test_reasoning():
    reasoning_result = reasoning("High-Risk", "Strong Credit Score", "Previous default recorded", "High debt-to-income ratio", "High usage of credit utilisation", "3 missed payments in the previous 24 months", "High loan-to-value ratio")
    assert reasoning_result == [
        "Risk Classification: High-Risk",
        "Credit Score Classification: Strong Credit Score",
        "Previous Default Flag Classification: Previous default recorded",
        "Debt-to-Income Classification: High debt-to-income ratio",
        "Credit Utilisation Classification: High usage of credit utilisation",
        "Missed Payment Classification: 3 missed payments in the previous 24 months",
        "Loan-to-Value Classification: High loan-to-value ratio"
    ]