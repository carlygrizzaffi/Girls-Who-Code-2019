#Put python in front of the file name in the command line
#First we need to import the json file
import json
#We also need to import io
import io
#Next we need to open the json file, we use r becuase we are reading it... w is writing to it (editing it)
tweetFile = open("tweets_small.json", "r")
#Next we need to load the json file (this is different from json data)
tweetData = json.load(tweetFile)

#Since we have stored the data into our variable, we can use the json file
tweetFile.close()

#We are printing the data of only ONE Tweet, we want to use the 0th index to access the first value
#We access the different categories of a tweet using "key", in this case it would be id
print("Tweet id: ", tweetData[0]["id"])
#How might we print the category of the tweet containing the text?
print("Tweet text: ", tweetData[0]["text"])
#How might we use loops?

#There are two ways of doing this

#Python allows us to cycle through each element in our json data vairable without the need for indices. Ex: for each char in string
for tweet in tweetData:
    print("Tweet text: " + tweet["text"])

#Here we are looping through the tweets using the indices and the length function to get our stopping point
for x in range(len(tweetData)):
    print("Tweet text: " + tweetData[x]["text"])
