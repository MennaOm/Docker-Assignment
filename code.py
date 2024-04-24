
import pandas as pd
import nltk


txt= pd.read_csv("paragraphs.txt",delimiter='\t')


nltk.download('stopwords')
from nltk.corpus import stopwords
stop_word = set(stopwords.words('english'))

txt['text'] = txt['text'].apply(lambda stwo : " ".join([w for w in str(stwo).split() if w not in stop_word]))


from collections import Counter
words_count = txt['text'].str.split(expand=True).stack().value_counts()
print(words_count)
