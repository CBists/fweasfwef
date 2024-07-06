import telebot

bot = telebot.TeleBot('7492688667:AAFaL7HGQO7gz2jjUJGv-0vNvdcuCSAnkVU')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
