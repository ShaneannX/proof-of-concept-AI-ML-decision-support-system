import pandas as pd

# Process csv into dataframe
def process_csv(filepath):
    df = pd.read_csv(filepath)
    return df

# Remove unnesscery columns for ML
def remove_unnesscery_columns(df,col:list):
    for c in col:
        c = str(c) # assures the column is a string
        df = df.drop(c, axis=1) # application id is not neccessary and can skew results.
    return df

# Handle categorical data into numerical data
def handle_categorical_data(df):
    df_encoded = pd.get_dummies(df, dtype=int) # created new columns of the options to have value True (1) or False (0)

    return df_encoded

# Handles missing values (Imputation)
def check_missing_columns(df):

    rows_with_missing_values = df[df.isnull().any(axis=1)]
    columns_with_missing_values = 0
    if len(rows_with_missing_values) > 0:
        print(f'There are {len(rows_with_missing_values)} rows with missing values! Attempting to replace...')
        columns_with_missing_values = df.isnull().sum() # Shows columns and how many missing values
        # print(columns_with_missing_values) # for visuality
        columns_with_missing_values = columns_with_missing_values[columns_with_missing_values > 0] # filters to only show which columns have missing value for better readability
        # print(columns_with_missing_values) # only shows columns with missing values
        missing_columns_list = df.columns[df.isnull().any()].tolist() # Gives names of columns with missing values in a list
        print(missing_columns_list)
        return missing_columns_list # returns columns list to then fill the missing values
    else:
        columns_with_missing_values
    
# replace missing values with mean
def replace_missing_values(df):
    missing_columns_list = check_missing_columns(df)
    print(f"Missing columns list: {len(missing_columns_list)}")
    if len(missing_columns_list) > 0:
        for column in missing_columns_list:
            if df[column].dtype in ['float64', 'int64']: # Check if the column is numeric
                df[column] = df[column].fillna(df[column].mean()) # Fill missing values with the mean of the column

    if check_missing_columns(df) is None:
        print("All missing values have been filled successfully.")
        return df
    else:
        raise ValueError("Failed to fill all missing values. Investigation needed!") # prevents the program from continuing if there are still missing values after the imputation process

# prepares features and target
def get_features_and_target(df, target, features=None):
    if features is None:
        X = df.drop(target, axis=1) # all the columns and values apart from the target
    else:
        X = df[[col for col in features if col != target]] # only the columns specified in the features list, excluding the target column
    Y = df[target]
    return X, Y
