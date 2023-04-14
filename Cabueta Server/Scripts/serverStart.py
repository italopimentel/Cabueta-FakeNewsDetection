from flask import Flask
from flask import request

app = Flask("Server")

global recebido

@app.route("/", methods = ['GET','POST'])
def principal():
    global recebido
    recebido = request.get_data()
    print(recebido, type(recebido))
    return "O que foi enviado foi: {}".format(recebido)  

app.run(host = '0.0.0.0', port=8000)