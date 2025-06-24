from amazon import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

class Produto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    description = database.Column(database.Text, nullable=False)
    image = database.Column(database.String(255), nullable=False)

class Usuarios(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    zip_code = database.Column(database.String, nullable=False)
    city = database.Column(database.String, nullable=False)
    state = database.Column(database.String, nullable=False)
    address = database.Column(database.String, nullable=False)
