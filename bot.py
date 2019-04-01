#https://youtu.be/jhFsFZXZbu4
#https://github.com/eternnoir/pyTelegramBotAPI#message-handlers
import telebot

bot_token = ''

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'Fuck you')

def extract_arg(arg):
    return '+'.join(arg.split()[1:])

def space_to_plus_sign(arg):
    return '+'.join(arg.split())

@bot.message_handler(commands=['google'])
def google(message):
    if message.reply_to_message is None:
        status = extract_arg(message.text)
        bot.reply_to(message, 'https://www.giyf.com/' + status)
    elif not message.reply_to_message.text is None:
        bot.reply_to(message.reply_to_message, 'https://www.giyf.com/' + space_to_plus_sign(message.reply_to_message.text))

@bot.message_handler(commands=['wolframalpha', 'wa'])
def wolframalpha(message):
    if message.reply_to_message is None:
        status = extract_arg(message.text)
        bot.reply_to(message, 'https://www.wolframalpha.com/input/?i=' + status)
    elif not message.reply_to_message.text is None:
        bot.reply_to(message.reply_to_message, 'https://www.wolframalpha.com/input/?i=' + space_to_plus_sign(message.reply_to_message.text))

bot.polling()
