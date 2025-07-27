from amazon import app, database
from amazon.models import Produto
import random

with app.app_context():
    database.drop_all()
    database.create_all()

    produtos = [
        Produto(
            name="Cachaça de Jambu",
            description="Toque vibrante do jambu com a força da cachaça paraense.",
            short_description="Cachaça com sabor e efeito do jambu.",
            image="assets/produtos/cachaca_.png",
            price=45.00,
            fake=random.randint(120, 150)
        ),
        Produto(
            name="Caipirinha de Jambu",
            description="Refrescante e exótica: jambu com limão e cachaça.",
            short_description="Drink amazônico com jambu e limão.",
            image="assets/produtos/caipirinha_.png",
            price=18.50,
            fake=random.randint(120, 150)
        ),
        Produto(
            name="Farofa de Jambu",
            description="Crocante e aromática, perfeita para pratos amazônicos.",
            short_description="Farofa crocante com aroma de jambu.",
            image="assets/produtos/farofa-jambu.png",
            price=14.75,
            fake=random.randint(120, 150)
        ),
        Produto(
            name="Farofa de Castanha-do-Pará",
            description="Sabor intenso da castanha em uma farofa deliciosa.",
            short_description="Farofa com sabor marcante da castanha.",
            image="assets/produtos/farofa-sementes.png",
            price=16.20,
            fake=random.randint(120, 150)
        ),
        Produto(
            name="Farinha Amazônica",
            description="Autêntica farinha da região Norte, ideal para o dia a dia.",
            short_description="Farinha típica e versátil da Amazônia.",
            image="assets/produtos/farinha.jpeg",
            price=10.00,
            fake=random.randint(120, 150)
        ),
        Produto(
            name="Geleia de Maracujá",
            description="Sabor marcante e levemente ácido, perfeita no café da manhã.",
            short_description="Geleia fresca de maracujá para o café.",
            image="assets/produtos/geleia_.png",
            price=22.30,
            fake=random.randint(120, 150)
        )
    ]

    database.session.add_all(produtos)
    database.session.commit()
    print("Produtos inseridos!")
