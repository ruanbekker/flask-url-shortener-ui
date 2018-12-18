from flask import Flask, render_template, request, url_for
import os
import sys
import socket
import requests
import json
import logging

tiny_api_url = os.getenv('TINY_API_URL', None)
tiny_api_key = os.getenv('X_API_KEY', None)
app_title = os.getenv('APP_TITLE', 'My URL Shortener')

if tiny_api_url == None or tiny_api_key == None:
    logging.error("Failed to load configuration")
    sys.exit(4)

headers = {'Content-Type': 'application/json', 'X-Api-Key': tiny_api_key}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', app_title=app_title)

@app.route('/shortened', methods=['GET', 'POST'])
def search_request():
    user_url = request.form["input"]
    response = requests.post(
        tiny_api_url,
        headers=headers,
        data=json.dumps({
            "long_url": user_url
            }
        )
    )
    return render_template('results.html', app_title=app_title, res=response.content )

if __name__ == '__main__':
    app.run(passthrough_errors=False)
