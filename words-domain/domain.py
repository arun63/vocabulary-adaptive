from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from mapper import DomainWordMapper
from datapreprocessing import DataPreprocessing


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/domain', methods=['GET','POST'])
def domain():

    if request.method == 'GET':
        filepath = json.load(open('filepath.json'))
        domainmap = DomainWordMapper(filepath)
        resp = domainmap.getDomains()
        return json.dumps(resp, sort_keys=True)
    else:
        return jsonify({'status':400})

@app.route('/paragraph', methods=['GET','POST'])
def paragraph():
    data = request.get_json()
    try:
        data and data['para']
    except Exception as e:
        return jsonify({'status':400})

    if data and data['para']:
        paragraph = json.load(open('paragraph.json'))
        sentence = paragraph[data['para']]
        data = DataPreprocessing(sentence)
        data_no_sw = data.remove_stop_words()
        return json.dumps(data_no_sw, sort_keys=True)
    else:
        return jsonify({'status':400})

@app.route('/paradomain', methods=['GET','POST'])
def getDomainFromParagraph():
    data = request.get_json()
    try:
        data and data['para']
        filepath = json.load(open('filepath.json'))
    except Exception as e:
        return jsonify({'status':400})

    if data and data['para']:
        paragraph = json.load(open('paragraph.json'))
        sentence = paragraph[data['para']]
        data = DataPreprocessing(sentence)
        data_no_sw = data.remove_stop_words()
        domainmap = DomainWordMapper(filepath)
        resp = domainmap.getDomainFromPara(data_no_sw)
        return json.dumps(resp, sort_keys=True)
    else:
        return jsonify({'status':400})
