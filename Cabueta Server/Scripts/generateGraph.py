import matplotlib.pyplot as plt
import numpy as np
import datetime

def createGraph(resultadosIA):
    y = np.array(resultadosIA[1]) # valores do vetor y

    y_percert = y*100

    max_y = int(max(y_percert))

    colors = ["green", "red"]
    x = np.arange(len(y)) # gerar os valores do eixo x
    plt.bar(x, y_percert, color=colors, width=0.6, align='center') # criar o gráfico de barras com as porcentagens
    plt.xticks(x) # definir os rótulos do eixo x
    plt.yticks(range(0,max_y + 3, 3))
    plt.xlabel('0: probabilidade de verdade, 1:probabilidade de fakenews')
    plt.ylabel('Porcentagem')
    plt.title('Gráfico da análise da notícia')

    now = datetime.datetime.now()
    plt.savefig(f"Cabueta Server\\Imgs\\{now.strftime('%Y-%m-%d_%H-%M-%S')}.png")
    return now.strftime('%Y-%m-%d_%H-%M-%S')
