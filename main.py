from flask import Flask
from views import views

def create_app():
    
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'end5373nbd0@$'

    app.register_blueprint(views, url_prefix='/')

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)