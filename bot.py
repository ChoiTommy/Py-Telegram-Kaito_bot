#https://youtu.be/jhFsFZXZbu4
import telebot
import time

bot_token = ''

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Fuck you')

def extract_arg(arg):
    return '+'.join(arg.split()[1:])

@bot.message_handler(commands=['google'])
def google(message):
    status = extract_arg(message.text)
    bot.reply_to(message, 'https://www.giyf.com/' + status)

@bot.message_handler(commands=['wolframalpha', 'wa'])
def wolframalpha(message):
    status = extract_arg(message.text)
    bot.reply_to(message, 'https://www.wolframalpha.com/input/?i=' + status)

bot.polling()
