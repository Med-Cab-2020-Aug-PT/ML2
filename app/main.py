from flask import request, render_template, flash, redirect, jsonify
from  app.model import PredictionBot

API = Flask(__name__)
API.config["MONGO_URI"] = os.getenv("MONGO_URL")


@API.route('/')
def index():
    return jsonify("App Online")

@API.route('/search/<user_input>')
def search(user_input):
    bot = PredictionBot()
    return jsonify(bot.cosine_recommender(user_input))

if __name__ == "__main__":
    API.run(debug=True)