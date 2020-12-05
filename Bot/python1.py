import logging
from typing import List, Any
from uuid import uuid4

from req3 import search , Manga
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update, InlineKeyboardMarkup, \
    InlineKeyboardButton
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext, CallbackQueryHandler
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


chats :dict = {}

logger = logging.getLogger(__name__)
def check(update: Update,context: CallbackContext) -> bool:
    # try:
        b=context.bot.get_chat_member(chat_id='@test1877',user_id=update.message.chat.id)
        print(b.status)
        if b.status not in ( 'member','creator','administrator' ):
            update.message.reply_text(text='You Have To Join This Channel',reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                                "Join",url='http://t.me/test1877'

                            )]]))
            return False

        return True
    # except:
    #     print('check')

def check2(update: Update, context: CallbackContext) -> bool:
    # try:
    print(update.inline_query.from_user.id)
    b = context.bot.get_chat_member(chat_id='@test1877', user_id=update.inline_query.from_user.id)
    print(b.status)
    if b.status not in ('member', 'creator', 'administrator'):
        result = [    InlineQueryResultArticle(
            id=uuid4(), title='Please Join The Channel', input_message_content=InputTextMessageContent('Please Join The Channel')
            , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                "Join", url='http://t.me/test1877'

            )]])) ]
        update.inline_query.answer(result)
        return False

    return True


# except:
#     print('check')


def start(update: Update,context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""

    if check(update,context) :
        update.message.reply_text('hi')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

# def echo(update: Update, context: CallbackContext) -> None:
#     """Echo the user message."""
#     print(update.message.text)
#     update.message.reply_text(update.message.text)
def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    # time.sleep(0.5)
    query = update.inline_query.query
    # update.inline_query.answer([])
    if query != '' :
     if check2(update,context):
      a = search(query)
      if a is not None:
        results = []
        for i in search(query):
            s=InlineQueryResultArticle(
                id=i.Id, title=i.Name, input_message_content=InputTextMessageContent(i.Id),thumb_url=i.Image
            ,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                            "Download",callback_data=f'{i.Id_encode}'

                        )]]))
            results.append(s)

        update.inline_query.answer(results)

    else:
        print('empty')
def create(get : list , id : int) -> list:
    list1=[]
    lenth = len(get)
    # lenthBottun = lenth//4
    lenthPage = lenth//25
    op:int = 0
    for i in range(lenthPage):
        list2 = []
        for j in range(10):
            # print('\n\n')
            list3= []
            for k in get[op:op+4]:
                list3.append(k['index'])
                #InlineKeyboardButton(text='chap:{}'.format(k['index']+1), callback_data=k['index'])
                # print(k['title'])
            op+=4
            list2.append(list3)
        list1.append(list2)
        # list1.append([i['title'] for i in get[-(lenthBottun%4):]])
    # list2.clear()
    # print(list1)
    # chats[id] =  list1
    return list1

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    # print()
    keyboard = create(Manga.getChapters(query.data),query.from_user.id)
    print(keyboard)
    # print(keyboard)
    # print(Manga.getChapters(query.data))
    '''
        reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_reply_markup(reply_markup=reply_markup)
    '''
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # print(Manga.getChapters(query.data))
    # query.edit_reply_markup(reply_markup=reply_markup)
    # context.bot.edit_message_reply_markup(chat_id=update,message_id=query.inline_message_id,reply_markup=reply_markup)
    # query.edit_message_text(text=f"Selected option: {query.data}")


def main():

    updater = Updater("225268369:AAGdzjNI9jWrRCz0-7fxXA9nbqAZ4XPo_3k", use_context=True )
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
