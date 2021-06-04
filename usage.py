"""
Copyright 2021 SefaMerve R&D Center

"""
from lid import Lid

model = Lid('models/NBModel_full.jbl')
text = "La rue double en longueur et s'urbanise durant le XIXe siècle ; plusieurs usines et ateliers s'y installent."
res = model.predict(text,topk=5)

print(res)
