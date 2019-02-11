from app import app
from app.query import query
from flask import render_template,request,jsonify,Response
import pandas as pd

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():

    device_list = ['all_devices']
    country_list = ['all_countries']

    display_table = query(country_list,device_list)

    return render_template('index.html',tables=[display_table.to_html(
    classes="mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp")],
    titles=display_table.columns.values)

@app.route('/submit', methods=['GET', 'POST'])
def display_table():

    if request.method == 'POST':
        device_list = request.form.getlist('device')
        country_list = request.form.getlist('country')

    display_table = query(country_list,device_list)

    return render_template('index.html',tables=[display_table.to_html(
    classes="mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp",
    justify="center")],titles=display_table.columns.values)
