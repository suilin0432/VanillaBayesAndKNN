import pandas as pd
import numpy as np
from .dataRead import wordList, classDict, wordD
from sklearn.feature_extraction.text import CountVectorizer
from SklearnVersionDataset import SklearnVersionDataset

class KNN(object):
    def __init__(self, K = 1):
        # 特征就不手动提取了
        S = SklearnVersionDataset()
        stringDataset, cls = S.get()
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform()
