from flask import Flask
from db import get_one_country, get_top_10
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    top_10 = json.dumps(get_top_10())
    return top_10

@app.route("/<id>")
def hello_world_one(id):
    one_c = json.dumps(get_one_country(id_=id))
    return one_c

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

