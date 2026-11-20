
def risk_classification(risk): # Determine the risk level based on the risk score
    if risk > 30:
        return f"High-Risk ({risk})"
    elif risk <= 30 and risk >= 12:
        return f"Medium Risk ({risk})"
    else:
        return f"Low-Risk ({risk})"

def credit_score_classification(credit_score): # Determine the credit score level based on the credit score value

    if credit_score > 740:
        return f"Strong Credit Score ({credit_score})"
    elif credit_score <= 740 and credit_score >= 650:
        return f"Average Credit Score ({credit_score})"
    else:
        return f"Bad Credit Score ({credit_score})"

def previous_default_flag_classification(default_flag): # Determine if there is a previous default based on the default flag value
    if default_flag > 0:
        return f"Previous default recorded"
    else:
        return "No previous default recorded"

def debt_to_income_classification(debt_to_income): # Determine the debt-to-income ratio level based on the debt-to-income value
    if debt_to_income > 50:
        return f"High debt-to-income ratio ({debt_to_income})"
    elif debt_to_income <= 50 and debt_to_income >= 20:
        return f"Medium debt-to-income ratio ({debt_to_income})"
    else:
        return f"Low debt-to-income ratio ({debt_to_income})"

def credit_utilisation_classification(credit_util): # Determine the credit utilisation level based on the credit utilisation value
    if credit_util > 50:
        return f"High usage of credit utilisation ({credit_util})"
    elif credit_util <= 50 and credit_util >= 30: 
        return f"Medium usage of credit utilisation ({credit_util})"
    elif credit_util < 30 and credit_util > 0:
        return f"Low usage of credit utilisation ({credit_util})"
    else:
        return f"No credit utilisation recorded ({credit_util})"

def missed_payment_classification(missed_payments): # Determine the missed payments level based on the missed payments value
    if missed_payments > 0:
        return f"{int(missed_payments)} missed payments in the previous 24 months"
    else:
        return f"No missed payments in the previous 24 months"

def load_to_value_classification(loan_to_value): # Determine the loan-to-value ratio level based on the loan-to-value value
    if loan_to_value >= 85:
        return f"High loan-to-value ratio ({loan_to_value})"
    elif loan_to_value < 85 and loan_to_value >= 60:
        return f"Moderate loan-to-value ratio ({loan_to_value})"
    else:
        return f"Low loan-to-value ratio ({loan_to_value})"

def recommendation(risk_classification): # Provide a recommendation based on the risk classification
    if "High-Risk" in risk_classification:
        return "Recommendation: High risk detected. Further review required. Consider additional checks or denial of application."
    elif "Medium Risk" in risk_classification:
        return "Recommendation: Medium risk detected. Manual review required. Proceed with caution and consider additional checks."
    else:
        return "Recommendation: Low risk detected. Application can be processed with standard checks."

def reasoning(risk_classification, credit_score_classification, previous_default_flag_classification, debt_to_income_classification, credit_utilisation_classification, missed_payment_classification, loan_to_value_classification): # Provide reasoning for the decisions
    results = []
    results.append(f"Risk Classification: {risk_classification}")
    results.append(f"Credit Score Classification: {credit_score_classification}")   
    results.append(f"Previous Default Flag Classification: {previous_default_flag_classification}")
    results.append(f"Debt-to-Income Classification: {debt_to_income_classification}")
    results.append(f"Credit Utilisation Classification: {credit_utilisation_classification}")
    results.append(f"Missed Payment Classification: {missed_payment_classification}")
    results.append(f"Loan-to-Value Classification: {loan_to_value_classification}")
    
    return results