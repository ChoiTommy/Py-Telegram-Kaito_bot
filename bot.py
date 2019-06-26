#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from time import strftime
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')


bot_token = ''

bot = telebot.TeleBot(token=bot_token)

chat_id = '-1001356677647'

#afk_list = []

#mute_list = []

'''
def is_admin(id):
    return (bot.get_chat_member(chat_id, id).status == 'administrator') or (bot.get_chat_member(chat_id, id).status == 'creator')
'''

@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, 'What\'s your problem?')


def extract_arg(arg):
    return '+'.join(arg.split()[1:])

def extract_string(string):
    return ' '.join(string.split()[1:])

def extract_arg_2(arg):
    return '+'.join(arg.split())

@bot.message_handler(commands=['ph', 'pornhub'])
def ph(message):
    if message.reply_to_message is None:
        status = extract_arg(message.text)
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(extract_string(message.text), url='https://www.pornhub.com/video/search?search=' + status ) )
        bot.reply_to(message, 'Here is your ' + extract_string(message.text) + 'from ph:', reply_markup = keyboard)
    elif not message.reply_to_message.text is None:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(message.reply_to_message.text, url='https://www.pornhub.com/video/search?search=' + extract_arg_2(message.reply_to_message.text) ) )
        bot.reply_to(message, 'Here is your ' +  message.reply_to_message.text + 'from ph:', reply_markup = keyboard)

'''
@bot.message_handler(commands=['kick'])
def kick(message):
    if is_admin(message.from_user.id):
        bot.kick_chat_member(chat_id, message.reply_to_message.from_user.id)

@bot.message_handler(commands=['purge'])
def purge(message):
    if is_admin(message.from_user.id):
        if not message.reply_to_message is None and not message.from_user.is_bot:
            for x in range(message.reply_to_message.message_id, message.message_id):
                try:
                    bot.delete_message(chat_id, x)
                except:
                    continue
            bot.delete_message(chat_id, message.message_id)

@bot.message_handler(commands=['delete', 'del'])
def delete(message):
    if is_admin(message.from_user.id):
        if not message.reply_to_message is None:
            bot.delete_message(chat_id, message.reply_to_message.message_id)
            bot.delete_message(chat_id, message.message_id)
'''

@bot.message_handler(commands=['now'])
def now(message):
    bot.reply_to(message, strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))

words = ['練', '偷', '做', 'In', '睇']

@bot.message_handler(func=lambda message: '睇' in message.text , content_types=['text'])
def steal(message):
    bot.reply_to(message, '睇完又睇')
    bot.reply_to(message, '日睇夜睇')
    bot.reply_to(message, '一睇再睇')
    bot.reply_to(message, '死睇爛睇')

@bot.message_handler(func=lambda message: '做' in message.text , content_types=['text'])
def steal(message):
    bot.reply_to(message, '做完又做')
    bot.reply_to(message, '日做夜做')
    bot.reply_to(message, '一做再做')
    bot.reply_to(message, '死做爛做')

@bot.message_handler(func=lambda message: '偷' in message.text , content_types=['text'])
def steal(message):
    bot.reply_to(message, '偷完又偷')
    bot.reply_to(message, '日偷夜偷')
    bot.reply_to(message, '一偷再偷')
    bot.reply_to(message, '死偷爛偷')

@bot.message_handler(func=lambda message: '練' in message.text , content_types=['text'])
def steal(message):
    bot.reply_to(message, '練完又練')
    bot.reply_to(message, '日練夜練')
    bot.reply_to(message, '一練再練')
    bot.reply_to(message, '死練爛練')

'''
# mute
@bot.message_handler(commands=['mute'])
def mute(message):
    if is_admin(message.from_user.id):
        if message.reply_to_message is not None and message.reply_to_message.from_user not in mute_list:
            mute_list.append(message.reply_to_message.from_user)
            bot.reply_to(message.reply_to_message, 'Muted')
    else:
        bot.reply_to(message, 'You are not an admin!')


@bot.message_handler(func=lambda message: message.from_user in mute_list)
def mute_message(message):
    bot.delete_message(chat_id, message.message_id)

@bot.message_handler(commands=['unmute'])
def unmute(message):
    if is_admin(message.from_user.id):
        if message.reply_to_message is not None and message.reply_to_message.from_user in mute_list:
            mute_list.remove(message.reply_to_message.from_user)
            bot.reply_to(message.reply_to_message, 'U can join now')
    else:
        bot.reply_to(message, 'You are not an admin!')

@bot.message_handler(commands=['afk'])
def afk(message):
    afk_list.append(message.from_user)
    bot.reply_to(message, bot.get_chat_member(chat_id, message.from_user.id).user.username + ' started steal practising!')


@bot.message_handler(func=lambda message: message.from_user in afk_list)
def remove_afk(message):
    bot.reply_to(message, 'No longer afk!')
    afk_list.remove(message.from_user)

def check_in_list(message):
    #m = [x for x in message.text.split() if '@' in x]
    #return ''.join(m) in afk_name
    if message.entities is not None:
        for x in message.entities:
            if x.type == 'mention' and x.user in afk_list:
            #'@' + x == bot.get_chat_member(chat_id, afk_id).user.username:
                return True
        #return message.entities[].user.id in afk_id

@bot.message_handler(func=check_in_list)
def tagging_afk_name(message):
    bot.reply_to(message, 'He is steal practising!')


@bot.message_handler(commands=['muteall'])
def mute_all(message):
    bot.reply_to(message, 'Only admins are allowed to send messages from now.')
    mute_status = True

@bot.message_handler(commands=['unmuteall'])
def unmute_all(message):
    bot.reply_to(message, 'Everyone can speak freely now.')
    mute_status = False

@bot.message_handler(func=lambda message: not is_admin(message.from_user.id))
def del_non_admins_messages(message):
    if mute_status:
        bot.delete_message(chat_id, message.message_id)

@bot.message_handler(commands=['mute_list'])
def mute_list(message):
    if mute_id is not None:
        bot.reply_to(message, mute_id)
    else:
        bot.reply_to(message, 'Null')
'''
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)

#https://youtu.be/jhFsFZXZbu4
#https://github.com/eternnoir/pyTelegramBotAPI#message-handlers
#https://www.mindk.com/blog/how-to-develop-a-chat-bot/
