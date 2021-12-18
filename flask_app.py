
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/blog')
def blog():
    return render_template('blog.html', title='Blog')
