from nltk.corpus import wordnet as wn
from textblob import TextBlob

import re
import wikipedia

class Wikisentences:
    def __init__(self, title):
        self.page = wikipedia.page(title)
        self.summary = TextBlob(self.page.summary)

    def generate_sentences(self):
        sentences = self.summary.sentences
        del sentences[0]

        all_sentences = []
        for sentence in sentences:
            all_frame_sent = self.evaluate_sentence(sentence)
            if all_frame_sent:
                all_sentences.append(all_frame_sent)

        return all_sentences

    def get_similar_words(self, word):
        synsets = wn.synsets(word, pos='n')
        if len(synsets) == 0:
            return []
        else:
            synset = synsets[0]

        hypernym = synset.hypernyms()[0]
        hyponyms = hypernym.hyponyms()

        similar_words = []
        for hyponym in hyponyms:
            similar_word = hyponym.lemmas()[0].name().replace('_', ' ')
            
            if similar_word != word:
                similar_words.append(similar_word)

            if len(similar_words) == 8:
                break

        return similar_words

    def evaluate_sentence(self, sentence):
        if sentence.tags[0][1] == 'RB' or len(sentence.words) < 6:
            return None

        tag_map = {word.lower(): tag for word, tag in sentence.tags}

        replace_nouns = []
        for word, tag in sentence.tags:
            if tag == 'NN' and word not in self.page.title:
                for phrase in sentence.noun_phrases:
                    if phrase[0] == '\'':
                        break

                    if word in phrase:
                        [replace_nouns.append(phrase_word) for phrase_word in phrase.split()[-2:]]
                        break

                if len(replace_nouns) == 0:
                    replace_nouns.append(word)
                break
        
        if len(replace_nouns) == 0:
            return None

        all_frame_sentences = {
            'title': self.page.title,
            'url': self.page.url,
            'answer': ' '.join(replace_nouns)
        }

        if len(replace_nouns) == 1:
            all_frame_sentences['similar_words'] = self.get_similar_words(replace_nouns[0])
        else:
            all_frame_sentences['similar_words'] = []

        replace_phrase = ' '.join(replace_nouns)
        blanks_phrase = ('__________ ' * len(replace_nouns)).strip()

        expression = re.compile(re.escape(replace_phrase), re.IGNORECASE)
        sentence = expression.sub(blanks_phrase, str(sentence), count=1)

        all_frame_sentences['question'] = sentence
        return all_frame_sentences
