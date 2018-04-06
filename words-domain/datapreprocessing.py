import os
import sys
import nltk
import re
from stop_words import get_stop_words
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer


class DataPreprocessing:

	def __init__(self, content):
		self.content = content

	def remove_stop_words(self):
		# extending the stop words - combination of NLTK and stop_words
		stop_words = list(get_stop_words('en'))
		nltk_words = list(stopwords.words('english'))
		stop_words.extend(nltk_words)

		tokens = []
		# check if the input is word list
		if isinstance(self.content, str):
			# iterate through the sentence and remove stop words
			sentence = self.content.lower()
			sentence = self.remove_number(sentence)
			tokenizer = RegexpTokenizer(r'\w+')
			tokens = tokenizer.tokenize(sentence)

		elif isinstance(self.content, list):
			print ('content must be a string')
			exit(0)
		tokens = list(set(tokens))
		# removing all stop words from the content
		without_stopwords = [w for w in tokens if not w in stop_words]

		return without_stopwords

	def remove_number(self, sentence):
		return re.sub("\d+", " ", sentence)

	def tokenize(self, word_list):
		tokenized_words = []
		for each_word in word_list:
			tokenized_words = (word_tokenize(word_list))
		return tokenized_words

	def stemming(self, word_list):
		ps = SnowballStemmer("english")
		stem_list = set()
		for word in word_list:
			stem_list.add(ps.stem(word))
		return stem_list

#def main():
	#analysis = DataPreprocessing("Wikipedia ( ( listen),  ( listen) WIK-ih-PEE-dee-ə) is a multilingual, web-based, free-content encyclopedia project supported by the Wikimedia Foundation and based on a model of openly editable content. Wikipedia is the largest and most popular general reference work on the Internet, and is named as one of the most popular websites. The project is owned by the Wikimedia Foundation, a non-profit which operates on whatever monies it receives from its  annual fund drives.Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger. Sanger coined its name, a portmanteau of wiki and encyclopedia. There was only the English-language version initially, but similar versions in other languages quickly developed, which differ in content and in editing practices. With 5,600,645 articles, the English Wikipedia is the largest of the more than 290 Wikipedia encyclopedias. \
	#Overall, Wikipedia comprises more than 40 million articles in 299 different languages and, as of February 2014, it had 18 billion page views and nearly 500 million unique visitors each month.As of March 2017, Wikipedia has about 40,000 high-quality articles, known as Featured Articles and Good Articles, that cover vital topics. In 2005, Nature published a peer review comparing 42 science articles from Encyclopædia Britannica and Wikipedia, and found that Wikipedia's level of accuracy approached that of Encyclopædia Britannica. Time magazine stated that the remarkably open-door policy of allowing anyone to edit had made Wikipedia the biggest and possibly the best encyclopedia in the world and it was testament to the vision of Jimmy Wales.Wikipedia has been criticized for allegedly exhibiting systemic bias, presenting a mixture of truths, half truths, and some falsehoods, \
	#and, in controversial topics, being subject to manipulation and spin.")
	#post_stopwords = analysis.remove_stop_words()
	#print(post_stopwords)

#if __name__ == '__main__':
# 	main()
