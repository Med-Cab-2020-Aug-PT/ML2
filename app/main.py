from flask import Flask, jsonify

API = Flask(__name__)

@API.rout('/')
def index():
    return "App Online"


if __name__ == '__main__':
    API.run(debug = True)