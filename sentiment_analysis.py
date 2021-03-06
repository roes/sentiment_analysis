import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.metrics import BigramAssocMeasures

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

  def classify(self, tweet):
    return self.classifier.classify(self.tweet_features(tweet))

def get_all_features( training_set, feature_n = 1000 ):
  label_word_freq_dist = ConditionalFreqDist()
  word_freq_dist = FreqDist()
  for (words, sentiment) in training_set:
    for word in words:
      if len(word) > 2:
        word_freq_dist.inc( word.lower() )
        label_word_freq_dist[ sentiment ].inc( word.lower() )
  
  pos_word_n = label_word_freq_dist[1].N()
  neg_word_n = label_word_freq_dist[-1].N()
  total_word_n = pos_word_n + neg_word_n
  word_scores = {}
  for word, freq in word_freq_dist.iteritems():
    word_scores[ word ] = BigramAssocMeasures.chi_sq( label_word_freq_dist[ 1 ][ word ], 
      (freq, pos_word_n), total_word_n )

  ext_words = sorted( word_scores.iteritems(), key = lambda( w, s ) : s, reverse 
    = True )[ : feature_n ]

  feature_words = [ w for w, s in ext_words ];

  return feature_words
