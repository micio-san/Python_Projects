#pip let's us install programs that are not already included with python
#pip installs programs globally, if needed different create a virtual enviroment to contain specific libraries, 
#but don't put in github
#py -m venv ./name
#-m mod : run library module as a script 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import abort, Resource, Api, reqparse, fields, marshal_with
from pprint import pprint
import json

app= Flask(__name__)
# The config is actually a subclass of a dictionary and can be modified just like any dictionary
pprint(json.dumps(app.config))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

db = SQLAlchemy(app)
api=Api(app)
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True,help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True,help="Email cannot be blank")

class UserModal(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=True, nullable=False)
    email=db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"user(name={self.name}, mail={self.mail})"

@app.route("/")

def homepage():
    return '<h1>Ass</h1>'

if __name__ == "__main__":
    app.run(debug=True)