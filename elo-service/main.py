# import argparse
from flask import request, jsonify
from flask_cors import CORS
import sys
# Elo rating
sys.path.append('lib/Elo/')
from Elo import Elo


from flask import Flask
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET', 'POST'])
def return_base_route():
	return jsonify({'status': 200, 'message': 'base route'})



@app.route('/elo/', methods=['GET','POST'])
def return_elo_rating():
	if request.method == 'POST':
		data = request.get_json()
		# print data
		try:
			data and data['player'] and data['word'] and data['win']
		except Exception as e:
			return jsonify({'status': 400, 'message': 'bad request'})
		else:
			obj = dict()
			player_rating = data['player']
			word_rating = data['word']
			player_win = data['win']
			if type(player_rating) and type(word_rating) == float or int:
				rank = Elo(player_rating, word_rating, player_win)
				if player_win == 0:
					(rank1, rank2) = rank.elo()
					obj['word'] = rank1
					obj['player'] = rank2
					return jsonify(obj)
				elif player_win == 1:
					(rank1, rank2) = rank.elo()
					obj['player'] = rank1
					obj['word'] = rank2
					return jsonify(obj)

			else:
				return jsonify({'status':400, 'message': 'bad request'})
	else:
		return jsonify({'status':400, 'message': 'bad request'})


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8082)
	# app = create_app(config.DATABASE_URI, debug=True)
