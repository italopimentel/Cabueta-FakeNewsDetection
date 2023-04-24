import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle

# Carrega os dados
import pandas as pd

# Lê o arquivo de texto e armazena em um DataFrame
df = pd.read_csv('Corpus\\normalizedData.txt', delimiter='\t', header=None, names=['label', 'text'])

print(df.head())
print(df.columns)

# Divide em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Transforma os textos em vetores de frequência de palavras
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Treina um modelo de Naive Bayes Multinomial
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Avalia o modelo
score = clf.score(X_test, y_test)
print("Acurácia: {:.2f}%".format(score*100))

# Salva o modelo treinado em um arquivo pkl
with open('TrainedModels\\NB_TRAIN_.pkl', 'wb') as f:
    pickle.dump((vectorizer, clf), f)
