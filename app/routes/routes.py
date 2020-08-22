#app/routes/routes.py


from flask import Blueprint

routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    print("Visiting home page")
    return "About me"