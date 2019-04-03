#https://youtu.be/jhFsFZXZbu4
#https://github.com/eternnoir/pyTelegramBotAPI#message-handlers
import telebot
from time import strftime
import time

bot_token = ''

bot = telebot.TeleBot(token=bot_token)

chat_id = '-352926939'

afk_name = []

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Fuck you')

def extract_arg(arg):
    return '+'.join(arg.split()[1:])

def space_to_plus_sign(arg):
    return '+'.join(arg.split())

@bot.message_handler(commands=['ph', 'pornhub'])
def ph(message):
    if message.reply_to_message is None:
        status = extract_arg(message.text.replace('+', '%2B'))
        bot.reply_to(message, 'https://www.pornhub.com/video/search?search=' + status)
    elif not message.reply_to_message.text is None:
        bot.reply_to(message.reply_to_message, 'https://www.pornhub.com/video/search?search=' + space_to_plus_sign(message.reply_to_message.text.replace('+', '%2B')))

@bot.message_handler(commands=['google'])
def google(message):
    if message.reply_to_message is None:
        status = extract_arg(message.text.replace('+', '%2B'))
        bot.reply_to(message, 'https://www.google.com/search?q=' + status)
    elif not message.reply_to_message.text is None:
        bot.reply_to(message.reply_to_message, 'https://www.google.com/search?q=' + space_to_plus_sign(message.reply_to_message.text.replace('+', '%2B')))

@bot.message_handler(commands=['wolframalpha', 'wa'])
def wolframalpha(message):
    if message.reply_to_message is None:
        status = extract_arg(message.text.replace('+', '%2B'))
        bot.reply_to(message, 'https://www.wolframalpha.com/input/?i=' + status)
    elif not message.reply_to_message.text is None:
        bot.reply_to(message.reply_to_message, 'https://www.wolframalpha.com/input/?i=' + space_to_plus_sign(message.reply_to_message.text.replace('+', '%2B')))

@bot.message_handler(commands=['kick'])
def kick(message):
    bot.kick_chat_member(chat_id, message.reply_to_message.from_user.id)

@bot.message_handler(commands=['purge'])
def purge(message):
    if not message.reply_to_message is None:
        for x in range(message.reply_to_message.message_id, message.message_id):
            try:
                bot.delete_message(chat_id, x)
            except:
                continue
        bot.delete_message(chat_id, message.message_id)

@bot.message_handler(commands=['delete', 'del'])
def delete(message):
    if not message.reply_to_message is None:
        bot.delete_message(chat_id, message.reply_to_message.message_id)
        bot.delete_message(chat_id, message.message_id)

@bot.message_handler(commands=['now'])
def now(message):
    bot.reply_to(message, strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))

@bot.message_handler(func=lambda message: 'steal' in message.text.lower() , content_types=['text'])
def steal(message):
    bot.reply_to(message, 'Steal practice huh')

@bot.message_handler(func=lambda message: '@' + message.from_user.username in afk_name)
def remove_afk(message):
    bot.reply_to(message, 'No longer afk!')
    afk_name.remove('@' + message.from_user.username)

@bot.message_handler(commands=['afk'])
def afk(message):
    afk_name.append('@' + message.from_user.username)
    bot.reply_to(message, message.from_user.username + ' started steal practising!')

def check_in_list(message):
    m = [x for x in message.text.split() if '@' in x]
    return ''.join(m) in afk_name

@bot.message_handler(func=check_in_list)
def tagging_afk_name(message):
    bot.reply_to(message, 'He is steal practising!')

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
