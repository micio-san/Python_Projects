#flask is the server to run the api
from flask import Flask, request,jsonify

app= Flask(__name__)

@app.route("/")

def home():
    return "Home"

@app.route("/get_name/<user_id>")

def get_name(user_id):
    user_data=[{
        "user_id":1,
        "name":"Giacomo",
        "eta":30
    },{
        "user_id":2,
        "name":"Mist",
        "eta":29
    }]

    extra = request.args.get("extra")
    if extra:
        user_data["extra"]=extra

    return jsonify(user_data), 200

def home():
    return "Home"


if __name__== "__main__":
    app.run(debug=True)
    
