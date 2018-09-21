from flask import request, Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm as Form
from wtforms.validators import Required, NumberRange
from wtforms import IntegerField, StringField, SubmitField
from diceware import handle_options
from diceware import get_passphrase
from random import choice
from string import ascii_letters, digits, punctuation

char_set = ascii_letters + digits + punctuation
def gen_word(length=12): return ''.join(choice(char_set) for _ in range(length))
def gen_phrase(length=5): return get_passphrase(handle_options(["-n",str(length)]))

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = gen_word(8)

class PasswordForm(Form):
    length = IntegerField('Number of Symbols?', validators=[Required(), NumberRange(min=1, max=30, message="Should be between 1 and 30")])
    submit = SubmitField('Submit')

class PassphraseForm(Form):
    length = IntegerField('Number of Symbols?', validators=[Required(), NumberRange(min=1, max=12, message="Should be between 1 and 12")])
    submit = SubmitField('Submit')

@app.route('/')
def index():
        return render_template('nav.html')

@app.route('/password', methods=('GET', 'POST'))
def password():
        form = PasswordForm()
        length = None
        if form.validate_on_submit():
                length = form.length.data
                return render_template('pwgen.html', password=gen_word(length), form=form)
        else:
                return render_template('pwgen.html', password=gen_word(), form=form)

@app.route('/passphrase', methods=('GET', 'POST'))
def passphrase():
        form = PassphraseForm()
        length = None
        if form.validate_on_submit():
                length = form.length.data
                return render_template('ppgen.html', passphrase=gen_phrase(length), form=form)
        else:
                return render_template('ppgen.html', passphrase=gen_phrase(), form=form)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=True)
