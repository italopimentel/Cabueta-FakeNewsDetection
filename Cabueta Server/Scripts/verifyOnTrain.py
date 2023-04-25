import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle
# Define uma função para fazer a classificação de uma notícia
def classify_news(news):
    # Lê o arquivo pickle e carrega o modelo treinado
    with open('TrainedModels\\NB_TRAIN_.pkl', 'rb') as f:
        model = pickle.load(f)

    # Extrai o vetorizador e o classificador do modelo
    vectorizer, clf = model[0], model[1]

    # Transforma o texto da notícia em um vetor de frequência de palavras
    X = vectorizer.transform([news])

    # Faz a classificação da notícia usando o modelo treinado
    pred = clf.predict(X)[0]

    probabilidade = clf.predict_proba(X)[0]

    # Retorna o resultado da classificação (fake ou não-fake)
    return pred, probabilidade


# Exemplo de uso da função
#news = "Estudo comprova que a vacina Coronavac é eficaz contra a COVID-19"
#news = "Lula se entrega à PF e é preso para cumprir pena por corrupção e lavagem de dinheiro"
#news = "Show de carnaval em recife contará com a presença de Pablo Vittar"


