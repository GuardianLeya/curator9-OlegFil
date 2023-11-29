import telebot
bot = telebot.TeleBot('6381926961:AAF-Kke6BEg8x0_uhzohzi5jz4S2MwF56V8')

#1
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Сообщение')

#2
@bot.message_handler(commands=['run!'])
def main(message):
    bot.send_message(message.chat.id, '*Беги!*', parse_mode='Markdown')    

#3
@bot.message_handler(commands=['run!!'])
def main(message):
    bot.send_message(message.chat.id, 'Беги! \nБеги!')

#4
@bot.message_handler(commands=['run!!!'])
def main(message):
    bot.send_message(message.chat.id, 'Беги! \nБеги! \nБеги!')    

#5
@bot.message_handler(commands=['stop'])
def main(message):
    bot.send_message(message.chat.id, 'СТОЙ!')

#6
@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'На ссылку [ТЫЦ!](https://pastebin.com/)', parse_mode='Markdown')

bot.infinity_polling()