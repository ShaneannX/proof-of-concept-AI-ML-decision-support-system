
def risk_decision(risk): # Determine the risk level based on the risk score
    if risk > 30:
        return "High-Risk"
    elif risk <= 30 and risk >= 12:
        return "Medium Risk"
    else:
        return "Low-Risk"

def credit_score_decision(credit_score): # Determine the credit score level based on the credit score value

    if credit_score > 740:
        return "Strong Credit Score"
    elif credit_score <= 740 and credit_score >= 650:
        return "Average Credit Score"
    else:
        return "Bad Credit Score"

def previous_default_flag_decision(default_flag): # Determine if there is a previous default based on the default flag value
    if default_flag > 0:
        return "Previous default recorded"
    else:
        return "No previous default recorded"

def debt_to_income_decision(debt_to_income): # Determine the debt-to-income ratio level based on the debt-to-income value
    if debt_to_income > 50:
        return "High debt-to-income ratio"
    elif debt_to_income <= 50 and debt_to_income >= 20:
        return "Medium debt-to-income ratio"
    else:
        return "Low debt-to-income ratio"

def credit_utilisation_decision(credit_util): # Determine the credit utilisation level based on the credit utilisation value
    if credit_util > 50:
        return "High usage of credit utilisation"
    elif credit_util <= 50 and credit_util >= 30: 
        return "Medium usage of credit utilisation"
    elif credit_util < 30 and credit_util > 0:
        return "Low usage of credit utilisation"
    else:
        return "No credit utilisation recorded"

def missed_payment_decision(missed_payments): # Determine the missed payments level based on the missed payments value
    if missed_payments > 0:
        return f"{int(missed_payments)} missed payments in the previous 24 months"
    else:
        return "No missed payments in the previous 24 months"

def load_to_value_decision(loan_to_value): # Determine the loan-to-value ratio level based on the loan-to-value value
    if loan_to_value >= 85:
        return "High loan-to-value ratio"
    elif loan_to_value < 85 and loan_to_value >= 60:
        return "Moderate loan-to-value ratio"
    else:
        return "Low loan-to-value ratio"