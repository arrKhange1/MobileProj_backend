from flask import Flask
from flask_cors import CORS
import os
import re


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'hello world'
    
def getSerializedTopCols(topTable):
    stringCols = topTable[0]
    return stringCols.split()

def mapRowToSeparateCols(row):
    splittedRow = row.split()
    return splittedRow[:11] + [" ".join(splittedRow[11:])]

def mapSeparateColsToObject(rowWithSeparateCols, cols):
    return { cols[index]:rowCol for index, rowCol in enumerate(rowWithSeparateCols) } 

def getSerializedTopBody(topTable, topTableCols):
    topBody = topTable[1:]
    bodyWithSeparateCols = list(map(mapRowToSeparateCols, topBody))
    serializedTopBody = list(map(lambda row: mapSeparateColsToObject(row, topTableCols), bodyWithSeparateCols))
    return serializedTopBody
    

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
    
    topTableCols = getSerializedTopCols(topTableResult)
    
    return {'topData': topHeaderResult, 'cols': topTableCols, 'body': getSerializedTopBody(topTableResult, topTableCols) }
    

app.run(host="178.253.42.169", port=5000, debug=True)
