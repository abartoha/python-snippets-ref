'''
Snippet #130-Sentiment Analysis
stevepython.wordpresss.com

Tested on Win 7.

source:
https://www.pythonprogramming.in/natural-language-processing-in-python/sentiment-analysis-using-textblob.html

pip3 install textblob
'''

from textblob import TextBlob


def sentiment(polarity):
    if blob.sentiment.polarity < 0:
        print("Negative")
    elif blob.sentiment.polarity > 0:
        print("Positive")
    else:
        print("Neutral")

print()
print()

blob = TextBlob("The movie was excellent. It was the shitz!")
print('- ' *20)
print(blob)
print()
print(blob.sentiment)
sentiment(blob.sentiment.polarity)
print('- ' *20)

blob = TextBlob("The movie was okay, good in places, bad in others.")
print(blob)
print()
print(blob.sentiment)
sentiment(blob.sentiment.polarity)


print('- ' *20)
blob = TextBlob("The movie was ridiculous. I hated it. I wasted my time, that's 2 hours I will never get back of my life and now I can't unsee it ffs. ")
print(blob)
print()
print(blob.sentiment)
sentiment(blob.sentiment.polarity)
print('- ' *20)
