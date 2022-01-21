import os
import telebot
import random

API_KEY = os.environ['API_KEY'] 
bot = telebot.TeleBot(API_KEY)

frases = ["Ni idea!", "Se lo comió el mar..", u"\U0001F937\u200D\u2642\uFE0F", "Ay mi niño..", "Ya no me acuerdo de él :(", "Ese es el monito ese?", "Voló..", "No sufras tanto, por favor", "Me gustas cuando callas porque estás como ausente", "Dice que trabaja..", "Obvio está borracho", "Lo perdimos amigo, lo perdimos.." ]

@bot.message_handler(commands=['DondeEstaGustavo'])
def dondeEstaGustavo(message):

  msj = random.choice(frases)
  bot.reply_to(message, msj)

@bot.message_handler(commands=['PingGustavo'])
def pingGustavo(message):

  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")
  bot.send_message(message.chat.id, "Ping Gustavo!")

bot.polling()