from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///language_learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    xp = db.Column(db.Integer, default=0)
    streak = db.Column(db.Integer, default=0)
    language = db.Column(db.String(20))

with app.app_context():
    db.create_all()

languages = ['Spanish', 'French', 'German', 'Italian', 'Japanese', 'Chinese']
lessons = {
    'Spanish': ['Greetings', 'Numbers', 'Colors', 'Family', 'Food'],
    'French': ['Bonjour!', 'Les Chiffres', 'Les Couleurs', 'La Famille', 'La Nourriture'],
    'German': ['Begrüßungen', 'Zahlen', 'Farben', 'Familie', 'Essen'],
    'Italian': ['Saluti', 'Numeri', 'Colori', 'Famiglia', 'Cibo'],
    'Japanese': ['挨拶', '数字', '色', '家族', '食べ物'],
    'Chinese': ['问候', '数字', '颜色', '家庭', '食物'],
}

@app.route('/')
def das():
    return render_template('das.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Logged in successfully', 'success')
            return redirect(url_for('index'))
        flash('Invalid username or password', 'danger')
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'danger')
            return redirect(url_for('signup'))
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        flash('Account created successfully', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/lesson')
def lesson():
    return render_template('lesson.html')

@app.route('/select_language')
def select_language():
    return render_template('select_language.html')

@app.route('/speaking')
def speaking():
    return render_template('speaking.html')

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
