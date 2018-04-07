# BitCamp 2018 - Twitter Emotion/Sentiment Analysis

4/6/18 - 4/8/18
By: Mamadou Mouctar and Shawn Jassal

This project was made during the 2018 BitCamp event at the University of Maryland College Park. We did this as an expierence to expose ourselves to new applications that we had not yet used.

This project will analyze data about the relationships between twitter users. The program will take in a twitter handle, and parse all the tweets of that twitter handle in the past 30 days. From this we will analyze the connections between the current handle and all other connections referred to in the users tweets, like other twitter handles and hashtags. We use the free version of Indico, a sentiment analysis program to obtain the rating of the tweets.

While creating the program we learned a bit about Indico. Because of this we found aspects of its analysis we thought were inconsistent, such as:
	- Indico was not affected by everything being capitilized
	- @ symbols at, what appears to be, a random effect on the sentiment rating of all messages. For example, sometimes adding more @ symbols would raise the sentiment rating and other times it would lower the rating.
	- Just like @ symbols the # symbol would have a random effect on the sentiment rating of all messages.

Because of what we found we chose to remove all @ and # from the text before we used Indico to find the sentiment rating.
