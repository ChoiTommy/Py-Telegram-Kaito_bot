#https://youtu.be/jhFsFZXZbu4
#https://github.com/eternnoir/pyTelegramBotAPI#message-handlers
import telebot

bot_token = ''

bot = telebot.TeleBot(token=bot_token)

chat_id = '-352926939'

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
        
@bot.message_handler(commands=['delete'])
def delete(message):
    if not message.reply_to_message is None:
        bot.delete_message(chat_id, message.reply_to_message.message_id)
        bot.delete_message(chat_id, message.message_id) 

bot.polling()
