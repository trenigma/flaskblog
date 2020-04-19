# home page route
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tree'}
    posts = [
        {
            'author': {'username': 'Onyx'},
            'body': 'Beautiful day in Seattle!'
        },
        {
            'author': {'username': 'Chanta'},
            'body': 'Star Wars was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)