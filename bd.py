from amazon import app, database
from amazon.models import Produto

with app.app_context():
    database.drop_all()
    database.create_all()

    produtos = [
        Produto(name="Bombom de Cupuaçu", description="Recheado com a polpa do verdadeiro cupuaçu amazônico.", image="assets/fotos/img001.jpeg"),
        Produto(name="Cachaça de Jambu", description="Toque vibrante do jambu com a força da cachaça paraense.", image="assets/produtos/cachaca_.png"),
        Produto(name="Caipirinha de Jambu", description="Refrescante e exótica: jambu com limão e cachaça.", image="assets/produtos/caipirinha_.png"),
        Produto(name="Farofa de Jambu", description="Crocante e aromática, perfeita para pratos amazônicos.", image="assets/produtos/farofa-jambu.png"),
        Produto(name="Farofa de Castanha-do-Pará", description="Sabor intenso da castanha em uma farofa deliciosa.", image="assets/produtos/farofa-sementes.png"),
        Produto(name="Farinha Amazônica", description="Autêntica farinha da região Norte, ideal para o dia a dia.", image="assets/produtos/farinha.jpeg"),
        Produto(name="Geleia de Maracujá", description="Sabor marcante e levemente ácido, perfeita no café da manhã.", image="assets/produtos/geleia_.png"),
        Produto(name="Bombom de Cupuaçu", description="Bombom de cupuaçu cremoso, autêntico sabor da Amazônia. 🍫🌱", image="assets/produtos/bombom.png")
    ]

    database.session.add_all(produtos)
    database.session.commit()
    print("Produtos inseridos!")
