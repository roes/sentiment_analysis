#!/usr/bin/env python

import argparse

happy_emot = [":)", ":-)", "=)", ":D", "=D"]
sad_emot = [":(", ":-(", "=("]

# Reads a file of tweets and removes unwanted parts.

def read_file(file_name):
  data = []
  f = open(file_name, 'r')
  line = f.readline()
  while line != '':
    if accept_tweet(line):
      print "accepted : " + line
      data.append(line)
    line = f.readline()
  f.close()
  for tweet in data:
    process_words(tweet)
  #print data
  return data

# Changes and removes unwanted words in the tweet.
# Should look for repeated sequences of characters, 
# maybe emoticons, at-signs etc.
def process_words(tweet):
  data = tweet.split()
  for word in data:
    #Check for unwanted words..
    #TODO
    print word
  return

# Determines whether the tweet should be in the training set.
# Checks for retweets and emoticons of both types (happy/sad).

def accept_tweet(tweet):
  happy = False
  sad = False
  data = ([e.lower() for e in tweet.split()])
  for word in data:
    if word == "rt":
      print "retweet! : " + word
      return False
    elif word in happy_emot:
      happy = True
      print "happy! : " + word
    elif word in sad_emot:
      sad = True
      print "sad! : " + word 
  if happy and sad:
    print "happy and sad! : " + tweet
    return False
  return True


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--postrain', nargs='?',
                      default='positive_training.txt',
                      help='Location of file with positive training data')
  parser.add_argument('-n', '--negtrain', nargs='?',
                      default='negative_training.txt',
                      help='Location of file with negative training data')
  parser.add_argument('-t', '--test', nargs='?', const=1, default=0,
                      help='Causes the program to test the accuracy')
  parser.add_argument('--postest', nargs='?',
                      default='positive_test.txt',
                      help='Location of file with positive test data')
  parser.add_argument('--negtest', nargs='?',
                      default='negative_test.txt',
                      help='Location of file with negative test data')
  parser.add_argument('-a', '--analyse', nargs='?', const=1, default=0,
                      help='Causes the program to analyse supplied data')
  parser.add_argument('--evalfiles', nargs='*',
                      help='Location of files containing data to be analysed')
  args = parser.parse_args()
  #print args
  # get training data
  training_set = read_file(args.postrain)+read_file(args.negtrain)

if __name__ == '__main__':
  main()
