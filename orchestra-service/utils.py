import numpy

class utils:
	"""docstring for utils"""
	def __init__(self):
		pass

	def decayFunction(lamb,word_elo_rating,confidence_user,user_actual_time,threshold_time_for_the_word):

		return numpy.exp(-lamb*(word_elo_rating - confidence_user)/(user_actual_time - threshold_time_for_the_word))

	def calculate_decay_value(self, word_elo_rating, confidence_user, user_actual_time, threshold_time_for_the_word):
		'''
		Decay_Function(player_rating, word_rating) = lambda
		'''

		lamb = 1
		decay_val = decayFunction(lamb, word_elo_rating, confidence_user, user_actual_time, threshold_time_for_the_word)
		return decay_val

