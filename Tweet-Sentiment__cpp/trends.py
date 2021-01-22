import sys
from state import load_states
from country import Country
from parse import load_sentiments
from colors import get_sentiment_color

class SentimentAnalysis:
    def __init__(self):
        self.sentiments = load_sentiments()
        self.states = load_states()
    def showCountry(self):
        self.usa = Country(self.states, 1200)
    #finish


if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        print query
    else:
        print "error"

    sa = SentimentAnalysis()
    sa.showCountry()

    #finish