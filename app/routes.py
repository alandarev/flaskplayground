from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {
            'username': 'Anthony',
    }
    more_random_data = {
            'favourite_day':    'Friday',
            'favourite_color':  'Pink',
    }
    return render_template('index.html', 
            title='Welcome', 
            user=user, 
            preferences=more_random_data)

