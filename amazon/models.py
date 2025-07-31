from amazon import database, login_manager
from flask_login import UserMixin
import random

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

class Produto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    description = database.Column(database.Text, nullable=False)
    short_description = database.Column(database.String(150), nullable=True)  # novo campo
    image = database.Column(database.String(255), nullable=False)
    price = database.Column(database.Float, nullable=False)
    fake = database.Column(database.Integer, nullable=False, default=random.randint(120, 150))

class Usuarios(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    password = database.Column(database.String, nullable=False)
    zip_code = database.Column(database.String, nullable=False)
    city = database.Column(database.String, nullable=False)
    state = database.Column(database.String, nullable=False)
    address = database.Column(database.String, nullable=False)

class ContactMessage(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(120), nullable=False)
    message = database.Column(database.Text, nullable=False)

class Partner(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    image = database.Column(database.String(255), nullable=False)