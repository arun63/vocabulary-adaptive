
from flask import request, jsonify
from flask_cors import CORS
from flask import Flask
import requests
import json
from utils import utils
# import psycopg2

state = list()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/orchestra', methods=['GET','POST'])
def orchestrate():
	# config file
	db = json.load(open('config.json'))
	host = db['host']
	port = db['port']

	# depending on the user params - orchestrate the next service to be called
	if request.method == 'POST':
		obj = dict();
		data = request.get_json()
		counter = 0

		try:
			data and data['word_rating'] and data['player_rating'] and data['time_taken'] and data['won']
		except Exception as e:
			return jsonify({'status': 400, 'message': 'bad request'})
		else:
			pass

		if data and data['word_rating'] and data['player_rating'] and data['time_taken'] and data['won']:
			word_rating = data['word_rating']
			player_rating = data['player_rating']
			time = data['time_taken']
			won = data['won']

			# print word_rating
			# print player_rating
			# print time
			# print won

			# Elo

			try:
				url = "http://ec2-34-244-237-146.eu-west-1.compute.amazonaws.com:8082/elo/"
				response = requests.post(url, json={ "player": player_rating, "word": word_rating, "win": won})
			except Exception as e:
				return jsonify({ 'status': 500, 'message': 'internal server error'})
			else:
				resp = response.json()
				new_player_rating = resp['player']
				new_word_rating = resp['word']

				# send the new player and word rating to decay along with time taken
				try:
					url = "http://ec2-34-244-237-146.eu-west-1.compute.amazonaws.com:8084/decay/"
					response = requests.post(url, json={ "elo_player": new_player_rating, "elo_word": new_word_rating, "time_taken": time})
				except Exception as e:
					return jsonify({ 'status': 500, 'message': 'internal server error'})
				else:
					# success
					word_list = { 'laconic': 5, 'intrepid': 4.9, 'reticent': 4.8, 'terse': 4.7, 'pithy': 4.6, 'churlish': 4.5, 'furtive': 4.5,  'polyglot': 4.4, 'veracious': 4.3, 'mercurial': 4.2, 'amenable': 4.1, 'insipid': 4.0, 'pragmatic': 3.9, 'arduous': 3.8, 'profligate': 3.7, 'prosaic': 3.6, 'obsequious': 3.5, 'capricious': 3.4, 'fortuitous':3.3, 'orthodox': 3.2, 'pellucid': 3.1, 'abash': 2.9, 'abase': 2.8};
					# pull words from database - rank them in order
					
					resp_ = response.json()
					lam = resp_['decay']
					threshold = (new_player_rating  + new_word_rating) * lam
					
					print 'Threshold : ', threshold

					# try:
					# 	url = "http://ec2-34-251-196-31.eu-west-1.compute.amazonaws.com:8090/question"
					# 	response = requests.post(url, json={ "words": str(key) })
					# except Exception as e:
					# 	return jsonify({'status': 500, 'message': 'question service not callable'})
					# else:
					# 	resp = response.json()
					# 	return jsonify({'status': 200, 'word': key})
					

					if threshold >= 0 and threshold <= 1.5:
						print 'hard'
						# call hard word
						val = min(word_list.values(), key=lambda x:abs (x - threshold))
						print val
						for key, value in word_list.iteritems():
							if val == value:
								print key
								state.append(key)
								return jsonify({'status': 200, 'message': key})
								

					elif threshold > 1.5 and threshold <= 3.2:
						print 'medium'
						# call medium word
						val = min(word_list.values(), key=lambda x:abs (x - threshold))
						print val
						for key, value in word_list.iteritems():
							if val == value:
								print key
								state.append(key)
								return jsonify({'status': 200, 'message': key})


					elif threshold > 3.2:
						print 'easy'
						val = min(word_list.values(), key=lambda x:abs (x - threshold))
						print val
						for key, value in word_list.iteritems():
							if val == value:
								print key
								state.append(key)
								return jsonify({'status': 500, 'message': key})


	elif request.method == "GET":
		return jsonify({'status': 400, 'message': 'method not allowed'})



if __name__ == '__main__':
	try:
		json.load(open('config.json'))
	except Exception as e:
		print 'config.json not found'
	else:
		pass
	finally:
		app.run(host='0.0.0.0',port=8080)
	