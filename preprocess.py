#!/usr/bin/env python

import argparse
import sys

happy_emot = [":)", ":-)", "=)", ":D", "=D", ": )"]
sad_emot = [":(", ":-(", ": ("]

# Reads a file of tweets and removes unwanted parts.

def read_file(file_name, training):
  data = []
  f = open(file_name, 'r')
  line = f.readline()
  while line != '':
    if training:
      if accept_tweet(line):
        data.append(line)
      else:
        print "Removing tweet: " + line
      line = f.readline()
    else:
      data.append(line)
      line = f.readline()
  f.close()
  i = 0
  for tweet in data:
    tweet = process_words(tweet)
    data[i] = tweet
    i += 1
  for ptweet in data:
      print ptweet
  return data

# Changes and removes unwanted features in the tweet.
# Looks for repeated sequences of characters, 
# at-signs and links at the moment..
def process_words(tweet):
  data = tweet.split()
  i = 0
  for word in data:
    #Usernames
    if word.startswith('@'):
      data[i] = "USERNAME"
      i += 1
      continue
    #Links
    if isURL(word):
      data[i] = "URL"
      i += 1
      continue
    #Repeated characters
    word = repeated_letter(word)
    data[i] = word
    i += 1
  return data

#Checks for repeated characters in a word and cuts the repetition to two.

def repeated_letter(word):
  prev_letter = ''
  num_rep = 0
  res = ""
  for letter in word:
    if letter == prev_letter:
      num_rep += 1
      if num_rep > 1: #throw the letter
        continue
      else:
        res += letter
    else:
      num_rep = 0
      prev_letter = letter
      res += letter
  return res


#Returns true if the string is considered an URL.

def isURL(word):
  if word.startswith("http"):
    return True
  else:
    return False

# Determines whether the tweet should be in the training set.
# Checks for retweets and emoticons of both types (happy/sad).

def accept_tweet(tweet):
  happy = False
  sad = False
  data = ([e.lower() for e in tweet.split()])
  for word in data:
    if word == "rt":
      return False
    elif word in happy_emot:
      happy = True
    elif word in sad_emot:
      sad = True
  if happy and sad:
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
  parser.add_argument('-t', '--training', nargs='?',
                      const=True, default=False, 
                      help='Use to analyse training data')
  args = parser.parse_args()
  processed_set = []
  if args.training:
    #Training data
    if len(sys.argv) < 3:
      print "Must give a file to process.."
      return
    processed_set = read_file(sys.argv[2], True)
  else:
    #TODO
    processed_set = read_file(args.postrain, False)

  #Write to file here.
  f = open(str(sys.argv[2] + 'a'),'w')
  for tweet in processed_set:
    for feature in tweet:
      f.write(feature + " ")
    f.write('\n')
  f.close()

if __name__ == '__main__':
  main()
