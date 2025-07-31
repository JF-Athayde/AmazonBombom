from flask import *
from amazon import app, database, bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from amazon.form import *
from amazon.models import Usuarios, Produto, ContactMessage, Partner
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect, CSRFError

PRODUTO1 = Produto(
            name="Bombons de Cupuaçu",
            description="Bombom de cupuaçu recheado com a pura polpa da fruta, fresca e autêntica. com recheio suave e consistente, envolto em chocolate meio amargo. 🍫🌱",
            short_description="Bombom de cupuaçu com chocolate meio amargo.",
            image= "assets/produtos/bombom.png",
            price=5.50,
            fake=145
        )

PRODUTO2 = Produto(
            name="Bombons de Cupuaçu",
            description="Bombom de cupuaçu recheado com a pura polpa da fruta, fresca e autêntica. com recheio suave e consistente, envolto em chocolate meio amargo. 🍫🌱",
            short_description="Bombom de cupuaçu com chocolate meio amargo.",
            image= "assets/produtos/cupuacu-bg.png",
            price=5.50,
            fake=145
        )

@app.route('/')
def homepage():
    produtos = Produto.query.all()
    parceiros = Partner.query.all()
    print(parceiros[0].image)
    return render_template('homepage.html', produtos=produtos, produto1=PRODUTO1, produto2=PRODUTO2, parceiros=parceiros)

@app.route("/login", methods=["GET", "POST"])
def login():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        usuario = Usuarios.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.password, formLogin.password.data):
            login_user(usuario)
            return redirect(url_for("homepage"))
        
        formLogin.email.errors.append("Login inexistente ou senha incorreta.")
    return render_template("login.html", form=formLogin)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    formCriarConta = RegistrationForm()
    
    if formCriarConta.validate_on_submit():

        usuario_existente = Usuarios.query.filter(
            (Usuarios.email == formCriarConta.email.data) | 
            (Usuarios.username == formCriarConta.username.data)
        ).first()
        if usuario_existente:
            flash("Este email ou nome de usuário já está em uso. Tente outro.", "danger")
            return render_template("signup.html", form=formCriarConta)
        senha_hash = bcrypt.generate_password_hash(formCriarConta.password.data).decode('utf-8')
        usuario = Usuarios(
            username=formCriarConta.username.data,
            password=senha_hash,
            email=formCriarConta.email.data,
            zip_code=formCriarConta.zip_code.data,
            city=formCriarConta.city.data,
            state=formCriarConta.state.data,
            address=formCriarConta.address.data
        )
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("homepage"))
    
    print(formCriarConta.errors)
    return render_template("signup.html", form=formCriarConta)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/produto/<int:produto_id>')
def produto_detalhe(produto_id):
    produto = Produto.query.get_or_404(produto_id)
    form = DummyForm()
    return render_template("products.html", produto=produto, form=form)

@app.route('/contato', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        database.session.add(new_message)
        database.session.commit()
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.route('/produto/bombom/1')
def bombom1():
    produto = PRODUTO1
    imagens = [
        "assets/produtos/bombom.png",
        "assets/produtos/cupuacu-bg.png"
    ]
    form = DummyForm()
    return render_template("bombom.html", produto=produto, imagens=imagens, form=form)

@app.route('/produto/bombom/2')
def bombom2():
    produto = PRODUTO2
    imagens = [
        "assets/produtos/cupuacu-bg.png",
        "assets/produtos/bombom.png"
    ]
    form = DummyForm()
    return render_template("bombom.html", produto=produto, imagens=imagens, form=form)
        
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

from flask import session

def get_cart():
    return session.get('cart', {})

@app.route('/add_to_cart/<int:produto_id>', methods=['POST'])
def add_to_cart(produto_id):
    cart = get_cart()
    cart[str(produto_id)] = cart.get(str(produto_id), 0) + 1
    session['cart'] = cart
    return redirect(request.referrer or url_for('cart'))

@app.route('/remove_from_cart/<int:produto_id>', methods=['POST'])
def remove_from_cart(produto_id):
    cart = get_cart()
    if str(produto_id) in cart:
        cart[str(produto_id)] -= 1
        if cart[str(produto_id)] <= 0:
            del cart[str(produto_id)]
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart = get_cart()
    produtos = []
    total = 0
    for pid, qty in cart.items():
        produto = Produto.query.get(int(pid))
        if produto:
            produtos.append({'produto': produto, 'qty': qty, 'subtotal': produto.price * qty})
            total += produto.price * qty
    form = DummyForm()
    return render_template('cart.html', produtos=produtos, total=total, form=form)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = get_cart()
    produtos = []
    total = 0
    for pid, qty in cart.items():
        produto = Produto.query.get(int(pid))
        if produto:
            produtos.append({'produto': produto, 'qty': qty, 'subtotal': produto.price * qty})
            total += produto.price * qty
    if request.method == 'POST':
        session.pop('cart', None)
        flash('Pedido realizado com sucesso!', 'success')
        return redirect(url_for('homepage'))
    return render_template('checkout.html', produtos=produtos, total=total)