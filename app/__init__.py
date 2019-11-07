import os

from flask import Flask

template_folder = os.path.dirname(os.path.realpath(__file__)) + '/templates/'
static_folder = os.path.dirname(os.path.realpath(__file__)) + '/static/'

app = Flask('playground', 
        template_folder=template_folder,
        static_folder=static_folder)

app.config['EXPLAIN_TEMPLATE_LOADING'] = True

from app import routes


