from flask import Flask
from database import db
from controllers.rotas import rotas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "biblioteca"

db.init_app(app)
app.register_blueprint(rotas)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)