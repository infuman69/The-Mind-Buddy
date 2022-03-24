from datetime import datetime
import re
from sqlite3 import Date

def sample_responses(input_text):
    user_message = str(input_text).lower()

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
        if user_message in ("i can't do it", "i can't", "its not fair"):
            return "I know! Its okay!"



    return "I understand!"

    # if user_message in ('hello', "hi", "ssup"):
    #     return "Hey! How's it going?"

    # if user_message in ('hello', "hi", "ssup"):
    #     return "Hey! How's it going?"
    
