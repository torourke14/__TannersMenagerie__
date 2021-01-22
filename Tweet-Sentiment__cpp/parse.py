"""Functions for reading data from the sentiment dictionary and tweet files."""

import os
import re
import string
import codecs
from datetime import datetime
from tweet import Tweet
from geo import GeoPosition

DATA_PATH = 'data' + os.sep

def load_sentiments(file_name="data"+os.sep+"sentiments.csv"):
    """Read the sentiment file and return a dictionary containing the sentiment
    score of each word, a value from -1 to +1.
    """
    sentiments = {}
    for line in codecs.open(file_name, encoding='utf8'):
        word, score = line.split(',')
        sentiments[word] = float(score.strip())
    return sentiments

def file_name_for_term(term):
    """Return a valid filename that corresponds to an arbitrary term string."""
    valid_characters = '-_' + string.ascii_letters + string.digits
    no_space = term.replace(' ', '_')
    return ''.join(c for c in no_space if c in valid_characters) + '.txt'

'''
def generate_filtered_file(unfiltered_name, term):
    """Return the path to a file containing tweets that match term, generating
    that file if necessary.
    """
    filtered_path = DATA_PATH + file_name_for_term(term)
    if not os.path.exists(filtered_path):
        print('Generating filtered tweets file for %s.' % term)
        r = re.compile('\W' + term + '\W', flags=re.IGNORECASE)
        out = codecs.open(filtered_path, mode='w', encoding='utf8')
        unfiltered = codecs.open(DATA_PATH + unfiltered_name, encoding='utf8')
        matches = [l for l in unfiltered if term in l.lower()]
        for line in matches:
            if r.search(line):
                out.write(line)
        out.close()
    return filtered_path

def load_tweets(term='my job', file_name='all_tweets.txt'):
    """Return the list of tweets in file_name that contain term."""
    term = term.lower()
    filtered_path = generate_filtered_file(file_name, term)
    tweets = []
    for line in codecs.open(filtered_path, encoding='utf8'):
        if len(line.strip().split("\t")) >=4:
            loc, _, time_text, text = line.strip().split("\t")
            time = datetime.strptime(time_text, '%Y-%m-%d %H:%M:%S')
            lat, lon = eval(loc)
            tweet = Tweet(text.lower(), time, GeoPosition(lat,lon) )
            tweets.append(tweet)
    return tweets
'''