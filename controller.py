from flask import Flask
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'hello world'

@app.route("/get-top-data")
def get_top_data():

    result = []
    Data = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
    a = str(Data)
    try:
        for i in range(len(a)):
            result.append(a.split("\\r\\r\\n")[i])
    except IndexError as e:
        print("All Done")

    return {'name': result}