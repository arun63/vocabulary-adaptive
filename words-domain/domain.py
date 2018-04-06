from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from mapper import DomainWordMapper


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/domain', methods=['GET','POST'])
def orchestrate():

    if request.method == 'GET':
        filepath = json.load(open('filepath.json'))
        domainmap = DomainWordMapper(filepath)
        resp = domainmap.getDomains()
        return json.dumps(resp, sort_keys=True)
    else:
        return jsonify({'status':400})
