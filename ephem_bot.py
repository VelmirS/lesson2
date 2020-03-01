"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import ephem
import logging
import settings 


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def planet_name(bot, update):  # Отдаем команды боту
    if str(update.message.text).split()[1]:
        planet = str(update.message.text).split()[1].capitalize()
        today_date = datetime.today().strftime('%Y/%m/%d')
        request_to_ephem = f"ephem.{planet}('{today_date}')"
        planet_info = ephem.constellation(eval(request_to_ephem))
        update.message.reply_text("Сегодня {} в созвезддии: {}".format(planet, planet_info[1]))

def talk_to_me(bot, update): 
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

    # Логи
    logging.info("User: %s, Chat id: %s, Message: %s",
                 update.message.chat.username,
                 update.message.chat.id,
                 update.message.text)

    update.message.reply_text(user_text)


# "тело" нашего бота
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info("Бот запускается")
    dp = mybot.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_name))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()  