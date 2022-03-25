import imp
from textblob import TextBlob
import imp
y= input("Type your sentence: ")
edu= TextBlob(y)

x= edu.sentiment.polarity


if x<0:
    print("Negative")

elif x==0:
    print("Neutral")

elif x>0 and x<=1:
    print("Positive")   