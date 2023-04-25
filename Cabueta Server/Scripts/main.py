from flask import Flask, render_template
from flask import request

import os

import pandas as pd
import requests
from bs4 import BeautifulSoup

import requests
import time

path = os.getcwd()
pathTemplates = path + "\\Cabueta Server\\templates"

# Adiciona o caminho raiz do projeto ao sys.path

app = Flask(__name__, template_folder=pathTemplates)

def execWebScrapping(link):
    response = requests.get(link)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    content_pg = soup.find_all(['h1', 'h2'])

    content = ""
    for tag in content_pg:
        content += tag.get_text()
    
    return content

@app.route("/", methods = ['POST'])
def principal():
    link_recebido = request.get_data()
    print(link_recebido)
    conteudoPagina = execWebScrapping(link_recebido)
    print(conteudoPagina)
    from verifyOnTrain import classify_news
    from generateGraph import createGraph
    resultadoAnalise = classify_news(conteudoPagina)
    imagemGerada = createGraph(resultadoAnalise) + ".png"
    time.sleep(1)
    from createHTML import createResultPage
    nome_arq_pagina = createResultPage("imagemResult.png")
    dataCompleto = [imagemGerada, nome_arq_pagina]

    with open(path + f"\\Cabueta Server\\Imgs\\{dataCompleto[1]}", 'rb') as f:
        requests.post("http://192.168.0.32:5000/upload", files={'paginaResult': f})
    with open(path + f"\\Cabueta Server\\Imgs\\{dataCompleto[0]}", 'rb') as f:
        requests.post("http://192.168.0.32:5000/upload", files={'imagemResult': f})
    
    print(resultadoAnalise[1][0])
    requests.post("http://192.168.0.32:5000/data", data=str(resultadoAnalise[1][0]))
    return 0


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=8000)
