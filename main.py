import telebot

bot = telebot.TeleBot('6234356715:AAGoJHgtA4D3z8IcdYTpMwaVxHh9ra0z73E')


@bot.message_handler(commands=['start'])
def main(msg):
    bot.send_message(msg.chat.id, f'Hello, {msg.from_user.first_name}!')


@bot.message_handler()
def repeat(msg):
    bot.send_message(msg.chat.id, msg.text)


bot.polling(none_stop=True)
