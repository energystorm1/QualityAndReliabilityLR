import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def lemmatize(text):
    words = nltk.word_tokenize(text)#Достаем слова из предложений
    #фильтруем стоп слова и знаки припинания
    filtredWords = [word for word in words if (word not in stops) and (word not in punc_str)]
    ulemms = list()
    wordnet = WordNetLemmatizer()
    for fw,tag in nltk.pos_tag(filtredWords):
        pos=tag[0].lower()
        if pos not in ['a', 'r', 'n', 'v']:
            pos='n'
        lemm = wordnet.lemmatize(fw,pos)#Лемматизируем слова
        if lemm not in ulemms:
            ulemms.append(lemm)#Добавляем только уникальные леммы
    return ulemms

raw_text = open(r'sem.txt', encoding='utf-8-sig').read()
punc_str = "!?()-[]{};:@#$%^',.\|/*-<>_~'’‘";
stops = set(stopwords.words('english'))
sentences = nltk.sent_tokenize(raw_text)#Разбиваем на предложения
vectorizer = CountVectorizer(tokenizer=lemmatize)#Создаем объект векторизаторизатора с созданым нами Лемматизатором
bag_of_words = vectorizer.fit_transform(sentences)#Создаем мешок слов
col_names = vectorizer.get_feature_names_out()#Названия колонок(леммы)
print(pd.DataFrame(bag_of_words.toarray(), columns=col_names[:53]))
