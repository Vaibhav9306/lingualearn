from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def das():
    return render_template('das.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Process signup
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