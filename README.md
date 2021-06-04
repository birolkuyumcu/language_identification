# Language Identification Model

language identification model trained with WiLI-2018

## Dataset

WiLI-2018 is a benchmark dataset for monolingual written natural language identification. WiLI-2018 is a publicly available, free of charge dataset of short text extracts from Wikipedia. It contains 1000 paragraphs of 235 languages, totaling in 23500 paragraphs. WiLI is a classification dataset: Given an unknown paragraph written in one dominant language, it has to be decided which language it is.

Paper :  https://arxiv.org/pdf/1801.07779.pdf

Download : https://zenodo.org/record/841984

## Model 

tf-idf vectorized text and  Naive Bayes classifier for multinomial models used 

## Usage

```python
from lid import Lid

model = Lid('models/NBModel_full.jbl')
text = "La rue double en longueur et s'urbanise durant le XIXe siècle ; plusieurs usines et ateliers s'y installent."
model.predict(text,topk=5)

```
### output 

```python
[('French', 74.38),
 ('Occitan', 6.33),
 ('Picard', 2.59),
 ('Narom', 2.36),
 ('Arpitan', 2.35)]
```

## Results

Overall results of trained model for test set of data

| Metric   | Score |
|----------|-------|
| Accuracy | 0.95  |
| Recall   | 0.93  |
| F1       | 0.93  |

## Detailed Results 

[full_results.md](full_results.md)

## FastAPI

for starting server
```bash
uvicorn main:app --reload
```

for documentation 

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

after started server