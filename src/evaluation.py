from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

def model_evaluation(model, X_test, Y_test): # Evaluate the performance of a trained model
    """
    Evaluate the performance of a trained model using various metrics.
    """
    predictions = model.predict(X_test) # Make predictions on the test set

    accuracy = accuracy_score(Y_test, predictions) # Calculate accuracy of the model

    precisions = precision_score(Y_test, predictions) # Calculate precision of the model

    recall = recall_score(Y_test, predictions) # Calculate recall of the model

    f1 = f1_score(Y_test, predictions) # Calculate F1 score of the model

    matrix = confusion_matrix(Y_test, predictions) # Calculate confusion matrix of the model

    return {
        "predictions": predictions,
        "accuracy" : accuracy,
        "precisions" : precisions,
        "recall": recall,
        "f1": f1,
        "matrix": matrix
    }