import pickle
from typing import List

from sklearn.decomposition import PCA


def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


def model_predict(model: PCA, x: List[float]):
    return model.transform(x)
