from flask import render_template, request, redirect, url_for
from app import app
import requests

@app.route('/')
def home():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote = response.json()
        return render_template('quote.html', quote=quote)
    else:
        return "Failed to retrieve quote", 500
