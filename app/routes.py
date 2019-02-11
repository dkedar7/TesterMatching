# Import required modules
from app import app
from app.query import query
from flask import render_template,request,jsonify,Response
import pandas as pd

# Index view
@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    '''
    Opening page. Displays 'index.html' files with the entire datatable.
    '''

    device_list = ['all_devices']
    country_list = ['all_countries']

    # Get the queries dataframe
    display_table = query(country_list,device_list)

    return render_template('index.html',tables=[display_table.to_html(
    classes="mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp")],
    titles=display_table.columns.values)

# Submit view
@app.route('/submit', methods=['GET', 'POST'])
def display_table():
    '''
    Display after querying.
    '''

    # After the form is submitted, get the values of devices and countries
    # checkboxes.
    if request.method == 'POST':
        device_list = request.form.getlist('device')
        country_list = request.form.getlist('country')

    # Get the queries dataframe
    display_table = query(country_list,device_list)

    return render_template('index.html',tables=[display_table.to_html(
    classes="mdl-data-table mdl-js-data-table mdl-data-table mdl-shadow--2dp",
    justify="center")],titles=display_table.columns.values)
