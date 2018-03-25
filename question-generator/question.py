from flask import Flask
from flask import request, jsonify
import subprocess
import json
app = Flask(__name__)

@app.route('/question', methods=['GET', 'POST'])
def question():
	data = request.get_json()
	try:
		data and data['words']
	except Exception as e:
		return jsonify({'status':400})
	if data and data['words']:
		words_list = data['words']
		w1, w2 = words_list.split(",")
		#all_words = ' '.join("'" + str(x) + "'" for x in word_split)
		#print('list of words: ', all_words)
		response = subprocess.run(['wikitrivia', w1, w2], stdout= subprocess.PIPE).stdout.decode('utf-8')
				
		return response
	else:
		return jsonify({'status':401})


