import requests
import telebot

# Hotels_bot
# My_Hotels_svu_bot
token = '1872028385:AAFJhyMlecp2Q34gmF45Ko84hMKPhTO7fX4'



bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['text'])
def get_text_messages(massage):
    if massage.text == '/help':
        bot.send_message(massage.from_user.id, '/lowprice — вывод самых дешёвых отелей в городе\n'
                                               '/highprice — вывод самых дорогих отелей в городе\n'
                                               '/bestdeal — вывод отелей, наиболее подходящих по цене и расположению от центра.')
    elif massage.text == '/lowprice':
        bot.send_message(massage.from_user.id, 'requests запрос на Hotels самых дорогих отелей в городе')
    elif massage.text == '/highprice':
        bot.send_message(massage.from_user.id, 'requests запрос на Hotels самых дешёвых отелей в городе')
    elif massage.text == '/bestdeal':
        bot.send_message(massage.from_user.id, 'requests запрос на Hotels наиболее подходящих по цене и расположению от центра')
    else:
        bot.send_message(massage.from_user.id,'Я не понимаю. Напиши /help.')

bot.polling(none_stop=True,interval=0)
