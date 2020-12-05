#
# from pyrogram import Client, filters
#
# app = Client(session_name="my_bot",api_id=2819335,api_hash='5f3cfaf0cd57f5873086ae3fa6ef86b5',proxy={
#         'hostname':"127.0.0.1",
#         'port':1080,
#         'username':"",
#         'password':"x23Z4LGkGDkThZ9Kaz4DURQp"
# }, bot_token="225268369:AAGdzjNI9jWrRCz0-7fxXA9nbqAZ4XPo_3k")
# #, bot_token="225268369:AAGdzjNI9jWrRCz0-7fxXA9nbqAZ4XPo_3k"
# @app.on_message(filters.text)
# def caller(client,message):
#     # Send a message, Markdown is enabled by default
#     print(message.text)
#     app.send_message(chat_id=message.chat.id,text=message.message_id)
#     app.send_message(chat_id=message.chat.id, text=app.get_me())
#     # app.send_photo(chat_id=message.chat.id,photo='0001-001.png')
#
# # @app.on_message(filters.text & filters.private)
# # def echo(client, message):
# #     print(message.text)
# #     message.reply_text(message.text)
# #
# # @app.on_callback_query()
# # def answer(client, callback_query):
# #     callback_query.answer(f"Button contains: '{callback_query.data}'", show_alert=True)
#
#
# app.run()
import time
from pyrogram import Client, filters
app = Client(session_name="my_bot",api_id=2819335,api_hash='5f3cfaf0cd57f5873086ae3fa6ef86b5')

'''
,proxy={
        'hostname':"127.0.0.1",
        'port':1080,
        'username':"",
        'password':"x23Z4LGkGDkThZ9Kaz4DURQp"
}

'''
@app.on_message(filters.text)
def caller(client : Client,message):
    # Send a message, Markdown is enabled by default
    print(message.text)
    app.send_message(chat_id=message.chat.id,text=message.message_id)

    def progress(current, total):
        print(f"{current * 100 / total:.1f}%")
    app.send_document(message.chat.id,'C:\\Users\\Elyas\\PycharmProjects\\pythonProject\\0001-001.png',caption='Page 1',progress=progress)
    # app.send_message(chat_id=message.chat.id, text=app.get_me())
    # app.send_photo(chat_id=message.chat.id,photo='0001-001.png')


    #app.send_message(chat_id='117422903', text=search(int(message.text)),reply_to_message_id=message.message_id)
    time.sleep(1)

app.run()