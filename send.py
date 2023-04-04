import telepot

def sendpicture(message,image):
    bot = telepot.Bot('5981392455:AAHbYGVYJ1P9XntMvDfPDWzVbrRd-Lb7jJs')
    bot.sendPhoto(5053711674, photo=open(image, 'rb'))
    bot.sendMessage(5053711674, message)