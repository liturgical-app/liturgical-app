"""
A simple app to display the current liturgical colour of the Church of England
"""
from datetime import date, datetime
import json
import os
import requests
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

url = os.getenv('LITURGICAL_API_URL', default='https://liturgical-api.gazeley.uk')

@app.route('/', methods =["GET", "POST"])
def main():
    """
    Return the liturgical colour
    """
    # Get date from datepicker, if set
    f_date = request.form.get("date") or date.today()

    # Get info from API
    # Append the date to the API endpoint
    path = f"{url}/{f_date}"

    # A GET request to the API
    response = requests.get(path, timeout=10)

    # Get response from API
    response_json = str(response.json())

    # Convert single quotes to double quotes for json spec
    response_json = response_json.replace("\'", "\"")

    # Unserialize json into a Python object
    dayinfo = json.loads(response_json)

    # Convert date string to date object
    shortdate = datetime.strptime(dayinfo['date'], '%Y-%m-%d')
    longdate = shortdate.strftime("%A, %-d %B %Y")

    return render_template('template.html', dayinfo=dayinfo, longdate=longdate, shortdate=shortdate)

@app.route('/manifest.json')
def serve_manifest():
    """
    Return the PWA manifest.json
    """
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/sw.js')
def serve_sw():
    """
    Return the service worker
    """
    return send_file('sw.js', mimetype='application/javascript')
