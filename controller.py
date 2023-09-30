from flask import Flask
from flask_cors import CORS
import subprocess
import os
import psutil
import jsonify
import re


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    
    return 'hello world'

@app.route("/get-top-data")
def get_top_data():
    
    process = os.popen('top -b -n 1')
    rawTop = process.read()
    process.close()
    
    rawTopParts = rawTop.split('\n\n')
    rawTopHeader = rawTopParts[0]
    rawTopTable = rawTopParts[1]
    
    rawTopHeaderArray = re.split('\n', rawTopHeader)
    rawTopTableArray = re.split('\n', rawTopTable)
    
    topHeaderResult = [val.strip() if index != len(rawTopHeaderArray)-1 else val.split('\n\n')[0].strip() for index, val in enumerate(rawTopHeaderArray)]
    topTableResult = [val.strip() for val in rawTopTableArray]
    
    return {'topHeader': topHeaderResult, 'topTable': topTableResult }

app.run(host="192.168.0.104", port=5000, debug=True)
