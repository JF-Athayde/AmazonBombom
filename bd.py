from amazon import app, database
from amazon.models import Produto
import random

with app.app_context():
    database.drop_all()
    database.create_all()

    produtos = [
        Produto(name="Bombom de Cupuaçu", description="Recheado com a polpa do verdadeiro cupuaçu amazônico.", image="assets/fotos/img001.jpeg", price=12.90, fake=random.randint(120, 150)),
        Produto(name="Cachaça de Jambu", description="Toque vibrante do jambu com a força da cachaça paraense.", image="assets/produtos/cachaca_.png", price=45.00, fake=random.randint(120, 150)),
        Produto(name="Caipirinha de Jambu", description="Refrescante e exótica: jambu com limão e cachaça.", image="assets/produtos/caipirinha_.png", price=18.50, fake=random.randint(120, 150)),
        Produto(name="Farofa de Jambu", description="Crocante e aromática, perfeita para pratos amazônicos.", image="assets/produtos/farofa-jambu.png", price=14.75, fake=random.randint(120, 150)),
        Produto(name="Farofa de Castanha-do-Pará", description="Sabor intenso da castanha em uma farofa deliciosa.", image="assets/produtos/farofa-sementes.png", price=16.20, fake=random.randint(120, 150)),
        Produto(name="Farinha Amazônica", description="Autêntica farinha da região Norte, ideal para o dia a dia.", image="assets/produtos/farinha.jpeg", price=10.00, fake=random.randint(120, 150)),
        Produto(name="Geleia de Maracujá", description="Sabor marcante e levemente ácido, perfeita no café da manhã.", image="assets/produtos/geleia_.png", price=22.30, fake=random.randint(120, 150)),
        Produto(name="Bombom de Cupuaçu", description="Bombom de cupuaçu cremoso, autêntico sabor da Amazônia. 🍫🌱", image="assets/produtos/bombom.png", price=13.50, fake=random.randint(120, 150))
    ]

    database.session.add_all(produtos)
    database.session.commit()
    print("Produtos inseridos!")
