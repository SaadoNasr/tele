from telegram.ext import Updater ,CommandHandler


updater=Updater(token='1705244162:AAHk9lExIZrd4oEgd6oDH50QWyBVSsaEBh8')
dispatcher=updater.dispatcher
def start(bot,update):
    bot.sendMessage(chat_id=update.Message.chat_id,text='welcom to cute bot')
    start_handler=CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()
