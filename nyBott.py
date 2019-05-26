import RPi.GPIO as GPIO
import time
from datetime import datetime
import telepot
from telepot.loop import MessageLoop

ID = 803524468
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)


def motionSensor():
  while True:
    i = GPIO.input(12)
    if i == 1 :
       handle()
       time.sleep(10)

def sendMsg(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == 'ja' :
        ja = 'nu har vi skrämt iväg dom'
        bot.sendMessage(ID, str(ja))
    elif command == 'nej' :
        nej = 'då får dom väl vara där'
        bot.sendMessage(ID, str(nej))
    else:
        bot.sendMessage(chat_id, 'dont know this command :'+command)


def handle():
    tiden = 'Nu rör det sig någon hemma'
    val = 'Vill du varna polisen? ja/nej'
    bot.sendMessage(ID, str(tiden))
    time.sleep(1)
    bot.sendMessage(ID, str(val))

bot = telepot.Bot('826949653:AAEoJg3_IyqnwBNzbPn55SXnyV81YACD1RY')
MessageLoop(bot, sendMsg).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(3)
    motionSensor()
#    handle()
