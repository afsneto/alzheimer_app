import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score
import pytest

# Requisitos mínimos de desempenho
MIN_ACCURACY = 0.64
MIN_RECALL = 0.80
MIN_F1 = 0.80
MIN_AUC = 0.85

# Carregar o modelo
@pytest.fixture(scope="module")
def model():
    with open('ML/models/model_svc.pkl', 'rb') as file:
        return pickle.load(file)

# Carregar os dados de teste
@pytest.fixture(scope="module")
def test_data():
    df = pd.read_csv('./ML/data/golden_dataset_test_alzheimer.csv')
    X_test = df.drop('Diagnosis', axis=1)
    y_test = df['Diagnosis']
    return X_test, y_test

def test_model_performance(model, test_data):
    X_test, y_test = test_data
    rescaledX_entrada = model[0].transform(X_test.values)
    y_pred = model[1].predict(rescaledX_entrada)

    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    # auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    
    print(f"Accuracy: {accuracy}")
    print(f"Recall: {recall}")
    print(f"F1-Score: {f1}")
    # print(f"AUC-ROC: {auc}")
    
    assert accuracy >= MIN_ACCURACY, f"Accuracy below threshold: {accuracy}"
    assert recall >= MIN_RECALL, f"Recall below threshold: {recall}"
    assert f1 >= MIN_F1, f"F1-Score below threshold: {f1}"
    # assert auc >= MIN_AUC, f"AUC-ROC below threshold: {auc}"
