

def createResultPage(imagemNAME):
    pagina = f'''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Resultados</title>
  </head>
  <body>
    <h1>Aqui estao os resultados analisado da página fornecidade</h1>
    <p></p>
    <img src={imagemNAME}></img>
    <p>A IA utiliza o algoritmo de NB (Naive Bayes) para detectar padrões de texto, para isso foram treinados <br>
  mais de 7200 notícias para identificar possíveis padrões de fakenews, a porcentagem mostrado acima foi <br>
  um retorno desse treinamento</p>
  </body>
</html>'''
    file = open("Cabueta Server\\Imgs\\results.html", "w")
    file.writelines(pagina)
    file.close()
    return "results.html"