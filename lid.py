"""

Copyright 2021 SefaMerve R&D Center

"""
import joblib
import numpy as np

class Lid(object):
    def __init__(self,fname):
        with open(fname,'rb') as fp:
            data = joblib.load(fp)

        self.clf = data['classifier']
        self.vectorizer = data['vectorizer']
        self.diller = data['languages']

    def predict(self,text,topk=1):
        x = self.vectorizer.transform([text])
        res = self.clf.predict_proba(x)[0]
        ix = list(np.argsort(-res))[:topk]
        return [(self.diller[x],np.round(100*res[x],2)) for x in ix]


