"""

Copyright 2021 SefaMerve R&D Center

"""
from lid import Lid 

class Model(object):
    def __init__(self):
        self.model = Lid('models/NBModel_full.jbl')
        
    def predict(self,query):
        prediction = None
        prediction = self.model.predict(query,5)      
        return str(prediction)
        

 
 