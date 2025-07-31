from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, FileField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import Regexp

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=1000)])
    submit = SubmitField('Send')

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="O nome é obrigatório.")])
    description = TextAreaField('Description', validators=[DataRequired(message="A descrição é obrigatória.")])
    image = FileField('Product Image', validators=[
        FileRequired(message="A imagem é obrigatória."),
        FileAllowed(['jpg', 'jpeg', 'png', 'webp'], 'Apenas arquivos de imagem são permitidos (jpg, jpeg, png, webp).')
    ])
    submit = SubmitField('Save')

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Fazer login")

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(message="O nome de usuário é obrigatório."),
            Length(min=2, max=100, message="O nome de usuário deve ter entre 2 e 100 caracteres.")
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="O email é obrigatório."),
            Email(message="Informe um endereço de email válido.")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message="A senha é obrigatória."),
            Length(min=6, message="A senha deve ter pelo menos 6 caracteres.")
        ]
    )

    zip_code = StringField(
        'ZIP Code',
        validators=[
            DataRequired(message="O CEP é obrigatório."),
            Regexp(r'^\d{5}-\d{3}$', message="Digite o CEP no formato 00000-000.")
        ]
    )

    city = StringField(
        'City',
        validators=[
            DataRequired(message="A cidade é obrigatória."),
            Length(max=100, message="A cidade deve ter no máximo 100 caracteres.")
        ]
    )
    state = SelectField(
        'State',
        choices=[
            ('', 'Selecione um estado'),
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        ],
        validators=[DataRequired(message="O estado é obrigatório.")]
    )
    address = StringField(
        'Address',
        validators=[
            DataRequired(message="O endereço é obrigatório."),
            Length(max=255, message="O endereço deve ter no máximo 255 caracteres.")
        ]
    )
    complement = StringField(
        'Complement',
        validators=[
            Length(max=255, message="O complemento deve ter no máximo 255 caracteres.")
        ]
    )
    submit = SubmitField('Register')

class DummyForm(FlaskForm):
    pass
