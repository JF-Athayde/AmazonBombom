from amazon import app, database
from amazon.models import Produto, Partner
import random

with app.app_context():
    database.drop_all()
    database.create_all()

    produtos = [
        Produto(
            name="Salame de Cupuaçu",
            description="Uma sobremesa sofisticada e regional que une o melhor do chocolate com o toque amazônico do cupuaçu. O salame de cupuaçu é ideal para quem busca uma experiência doce diferente, com textura macia e o sabor marcante da fruta amazônica, levemente ácida e refrescante. É finalizado com castanhas-do-pará, oferecendo crocância e identidade ao doce. Ideal para presentear ou degustar após as refeições. 70g",
            short_description="Doce regional de cupuaçu com castanha do Pará.",
            image="assets/produtos/salame.png",
            price=18.00,
            fake=random.randint(120, 150)
        ),

        Produto(
            name="Cachaça de Jambu",
            description="A tradicional cachaça brasileira ganha um toque eletrizante com a infusão de jambu, a planta amazônica conhecida por seu leve efeito anestésico e vibrante na boca. Ideal para drinks ousados ou para ser degustada pura, a Cachaça de Jambu é um símbolo da cultura paraense, trazendo personalidade e regionalidade a qualquer celebração.",
            short_description="Cachaça com sabor e efeito do jambu.",
            image="assets/produtos/cachaca_.png",
            price=45.00,
            fake=random.randint(120, 150)
        ),

        Produto(
            name="Doce de Cupuaçu",
            description=(
                "Delicioso doce cremoso feito exclusivamente com a polpa pura do cupuaçu, fruta típica da floresta amazônica. Sua textura aveludada e sabor agridoce proporcionam uma explosão sensorial marcante, equilibrando doçura e acidez. Ideal para ser consumido puro, com torradas ou como recheio de sobremesas. Um potinho que concentra a alma da Amazônia."
            ),
            short_description="Doce cremoso de cupuaçu",
            image="assets/produtos/doce-cupuacu.png",
            price=6.50,
            fake=random.randint(120, 150)
        ),

        Produto(
            name="Caipirinha de Jambu",
            description="Uma releitura amazônica do drink mais famoso do Brasil. A Caipirinha de Jambu une a refrescância do limão com o efeito levemente anestésico do jambu, resultando em uma bebida surpreendente. Ideal para dias quentes e encontros festivos, esse coquetel proporciona uma sensação única e divertida no paladar, deixando a língua levemente dormente e cheia de sabor.",
            short_description="Drink amazônico com jambu e limão.",
            image="assets/produtos/caipirinha_.png",
            price=18.50,
            fake=random.randint(120, 150)
        ),

        Produto(
            name="Farofa de Jambu",
            description="Farofa artesanal crocante com toques da planta amazônica jambu, que adiciona leve frescor e sabor terroso ao prato. Ideal como acompanhamento para carnes grelhadas, peixes ou pratos regionais. A combinação do crocante da farinha com o jambu proporciona uma experiência típica da culinária nortista com um toque de originalidade.",
            short_description="Farofa crocante com aroma de jambu.",
            image="assets/produtos/farofa-jambu.png",
            price=14.75,
            fake=random.randint(120, 150)
        ),

        Produto(
            name="Farofa de Castanha-do-Pará",
            description="Combinando a crocância da farinha com o sabor nobre e amanteigado da castanha-do-pará, esta farofa é perfeita para dar sofisticação aos seus pratos. Rica em nutrientes e sabor, acompanha desde churrascos até pratos vegetarianos, adicionando textura e um toque amazônico à sua refeição.",
            short_description="Farofa com sabor marcante da castanha.",
            image="assets/produtos/farofa-sementes.png",
            price=16.20,
            fake=random.randint(120, 150)
        ),

        Produto(
            name="Farinha Amazônica",
            description="A autêntica farinha da região Norte, feita com mandioca selecionada e processada de forma tradicional. Levemente torrada e com textura crocante, é ideal para acompanhar peixes, caldos e açaí. Um produto essencial nas mesas nortistas, representando sabor, cultura e versatilidade.",
            short_description="Farinha típica e versátil da Amazônia.",
            image="assets/produtos/farinha.jpeg",
            price=10.00,
            fake=random.randint(120, 150)
        ),

        Produto(
            name="Geleia de Maracujá",
            description="Feita com maracujás frescos, essa geleia artesanal combina acidez equilibrada com doçura natural. Com textura suave e sabor marcante, é ideal para acompanhar pães, torradas, queijos ou como cobertura de sobremesas. Uma opção tropical e aromática que remete ao calor e frescor do Norte brasileiro.",
            short_description="Geleia fresca de maracujá para o café.",
            image="assets/produtos/geleia_.png",
            price=22.30,
            fake=random.randint(120, 150)
        )
    ]

    database.session.add_all(produtos)
    database.session.commit()
    print("Produtos inseridos!")

    parceiros = [
        Partner(
            name="Chico do Caranguejo",
            image="assets/parceiros/chico.png"
        ),
        Partner(
            name="Croco Beach",
            image="assets/parceiros/croco.png"
        ),
        Partner(
            name="Emporio Delitalia",
            image="assets/parceiros/delitalia.png"
        ),
        Partner(
            name="Feijão Verde",
            image="assets/parceiros/feijao.png"
        ),
        Partner(
            name="Iate Clube",
            image="assets/parceiros/iate.png"
        ),
        Partner(
            name="Fazendinha",
            image="assets/parceiros/fazendinha.png"
        )
    ]

    database.session.add_all(parceiros)
    database.session.commit()
    print("Parceiros inseridos!")
