
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

			# Elo
			try:
				url = "http://localhost:8082/elo/"
				response = requests.request("POST", url, data=jsonify({ "player": player_rating, "word": word_rating, "win": won}))
			except Exception as e:
				return jsonify({ 'status': 500, 'message': 'internal server error'})
			else:
				print response.json()
			finally:
				pass

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
			if type(player_rating) and type(word_rating) and type(time) == float or int:
				# call lambda word decay service
				try:
					url = "http://localhost:8084/decay/"
					payload = { "elo_word": word_rating, "elo_player": player_rating, "time_taken": time }
					headers = { 'content-type': "application/json", 'cache-control': "no-cache"}
					response = requests.request("POST", url, data=jsonify(payload), headers=jsonify(headers))
				except Exception as e:
					return jsonify({'status': 500, 'message': 'unable to connect to decay service'})
				else:
					resp = response.json()
					lam = resp['decay']
					print lam
					return response.json()

					threshold = (player_rating * lam)  + (word_rating * lam)
					# if threshold >= 150:
					# 	# call hard word
					# 	try:
					# 		response = requests.request("GET", host+'/word/hard')
					# 	except Exception as e:
					# 		return jsonify({'status': 500, 'message': 'unable tp connect to hard word service'})
					# 	else:
					# 		return jsonify(response.json())


					# elif threshold < 150 and threshold > 100:
					# 	# call medium word
					# 	try:
					# 		response = requests.request("GET" , host+'/word/medium')
					# 	except Exception as e:
					# 		return jsonify({'status': 500, 'message': 'unable to connect to medium word service'})
					# 	else:
					# 		return jsonify(response.json())


					# elif threshold < 100 and threshold >= 0:
					# 	# call easy word
					# 	try:
					# 		response = requests.request("GET" , host+'/word/easy')
					# 	except Exception as e:
					# 		return jsonify({'status': 500, 'message': 'unable to connect to easy word service'})
					# 	else:
					# 		return jsonify(response.json())
			else:
				return jsonify({'status':400, 'message': 'bad request'})

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
		app.run(host='0.0.0.0',port='8080')
	