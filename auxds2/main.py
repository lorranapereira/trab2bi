from flask import Flask, request, url_for, redirect, render_template, session
from flask_wtf import Form
from wtforms import TextField,BooleanField, StringField, PasswordField, validators
from form import RegistrationForm
app = Flask(__name__)

@app.route('/')
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

class ContactForm(Form):
    name = TextField("Name Of Student")
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
def main():
    app.secret_key = 'string'
    app.env = 'development'
    app.run(debug=True, port=4000)
if __name__ == "__main__":
    main()
# nome
# admin
# salario
# filhos
# sexo
# biografia
# senha
# login
