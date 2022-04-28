import os
import telebot
import random
from flask import Flask, request
from datetime import datetime, date, timedelta
import pytz

API_KEY = os.environ.get("API_KEY")
bot = telebot.TeleBot(token=API_KEY, parse_mode="MARKDOWN")
server = Flask(__name__)

#Inicializar variables globales
local_date = datetime.now(pytz.timezone('America/Bogota'))  # use datetime here
fecha_hoy = local_date.date()                                       # now call date method
fecha_hoy_str = str(fecha_hoy)
weekday_hoy = fecha_hoy.isoweekday()  #Monday is 1 and Sunday is 7
day_hoy = fecha_hoy.day

#Pico y placa actual Bucaramanga
horario_bmga_entre_semana = "De 6am a 8pm"
regla_bmga_entre_semana = {
  1: "5 y 6", #Lunes
  2: "7 y 8", #Martes
  3: "9 y 0", #Miercoles
  4: "1 y 2", #Jueves
  5: "3 y 4"} #Viernes

horario_bmga_sabado = "De 9am a 1pm"
regla_bmga_sabado = {
  "2022-04-16": "1 y 2",
  "2022-04-23": "3 y 4",
  "2022-04-30": "5 y 6",
  "2022-05-07": "7 y 8",
  "2022-05-14": "9 y 0",
  "2022-05-21": "1 y 2",
  "2022-05-28": "3 y 4",
  "2022-06-04": "5 y 6",
  "2022-06-11": "7 y 8",
  "2022-06-18": "9 y 0",
  "2022-06-25": "1 y 2"
}

#Pico y placa actual Bogota
horario_bog_entre_semana = "De 6am a 9pm"

#print (fecha_hoy + timedelta(days = 1))

# Enviar pico y placa de Bucaramanga Hoy
@bot.message_handler(commands=['picoyplacabmgahoy'])
def picoyplacabmgahoy(message):

  if weekday_hoy == 7:    #Domingo
    msj = f'\U0001F6D1 Hola! En Bucaramanga hoy no hay Pico y Placa \n'
  elif weekday_hoy == 6:  #Sabado
    msj = f'\U0001F6D1 Hola! En Bucaramanga hoy tiene Pico y Placa *{regla_bmga_sabado[fecha_hoy_str]}* \n Horario: {horario_bmga_sabado}'
  else:                   #Entre semana
    msj = f'\U0001F6D1 Hola! En Bucaramanga hoy tiene Pico y Placa *{regla_bmga_entre_semana[weekday_hoy]}* \n Horario: {horario_bmga_entre_semana}'
  
  bot.send_message(message.chat.id, msj)

# Enviar pico y placa de Bogota Hoy
@bot.message_handler(commands=['picoyplacaboghoy'])
def picoyplacaboghoy(message):

  if weekday_hoy == 7:    #Domingo
    msj = f'\U0001F6D1 Hola! En Bogotá hoy no hay Pico y Placa \n'
  elif weekday_hoy == 6:  #Sabado
    msj = f'\U0001F6D1 Hola! En Bogotá hoy no hay Pico y Placa \n'
  else:                   #Entre semana
    if (day_hoy % 2) == 0:      #Dia par
      msj = f'\U0001F6D1 Hola! En Bogotá hoy tiene Pico y Placa los *pares* \n Horario: {horario_bog_entre_semana}'
    else:                   #Dia impar
      msj = f'\U0001F6D1 Hola! En Bogotá hoy tiene Pico y Placa los *impares* \n Horario: {horario_bog_entre_semana}'
  
  bot.send_message(message.chat.id, msj)

@server.route('/' + API_KEY, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegram-picoyplaca-bot.herokuapp.com/' + API_KEY)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
