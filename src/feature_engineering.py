import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def feature_correlation(df): # Visualize the correlation between features in the DataFrame
    corr = df.corr(numeric_only=True) # Calculate the correlation matrix for the DataFrame, considering only numeric columns

    plt.figure(figsize=(16, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Feature Correlation Heatmap')
    plt.tight_layout()
    plt.show()
                

def feature_importance(df, model):
    importance_df = pd.DataFrame({'Feature': df.columns, 'Coefficient': model.coef_[0]}) # Create a DataFrame with features and their corresponding coefficients from the trained model
    print(importance_df.sort_values(by='Coefficient', key=abs, ascending=False)) # Print the features sorted by their absolute coefficient values in descending order

    importance_df["Absolute_Coefficient"] = importance_df["Coefficient"].abs() # Create a new column in the DataFrame for the absolute values of the coefficients
    importance_df = importance_df.sort_values(by="Absolute_Coefficient", ascending=False) # Sort the DataFrame by the absolute coefficient values in descending order

    importance_df.plot(kind='bar', x='Feature', y='Absolute_Coefficient', legend=False, figsize=(10, 5)) # Create a bar plot of the absolute coefficient values for each feature
    plt.title('Logistic Regression Feature Importance')
    plt.ylabel('Absolute Coefficient Value')
    plt.tight_layout()
    plt.show()

    # return importance_df["Feature"].tolist() # Return the list of features sorted by importance if needed
