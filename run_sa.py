#!/usr/bin/env python

import argparse
import sentiment_analysis

def read_file(file_name, value):
  data = []
  f = open(file_name, 'r')
  line = f.readline()
  while line != '':
    data.append([[e.lower() for e in line.split()], value])
    line = f.readline()
  f.close()
  return data

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
  training_set = read_file(args.postrain, 1)+read_file(args.negtrain, -1)
  print training_set
  # create analyzer
  sa = sentiment_analysis.SentimentAnalyser(training_set)
  print sa.features
  # train
  # analyze
  # present/save results

if __name__ == '__main__':
  main()
