#!/usr/bin/python
import functions
import Tweet
import parser
import os
import sys

# This is the main driver method.
# It takes 1 argument:
#	- One twitter handle (without the @)

def main():
	data = parser.getTweets(sys.argv[1])
	functions.printMentionHashtagSentiment(data)

if __name__== "__main__":
  main()