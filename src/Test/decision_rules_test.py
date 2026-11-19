from src.decision_rules import *

def test_risk_decision():
    assert risk_decision(35) == "High-Risk"
    assert risk_decision(20) == "Medium Risk"
    assert risk_decision(10) == "Low-Risk"

def test_credit_score_decision():
    assert credit_score_decision(750) == "Strong Credit Score"
    assert credit_score_decision(700) == "Average Credit Score"
    assert credit_score_decision(600) == "Bad Credit Score"

def test_previous_default_flag_decision():
    assert previous_default_flag_decision(1) == "Previous default recorded"
    assert previous_default_flag_decision(0) == "No previous default recorded"

def test_debt_to_income_decision():
    assert debt_to_income_decision(60) == "High debt-to-income ratio"
    assert debt_to_income_decision(30) == "Medium debt-to-income ratio"
    assert debt_to_income_decision(10) == "Low debt-to-income ratio"

def test_credit_utilisation_decision():
    assert credit_utilisation_decision(60) == "High usage of credit utilisation"
    assert credit_utilisation_decision(40) == "Medium usage of credit utilisation"
    assert credit_utilisation_decision(20) == "Low usage of credit utilisation"
    assert credit_utilisation_decision(0) == "No credit utilisation recorded"

def test_missed_payment_decision():
    assert missed_payment_decision(3) == "3 missed payments in the previous 24 months"
    assert missed_payment_decision(0) == "No missed payments in the previous 24 months"

def test_load_to_value_decision():
    assert load_to_value_decision(90) == "High loan-to-value ratio"
    assert load_to_value_decision(70) == "Moderate loan-to-value ratio"
    assert load_to_value_decision(50) == "Low loan-to-value ratio"