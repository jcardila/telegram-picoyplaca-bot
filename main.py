import os
import telebot
import random
from flask import Flask, request
from datetime import datetime, date, timedelta
import pytz

# API_KEY = os.environ.get("API_KEY")
# bot = telebot.TeleBot(token=API_KEY)
# server = Flask(__name__)

#Inicializar variables globales
local_date = datetime.now(pytz.timezone('America/Bogota'))  # use datetime here
fecha_hoy = local_date.date()                                       # now call date method
fecha_hoy_str = str(fecha_hoy)
weekday_hoy = fecha_hoy.isoweekday()  #Monday is 1 and Sunday is 7

#Pico y placa actual Bucaramanga
horario_bmga_entre_semana = "De 6am a 8pm"
regla_bmga_entre_semana = {
  1: "3 y 4", #Lunes
  2: "5 y 6", #Martes
  3: "7 y 8", #Miercoles
  4: "9 y 0", #Jueves
  5: "1 y 2"} #Viernes
print(regla_bmga_entre_semana[2])
print(fecha_hoy)

horario_bmga_sabado = "De 9am a 1pm"
regla_bmga_sabado = {
  "2022-02-05": "1 y 2",
  "2022-02-12": "3 y 4",
  "2022-02-19": "5 y 6",
  "2022-02-26": "7 y 8",
  "2022-03-05": "9 y 0",
  "2022-03-12": "1 y 2",
  "2022-03-19": "3 y 4",
  "2022-03-26": "5 y 6"
}

# print(regla_bmga_sabado[fecha_hoy_str])

print (fecha_hoy + timedelta(days = 1))

# Enviar pico y placa de Bucaramanga Hoy
# @bot.message_handler(commands=['picoyplacabmgahoy'])
def picoyplacabmgahoy(message):

  if weekday_hoy == 7:
    msj = f'\U0001F6D1 Hola! En Bucaramanga hoy no hay Pico y Placa \n'
  elif weekday_hoy == 6:
    msj = f'\U0001F6D1 Hola! En Bucaramanga hoy tiene Pico y Placa *{regla_bmga_sabado[fecha_hoy_str]}* \n'
  else:
    msj = f'\U0001F6D1 Hola! En Bucaramanga hoy tiene Pico y Placa *{regla_bmga_entre_semana[weekday_hoy]}* \n'
  
  #bot.send_message(message.chat.id, msj)
  print(msj)

picoyplacabmgahoy("j")

# @bot.message_handler(commands=['PingGustavo'])
# def pingGustavo(message):

#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")
#   bot.send_message(message.chat.id, "Ping Gustavo!")

# @bot.message_handler(commands=['CompreGustavo'])
# def compreGustavo(message):

#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")
#   bot.send_message(message.chat.id, "Compre Gustavo!")


# @server.route('/' + API_KEY, methods=['POST'])
# def getMessage():
#     json_string = request.get_data().decode('utf-8')
#     update = telebot.types.Update.de_json(json_string)
#     bot.process_new_updates([update])
#     return "!", 200


# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://telegram-gustavo-bot.herokuapp.com/' + API_KEY)
#     return "!", 200


# if __name__ == "__main__":
    # server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
