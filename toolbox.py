from flask import request, Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm as Form
from wtforms.validators import Required, NumberRange
from wtforms import IntegerField, StringField, SubmitField
from diceware import handle_options, get_passphrase
from random import choice
from string import ascii_letters, digits, punctuation
from psutil import disk_usage, disk_partitions, net_connections, process_iter

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
                return render_template('word.html', password=gen_word(length), form=form)
        else:
                return render_template('word.html', password=gen_word(), form=form)

@app.route('/passphrase', methods=('GET', 'POST'))
def passphrase():
        form = PassphraseForm()
        length = None
        if form.validate_on_submit():
                length = form.length.data
                return render_template('phrase.html', passphrase=gen_phrase(length), form=form)
        else:
                return render_template('phrase.html', passphrase=gen_phrase(), form=form)
            
@app.route('/disk', methods=['GET', 'POST'])
def disk():
        usage=[]
        for l in disk_partitions():
                try:
                        usage.append((l.device,disk_usage(l.device).percent))
                except:
                        pass
        return render_template('disk.html',usage=list(usage))
    
@app.route('/network', methods=['GET', 'POST'])
def network():
        cs=filter(lambda x: x.status == 'ESTABLISHED' and x.raddr[0] != '127.0.0.1',net_connections())
        out=[]
        for c in cs:
                for p in process_iter():
                        if p.pid == c.pid:
                                 out.append('{}({}) port {} > {}:{}'.format(p.name(), c.pid, c.laddr[1], c.raddr[0], c.raddr[1]))          
        return render_template('network.html', out=out)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80, debug=True)
