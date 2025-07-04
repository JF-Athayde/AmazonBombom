from flask import *
from amazon import app, database, bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from amazon.form import *
from amazon.models import Usuarios, Produto, ContactMessage
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect, CSRFError

@app.route('/')
def homepage():
    produtos = Produto.query.all()
    return render_template('homepage.html', produtos=produtos)

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
    return render_template("products.html", produto=produto)

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

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))