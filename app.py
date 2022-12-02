from flask import Flask, render_template
import requests

app = Flask(__name__) #Crea la aplicación Flask.

@app.route("/") #Crear ruta home
def index(): #Función que devuelve una cadena de texto.
    respuesta = requests.get("https://rickandmortyapi.com/api/character/").json()
    personajes = respuesta['results']
    return render_template('index.html', personajes=personajes)  #Devuelve un archivo html y el json

if __name__ == "__main__":
    app.run(debug=True) #Ejecuta la aplicación Flask facilmente desde la terminal.
    # debug=True