# Yazılı Metin Dilini Algılama Modeli

WiLI-2018 veri seti ile eğitilmiş yazılı metin dilini algılama modeli

## Veri Kümesi

WiLI-2018, yazılı metin dil tanımlaması için bir oluşturulmuş bir veri kümesidir. WiLI-2018, Wikipedia'dan kısa metin alıntıları içeren, halka açık, ücretsiz bir veri kümesidir. Toplam 23500 paragrafta olmak üzere 235 dilde 1000 paragraf içerir. 

Makale :  https://arxiv.org/pdf/1801.07779.pdf

İndir : https://zenodo.org/record/841984

## Model 

tf-idf ile vektörize eden Naive Bayes sınıflandırıcısı modeli kullanılmışır 

## Kullanım

```python
from lid import Lid

model = Lid('models/NBModel_full.jbl')
text = "La rue double en longueur et s'urbanise durant le XIXe siècle ; plusieurs usines et ateliers s'y installent."
model.predict(text,topk=5)

```
### çıktı 

```python
[('French', 74.38),
 ('Occitan', 6.33),
 ('Picard', 2.59),
 ('Narom', 2.36),
 ('Arpitan', 2.35)]
```

## Sonuçlar

Overall results of trained model for test set of data

| Metric   | Score |
|----------|-------|
| Accuracy | 0.95  |
| Recall   | 0.93  |
| F1       | 0.93  |

## Detaylı Sonuçlar 

[full_results.md](full_results.md)
