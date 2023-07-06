from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '66s449b6y970168c9397ae9ij5c13d55'

posts = [
    {
        'Author':'Kupelekale',
        'Title': 'The Wizard Grauchi',
        'Content': 'Lopsum Gypsum'
    },
    {
        'Author':'Mfalme mkuu',
        'Title': 'Sham sham za kishada',
        'Content': 'Lopsum Gypsum ipsam'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/users")
def users():
    return render_template('users.html', title='users')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}')
    return render_template('register.html', title='register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8080)