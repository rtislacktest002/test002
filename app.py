#!flask/bin/python
from flask import Flask, request, make_response
import requests
import os
import json

app = Flask(__name__)

slack_api_dialog_url = 'https://slack.com/api/dialog.open'

bot_token = os.environ['SBOT_TOKEN']

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run()
