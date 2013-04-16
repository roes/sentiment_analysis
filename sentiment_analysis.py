import nltk
from nltk.classify import NaiveBayesClassifier

class SentimentAnalyser:

  def __init__(self, tweets):
    self.features = get_all_features(tweets)
    training_set = nltk.classify.util.apply_features(
        self.tweet_features, tweets)
    self.classifier = NaiveBayesClassifier.train(training_set)

  def tweet_features(self, tweet):
    words = set(tweet)
    features = {}
    for feature in self.features:
      features['contains(%s)' % feature] = (feature in words)
    return features

  def test_accuracy(self, tweets):
    test_set = nltk.classify.util.apply_features(
        self.tweet_features, tweets)
    return nltk.classify.accuracy(self.classifier, test_set)

def get_all_features(training_set):
  wordlist = []
  for (words, sentiment) in training_set:
    wordlist.extend(words)
  wordlist = nltk.FreqDist(wordlist)
  return wordlist.keys()
