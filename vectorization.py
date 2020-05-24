# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:49:00 2020

@author: Khadija Kamran
"""
import pandas as pd 

df = pd.read_pickle("All files")
print(df.info())

from sklearn.feature_extraction.text import TfidfVectorizer
def vectorize(text, maxx_features):
    vectorizer = TfidfVectorizer(max_features=maxx_features)
    X = vectorizer.fit_transform(text)
    return X

text = df['body_text'].values
X = vectorize(text, 8000)

from sklearn.decomposition import PCA

pca = PCA(n_components=0.95, random_state=42)
X_reduced= pca.fit_transform(X.toarray())
X_reduced.shape