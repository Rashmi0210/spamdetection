from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd 

def prepare_data(path_to_data, encoding="latin-1"):
    # Read data from path
    data = pd.read_csv(path_to_data, encoding=encoding)

    # Encode labels
    data['label'] = data['v1'].map({'not spam': 0, 'spam': 1})

    X = data['v2']
    y = data['label']

    return {'text':X, 
            'label':y}

def create_train_test_data(X, y, test_size, random_state):
    cv = CountVectorizer()
    X = cv.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=test_size, 
                                                        random_state=random_state)

    return {'x_train': X_train, 'x_test': X_test,
            'y_train': y_train, 'y_test': y_test}, cv