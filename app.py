from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def sobre():
    return "Sobre"

if __name__ == "__main__": #recomendado em desenvolvimento local (executado de forma manual)
    app.run(debug=True)