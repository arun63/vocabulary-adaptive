
from flask import request, jsonify
from flask_cors import CORS
from flask import Flask
import requests
import json
from utils import utils
import psycopg2


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

		try:
			data and data['player'] and data['word']
		except Exception as e:
			return jsonify({'status': 400, 'message': 'bad request'})
		else:
			pass

		if data and data['player'] and data['word']:
			player_rating = data['player']
			word_rating = data['word']

			# connecting to remote postgres DB
			# try:
			# 	conn = psycopg2.connect(
			# 		database=db['db'],
			# 		user=db['db_user'],
			# 		password=db['db_password'],
			# 		host = db['db_host'],
			# 		port = db['db_port']
			# 	)
			# except Exception as e:
			# 	print 'unable to connect to postgres - setting value of lambda to 1'
			# 	print e
			# else:
			# 	cursor = conn.cursor()
			# finally:
			# 	cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
			# 	print cursor.fetchall()
				


			# lamdba must be fetched from the database on every transaction
			# util = utils()
			# lam = util.calculate_lambda(player_rating, word_rating)
			# print lam

			resp = dict()
			# replace with the remote instance host
			if type(player_rating) and type(word_rating) == float or int:
				# call lambda word decay service
				try:
					response = requests.post('http://http://ec2-34-244-237-146.eu-west-1.compute.amazonaws.com:8084/decay/', json = { "elo_word": 0.85, "elo_player": 0.40, "time_taken": 12 })
				except Exception as e:
					return jsonify({'status': 500, 'message': 'unable tp connect to hard word service'})
				else:
					return jsonify(response.json())
					resp = jsonify(response.json())
					print resp

					threshold = (player_rating * lam)  + (word_rating * lam)
					if threshold >= 150:
						# call hard word
						try:
							response = requests.request("GET", host+'/word/hard')
						except Exception as e:
							return jsonify({'status': 500, 'message': 'unable tp connect to hard word service'})
						else:
							return jsonify(response.json())


					elif threshold < 150 and threshold > 100:
						# call medium word
						try:
							response = requests.request("GET" , host+'/word/medium')
						except Exception as e:
							return jsonify({'status': 500, 'message': 'unable to connect to medium word service'})
						else:
							return jsonify(response.json())


					elif threshold < 100 and threshold >= 0:
						# call easy word
						try:
							response = requests.request("GET" , host+'/word/easy')
						except Exception as e:
							return jsonify({'status': 500, 'message': 'unable to connect to easy word service'})
						else:
							return jsonify(response.json())
			else:
				return jsonify({'status':400, 'message': 'bad request'})



if __name__ == '__main__':
	try:
		json.load(open('config.json'))
	except Exception as e:
		print 'config.json not found'
	else:
		pass
	finally:
		app.run(host='0.0.0.0',port='8080')
	