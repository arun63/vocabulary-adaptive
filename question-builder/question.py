from wikisentences import Wikisentences
from flask import Flask
from flask import request, jsonify
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
		questions = []
		for article in words_list.split(","):
			article = Wikisentences(title=article)
			questions = questions + article.generate_sentences()
		#print(questions)
		return json.dumps(questions, sort_keys=True, indent =4)
	else:
		return jsonify({'status':401})

