#!/usr/bin/env python

import argparse

from nltk.classify import NaiveBayesClassifier

def read_training_set(positive_training_set, negative_training_set):
  training_set = []
  f = open(positive_training_set, 'r')
  line = f.readline()
  while line != '':
    training_set.append([line, 1])
    line = f.readline()
  f.close()
  f = open(negative_training_set, 'r')
  line = f.readline()
  while line != '':
    training_set.append([line, -1])
    line = f.readline()
  f.close()
  return training_set

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
  parser.add_argument('--eval', nargs='?', const=1, default=0,
                      help='Causes the program to evaluate supplied data')
  parser.add_argument('--evalfiles', nargs='*',
                      help='Location of files containing eval data')
  args = parser.parse_args()
  print args
  # get training data
  training_set = read_training_set(args.postrain, args.negtrain)
  print training_set
  # create analyzer
  # train
  # analyze
  # present/save results

if __name__ == '__main__':
  main()
