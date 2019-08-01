#Import your Twitter data, json library, and textblob library.
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
#Create a list for polarity and subjectivity.
polarity = []
subjectivity = []
#For each tweet, make a textblob from the text.
for x in range(len(tweetData)):
    testimonial = TextBlob(tweetData[x]["text"])
    testimonial.sentiment
    subjectivity.append(testimonial.sentiment.subjectivity)
    polarity.append(testimonial.sentiment.polarity)
    #Sentiment(polarity=[-1.0, 0.0, 1.0] , subjectivity=[-1.0, 0.0, 1.0])
    print("Polarity")
    print(testimonial.sentiment.polarity)
    print("Subjectivity")
    print(testimonial.sentiment.subjectivity)
#Store each tweet's polarity and subjectivity in the list.
testimonial.sentiment.polarity
testimonial.sentiment.subjectivity
#Print out the average polarity and subjectivity.
# Textblob sample:
#tb = TextBlob("You are a brilliant computer scientist.")
#print(tb.polarity)
tb = TextBlob("tweets_small.json")
print(tb.polarity)

#Create a histogram plot in matplotlib.
import numpy as np
import matplotlib.pyplot as plt
import random
from numpy.random import RandomState

subjectity = np.random.randn(1000)
#Set the axis to fit you data range
#Give it polarity data and a list of bins.
plt.hist(subjectivity, bins = 30, color = "blue")
plt.title("Subjectivity")
#Set the x and y labels.
plt.xlabel("Value")
plt.ylabel("Frequency")
#Show your plot.
#plt.show()
plt.close()

#Create another histogram for polalrity.
import numpy as np
import matplotlib.pyplot as plt
import random
from numpy.random import RandomState

subjectity = np.random.randn(1000)
#Set the axis to fit your data range
#Give it polarity data and a list of bins.
plt.hist(polarity, bins = 30, color = "teal")
plt.title("Polarity")
#Set the x and y labels.
plt.xlabel("Value")
plt.ylabel("Frequency")
#Show your plot.
#plt.show()
plt.close()

#Create a scatterplot
plt.scatter(subjectivity, polarity, color = 'magenta')

plt.xlim([-.75,1.25])
plt.ylim([0,1])
plt.title("Scatter Plot")
plt.xlabel("Subjectivity")
plt.ylabel("Polarity")
#plt.show()
#Clear out memory
plt.close()


#Combine all the tweets into one large string.
    #Remember loops and string operators
ongoing = ""

for x in tweetData:
    y = x["text"]
    ongoing = ongoing + y
#Create a textblob from the combined string.
tweetblob = TextBlob(ongoing)
#Generate your own dictionary of `filteredWords[word] = count` by looping TextBlob's words list and word_counts dictionary.
    #Skip words you don't want in your filtered dictionary.
    #Try filtering words that are less than three letters.
    #Try creating a list of common words to filter like "and," "about," "the," "http," etc. and skip words `in` that list.
    #Try filtering things that aren't words.
wordsToFilter = ["about", "https", "in", "the", "thing", "will", "could", "automation", "I", "to"]
filteredDictionary = dict()

for word in tweetblob.words:
    if len(word) < 2:
        continue
    if not word.isalpha():
        continue
    if word.lower() in wordsToFilter:
        continue
    #if len(word) < 5 and word.upper() ! = word:
        #continue;
    #Code below is adding the words into our filtered dictionary
    filteredDictionary[word.lower()] = tweetblob.word_counts[word.lower()]
#Generate a word cloud from the frequencies.
    #Consider the questions below as you work:
    #How can you combine strings?
    #What words do you not want to show up in your word cloud? How can you filter those out using Python’s `continue` keyword?
    #What things does TextBlob mistake for a word? How might you use Python’s `isalpha()`function to filter out numbers and urls?
    #Can you draw any conclusions from this data? Are there limits to what you can conclude? Why?
wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.show()
plt.close()
