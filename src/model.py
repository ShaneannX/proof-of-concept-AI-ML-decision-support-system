from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    model = LogisticRegression() # create model using LogisticRegression algorithm
    model.fit(X_train, y_train) # train model on train features and target
    return model # return model to use other built in methods. 

# Splits data 80% training and 20% test.
def split_data(X, Y): 
    return train_test_split(X,Y,random_state=42, test_size=0.2,shuffle=True)

# Scale numerical values
def scale_data(X_train, X_test):
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train) # Should only learn average and ranges from training data only

    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled