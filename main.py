from flask import Flask, render_template, url_for, flash, request, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '66s449b6y970168c9397ae9ij5c13d55'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/users")
def users():
    users = User.query.all()
    return render_template('users.html', title='users', users=users)

@app.route('/users/new', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        flash('User was successfully added')
        return redirect(url_for('users'))
    return render_template('add_user.html')

@app.route('/users/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        db.session.commit()
        flash('User was successfully updated')
        return redirect(url_for('users'))
    return render_template('edit_user.html', user=user)


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User was successfully deleted')
    return redirect(url_for('users'))

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