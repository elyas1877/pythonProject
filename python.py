import telegram
import telegram.ext.updater
from telegram.ext import Updater , CommandHandler
updat = Updater("225268369:AAGIXSbeXFVi-2Ye0x7md9UmvQV-fLKDy2o",use_context=True)
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="ssssss")


updat.dispatcher.add_handler(CommandHandler('start',start))
updat.dispatcher.add_handler(CommandHandler('help',help))
# updater.Dispatcher.add_handler(CommandHandler('send',reply1))
updat.start_polling()
updat.idle()