import telebot
from config import keys, TOCKEN
from extensions import MyConverter, APIException

# Имя Бота:
# CryptoBot
# CryptoStudyMyBot

bot = telebot.TeleBot(TOCKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Введите: \n<название валюты> \ <в какую перевести> \ <сумма переводимой валюты>\n Список досупных валют комманда: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def values(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров')

        qoute, base, amount = values

        total_base = MyConverter.get_price(qoute, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка ввода\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {qoute} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()


