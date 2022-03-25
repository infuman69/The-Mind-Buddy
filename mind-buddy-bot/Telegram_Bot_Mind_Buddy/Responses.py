from datetime import datetime
import re
from sqlite3 import Date

from matplotlib.style import use
import imp
from textblob import TextBlob


def sentiment_analysis(y):

    # y= input("Type your sentence: ")
    edu= TextBlob(y)

    x= edu.sentiment.polarity


    if x<0:
        print("Negative")

    elif x==0:
        print("Neutral")

    elif x>0 and x<=1:
        print("Positive")   


def sample_responses(input_text):
    user_message = str(input_text)

    if user_message in ('hello', "hi", "ssup"):
        return "Hey! How's it going?"

    if user_message in ('who are you', "who are you?", "what are you?", "what are you"):
        return "I am your Mental Health buddy! I am a bot and I am here to help you with your downtime."

    if user_message in ('time', "time?", "what time is it?", "what's the time?", "what is the time?", "what is the time", "what's the time"):
        now = datetime.now()
        date_time= now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    if user_message in ("i don't feel good", "i am sad", "sad", "not good ", "ugh", "i don't know"):
        return "I understand! It's okay not to feel okay sometimes!"

    if user_message in ("i don't feel good", "i am sad", "sad", "not good ", "ugh", "i don't know"):
        sentiment_analysis("I am sad")

        return "I understand! It's okay not to feel okay sometimes!"

    if user_message in ("yes"):
        return "What do you think is going wrong?"

    if user_message in ("i am anxious", "i suffer from extreme worries", "i have fear of anticipation", "i suffer from irritability", "i suffer from extreme worries and i have fear of anticipation"):
        sentiment_analysis("I am sad")

        return "Ok! That seems like mild anxiety! It's perfectly manageable........"

    if user_message in ("i am often very tensed", "i suffer from the constant feeling of tension", "i have extreme fatigue", "i startle too easily", "tears", "i cry a lot", "i can't relax"):
        return "Okay, you might have mild anxiety! Nothing to worry about. With just a few exercises you can bring it under control!......"

    if user_message in ("fear of dark", "being alone", "fear of animals", "afraid of animals", "afraid of traffic", "fear of crowds"):
        return "Huff! You will be relieved to find that this is perfectly normal amoung human beings. Being afraid of such entitites is second nature to homo sapiens! Relax, will ya!"

    if user_message in ("insomnia", "i have difficulty falling asleep", "i suffer from broken sleep", "unsatisfying sleep", "fatigue on walking", "I often have nightmares"):
        return "Right, so it looks like you have a mild to moderate level of anxiety! You might wanna consider seeking help. Perhaps you should talk to your family members! Do you want us to ping them up?"

    if user_message in ("yes ping"):
        return "Sending text right away......"

    if user_message in ("no don't ping", "don't ping"):
        return "Okay! We respect your privacy! We suggest you ask for help at any early stage!" 

    if user_message in ("i can't concentrate", "i have poor memory", "i think i have poor memory", "poor memory", "can't concentrate"):

        return "That's perfectly normal! A lot of people have trouble concentrating, or simply have a poor memory! You should let that pass!"

    if user_message in ("i am so depressed you know", "i am depressed", "i am sick", "i am crying", "oh my god"):
        sentiment_analysis("I am sad")

        return "It's okay we are here to help! Do you want us to call someone?"

    if user_message in ("yes call"):
        return "Calling emergency contact..."

    if user_message in ("no dont call", "no don't call", "don't call"):
        sentiment_analysis("I am sad")

        return "Okay! We respect your privacy! We can suggest a few exercises to help with you depression!"

    if user_message in ("no don't call i'm afraid", "no, no one should find out"):
        return "Hey! It's okay, you can trust us. We respect your privacy. But you should never be afraid to seek help."

    if user_message in ("what do i do i wanna suicide", "i wanna suicide",  "I wanna suicide", "suicide", "I wanna suicide"):
        sentiment_analysis("I am sad")
        return "Heyyy relax! Don't take any drastic measures. We are here to help you! Talk to us!"

    if user_message in ("helpline number", "national helpline"):
        return "Here's the national mental health helpline number: 080-46110007. Please feel free to contact them anytime."

    if user_message in ("nothing feels right"):
        return "It's okay! It doesn't have to always feel right! Life is all about ups and downs! But ending it no solution at all! Here's the national mental health helpline number: 080-46110007. Please feel free to contact them anytime. "

    if user_message in ("i suffer from muscular aches", "i suffer from twiching", "i have twitching", "i have stiffness", "i have grinding of teeth", "i have unsteady voice", "pains and aches", "grinding of teeth"):
        return "Okay! Based on the symptoms described by you, we infer that you might have moderate anxiety disorder! Don't worry, we are here to help! We suggest you seek help! We will connect you to some of the best mental health clinics in the country."

    return "I understand!"

    # if user_message in ('hello', "hi", "ssup"):
    #     return "Hey! How's it going?"

    # if user_message in ('hello', "hi", "ssup"):
    #     return "Hey! How's it going?"
    
