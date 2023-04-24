import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle

# Lê o arquivo pickle e carrega o modelo treinado
with open('TrainedModels\\NB_TRAIN_.pkl', 'rb') as f:
    model = pickle.load(f)

# Extrai o vetorizador e o classificador do modelo
vectorizer, clf = model[0], model[1]

# Define uma função para fazer a classificação de uma notícia
def classify_news(news):
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

news = "Investigação apontam que o ex presidente lula desviou dinheiro em seu governo"
result = classify_news(news)
print(result)  # imprime 'non-fake'


# se quiser usar depois, recomendo:
'''
prob_fake = probabilidade[0]
prob_non_fake = probabilidade[1]

# Exibe o resultado
if predicao == 0:
    print("A notícia é FAKE com {:.2f}% de probabilidade".format(prob_fake*100))
else:
    print("A notícia é NON-FAKE com {:.2f}% de probabilidade".format(prob_non_fake*100))
'''


