#!/usr/bin/env python

import argparse

def read_file(file_name):
  data = []
  f = open(file_name, 'r')
  line = f.readline()
  while line != '':
    data.append(line.strip())
    line = f.readline()
  f.close()
  return data

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-d', '--datafiles', nargs='+',
                      help='Location of files containing sentiment analysis results')
  args = parser.parse_args()

  output = open('aggregated_results.csv', 'w')
  for f in args.datafiles:
    company, date, _ = f.rpartition('/')[2].split('_',2)
    values = read_file(f)
    value = 0
    for v in values:
      value += int(v)
    output.write(company+';'+date+';'+str(value)+'\n')
  output.close()

if __name__ == '__main__':
  main()
