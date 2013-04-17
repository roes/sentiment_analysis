#!/usr/bin/env python

import argparse
import sentiment_analysis

def read_file(file_name, value=None):
  data = []
  f = open(file_name, 'r')
  line = f.readline()
  while line != '':
    if value is None:
      data.append([e.lower() for e in line.split()])
    else:
      data.append([[e.lower() for e in line.split()], value])
    line = f.readline()
  f.close()
  return data

def classify(file_name, sa):
  data_set = read_file(file_name)
  f = open(file_name[:-4]+'_result.txt', 'w')
  reputation = 0
  for d in data_set:
    value = sa.classify(d)
    reputation += value
    f.write(str(value)+'\n')
  f.close()
  return reputation

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
  print args
  # get training data
  training_set = read_file(args.postrain, 1)+read_file(args.negtrain, -1)
  # create analyzer
  # train
  sa = sentiment_analysis.SentimentAnalyser(training_set)
  # analyze
  if args.test:
    test_set = read_file(args.postest, 1)+read_file(args.negtest, -1)
    print sa.test_accuracy(test_set)
  # present/save results
  if args.analyse:
    for f in args.evalfiles:
      print classify(f, sa)

if __name__ == '__main__':
  main()
