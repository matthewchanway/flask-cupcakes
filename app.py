from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/api/cupcakes')
def list_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)


@app.route('/api/cupcakes/<int:cupcakeid>')
def show_cupcake(cupcakeid):
    cupcake = Cupcake.query.get_or_404(cupcakeid)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods = ["POST"])
def add_cupcake():
    new_cupcake = Cupcake(flavor = request.json["flavor"],
    size = request.json["size"],
    rating = request.json["rating"],
    image = request.json["image"]
    )
    db.session.add(new_cupcake)
    db.session.commit
    return(jsonify(cupcake=new_cupcake.serialize()),201)
