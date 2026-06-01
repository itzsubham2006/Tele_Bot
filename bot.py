import telebot


TOKEN = '8957160334:AAHyX_D5GTnheqwkqwzGJmoXGwDo3l_SaYU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, 'Welcome to Telegro_Bot, this bot is created by Subham')

@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message, 
                 """
                /start ->  Greetings
                /help -> It will give u all command  
                 
                 """                 
                 )
    


bot.polling()