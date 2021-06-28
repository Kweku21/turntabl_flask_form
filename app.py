from flask import Flask, render_template, redirect, flash, request
from flask.helpers import url_for
from forms import RegisterForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/')
@app.route('/home')
def home():
    return 'Hello World!'

@app.route('/login')
def login():

    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        # flash("message", "da")
        return redirect(url_for('login'))
        
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
