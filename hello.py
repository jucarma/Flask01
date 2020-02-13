from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hola, mundo"

@app.route("/otrorecurso")
def otro():
    return "Este es otro recurso"