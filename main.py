import os
import telebot
import random
from flask import Flask, request

API_KEY = os.environ.get("API_KEY")
bot = telebot.TeleBot(token=API_KEY)
server = Flask(__name__)

frases = ["Ni idea!", "Se lo comió el mar..", u"\U0001F937\u200D\u2642\uFE0F", "Ay mi niño..", "Ya no me acuerdo de él :(", "Ese es el monito ese?", "Voló..", "No sufras tanto, por favor", "Me gustas cuando callas porque estás como ausente", "Dice que trabaja..", "Obvio está borracho", "Lo perdimos amigo, lo perdimos.." ]

@bot.message_handler(commands=['dondeestagustavo'])
def dondeEstaGustavo(message):

  msj = random.choice(frases)
  bot.reply_to(message, msj)

@bot.message_handler(commands=['pinggustavo'])
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

@bot.message_handler(commands=['compregustavo'])
def compreGustavo(message):

  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")
  bot.send_message(message.chat.id, "Compre Gustavo!")


@server.route('/' + API_KEY, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegram-gustavo-bot.herokuapp.com/' + API_KEY)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
