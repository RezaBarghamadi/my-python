import random
import datetime
import datetime
from persiantools import jdatetime
import qrcode
import gtts
import telebot
from telebot import types

bot = telebot.TeleBot("6735893555:AAF6Gba1ENdJGZGbWOrF0q6Uc_ZTkoqJIb8", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=7)
key1 = telebot.types.KeyboardButton("game")
key2 = telebot.types.KeyboardButton("Age")
key3 = telebot.types.KeyboardButton("Voice")
key4 = telebot.types.KeyboardButton("Max")
key5 = telebot.types.KeyboardButton("Argmax")
key6 = telebot.types.KeyboardButton("QRcode")
markup.add(key1, key2, key3, key4, key5, key6)
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f" Welcome, {user_name} ", reply_markup=markup)

@bot.message_handler(func= lambda m : True)
def Main_Func(message) :

    if message.text == "Game" :
        Start_Game(message)
    elif message.text == "New game" :
        New_Game(message)
    elif message.text == "Home" :
        ...
    elif message.text == "Age" :
        Get_Birthday(message)
    elif message.text == "Voice" :
        Voice_Text(message)
    elif message.text == "Max" : 
        Get_Numbers(message)
    elif message.text == "Argmax":
        Get_Numbers_2(message)
    elif message.text =="QRcode" :
        QRCode_Text(message)
    
    
    
Number = random.randint(1, 50)
chat_id = None
Counter = 0

def Home(message):

    
    markup = telebot.types.ReplyKeyboardMarkup(row_width=7)
    key1 = telebot.types.KeyboardButton("game")
    key2 = telebot.types.KeyboardButton("Age")
    key3 = telebot.types.KeyboardButton("Voice")
    key4 = telebot.types.KeyboardButton("Max")
    key5 = telebot.types.KeyboardButton("Argmax")
    key6 = telebot.types.KeyboardButton("QRcode")
    markup.add(key1, key2, key3, key4, key5, key6)
    
    lst = ["Alright","OK","Okay","Fair enough","Sure"]
    bot.reply_to(message,random.choice(lst), reply_markup=markup)

def Start_Game(message):
        
        global chat_id
        chat_id = message.chat.id
        markup = types.ReplyKeyboardMarkup(row_width=1)
        item_markup1 = types.KeyboardButton("New game")
        item_markup2 = types.KeyboardButton("Home")
        markup.add(item_markup1)
        markup.add(item_markup2)
        msg = bot.send_message(chat_id, "Guess a Number between 1 to 50", reply_markup=markup)
        bot.register_next_step_handler(msg, Guess_Number)

def Guess_Number(message):

    global Number
    global Counter

    if message.text == "Home" :
        Home(message)
    elif message.text == "New game" :
        New_Game(message)
    else: 
        guess = int(message.text)
        if guess > Number:
            Counter += 1
            msg = bot.send_message(chat_id, "Go down ")
            bot.register_next_step_handler(msg, Guess_Number)
        elif guess < Number:
            Counter += 1
            msg = bot.send_message(chat_id, "Go up ")
            bot.register_next_step_handler(msg, Guess_Number)
        elif guess == Number:
            bot.send_message(chat_id, f"That is correct  | you`ve had {Counter + 1} guesses ")
            markup.add(key1, key2, key3, key4, key5, key6)
            Counter = 0
        

def New_Game(message):

    global Counter
    global Number
    Number = random.randint(1, 50)
    msg = bot.send_message(chat_id, "Guess a Number between 1 to 50")
    bot.register_next_step_handler(msg, Guess_Number)


def Get_Birthday(message):
    msg = bot.send_message(message.chat.id, "Enter Your Birth Day By Template this Year-Month-Day")
    bot.register_next_step_handler(msg, Calculate_Age)

def Calculate_Age(message):
    birthday_year, birthday_month, birthday_day = map(int, message.text.split("-"))
    miladi_date = jdatetime.JalaliDate(birthday_year, birthday_month, birthday_day).to_gregorian()
    age_timedelta = datetime.date.today() - miladi_date
    age_years = age_timedelta.days // 365
    bot.send_message(message.chat.id, f"You are {age_years} years old")


def Voice_Text(message):
    msg = bot.send_message(message.chat.id, "Please give me an English text")
    bot.register_next_step_handler(msg, Text_To_Voice)

def Text_To_Voice(message):
    user_text = message.text
    voice = gtts.gTTS(user_text, lang="en", slow=False)
    voice.save("my-python/Assignment_9/voice.mp3")
    with open("my-python/Assignment_9/voice.mp3", "rb") as voice_file:
      bot.send_voice(message.chat.id, voice_file)


def Get_Numbers(message):
    msg = bot.send_message(message.chat.id, "Please give me a list of numbers like this 14,7,78,15,8,19,20")
    bot.register_next_step_handler(msg, Show_Max)

def Show_Max(message):
    Numbers = list(map(int, message.text.split(",")))
    Max_Number = max(Numbers)
    bot.send_message(message.chat.id, f" The maximum number is {Max_Number}")


def Get_Numbers_2(message):
    msg = bot.send_message(message.chat.id, "Please give me a list of numbers like this 14,7,78,15,8,19,20")
    bot.register_next_step_handler(msg, Show_Max_Arg)


def Show_Max_Arg(message):
    Numbers = list(map(int, message.text.split(",")))
    Max_Index = Numbers.index(max(Numbers))
    bot.send_message(message.chat.id, f"Maximum number index is {Max_Index}")

def QRCode_Text(message):
    msg = bot.send_message(message.chat.id, "Please give me your text")
    bot.register_next_step_handler(msg, Create_QRCode)

def Create_QRCode(message):
    qr_img = qrcode.make(message.text)
    qr_img.save("my-python/Assignment_9/qrcode.png")
    with open("my-python/Assignment_9/qrcode.png", "rb") as qr_file:
        bot.send_photo(message.chat.id, qr_file)
        
bot.infinity_polling()