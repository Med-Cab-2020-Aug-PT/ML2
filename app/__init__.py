#app/__init__.py

from flask  import Flask

from app.routes.routes import routes


# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
# SECRET_KEY = os.getenv("SECRET_KEY")

def create_app():
    APP = Flask(__name__)
    # APP.config["SECRET_KEY"] = SECRET_KEY

    # APP.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    # APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # DB.init_app(APP)
    # migrate.init_app(APP, DB)

    APP.register_blueprint(routes)

    return APP

if __name__ == '__main__':
    
    my_app = create_app()
    my_app.run(debug=True)
