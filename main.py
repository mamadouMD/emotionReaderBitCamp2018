import functions
import Tweet
import os

def main():
	os.system("python functions.py")
	os.system("python Tweet.py")

	data = {"Shawn": Tweet.Tweet("I Hate @Shawn",["@Shawn"],[]),
			"Bob": Tweet.Tweet("Goodbye, @Bob",["@Bob"],[])}
	functions.printData(data)

if __name__== "__main__":
  main()
