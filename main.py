from flask import Flask, request, redirect, render_template, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['DEBUG'] = True
app.config["MONGO_URI"] = "mongodb+srv://Lucas:pokemon@pokedex.l4iml.mongodb.net/Pokedex?retryWrites=true&w=majority"
mongo = PyMongo(app)
  

@app.route('/Home')
def index():
    print("Home Endpoint: Hit")
    return render_template("home.html")

@app.route('/Pokecheck')
def pokecheck():
    print("Pokecheck Endpoint: Hit")
    pokechecks = mongo.db.Checklist.find()
    return render_template("pokecheck.html", pokechecks=pokechecks)


if __name__ == '__main__':
    print("Server UP")
    app.run()