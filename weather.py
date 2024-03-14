import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot('*******')
API = '**********'

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Привет, напиши название города')

@bot.message_handler(content_types=['text'])
def get_weather(msg):
    city = msg.text.strip().lower()
    req = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if req.status_code == 200:
        data = json.loads(req.text)
        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        bot.reply_to(msg, f'Температура у указанном городе: {temp} °C\nПогода: \n')
        if weather.lower() == 'clouds':
            file = open('img/cloud.bmp', 'rb')
            bot.send_photo(msg.chat.id, file)
        if weather.lower() == 'rain':
            file = open('img/rain.bmp', 'rb')
            bot.send_photo(msg.chat.id, file)
        if weather.lower() == 'clear':
            file = open('img/clear.bmp', 'rb')
            bot.send_photo(msg.chat.id, file)
        if weather.lower() == 'snow':
            file = open('img/snow.bmp', 'rb')
            bot.send_photo(msg.chat.id, file)
    else:
        bot.reply_to(msg, f'Город не найден')

bot.polling(non_stop=True)
