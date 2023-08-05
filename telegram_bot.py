import telegram
bot = telegram.Bot(token='6044295717:AAHzgphndfHFiMo_qUz02PJhVISoKlHCu_M')
chat_id = bot.get_updates()[-1].message.chat_id
bot.send_document(chat_id=chat_id, document=open('images/nasa_apod_1.jpg', 'rb'))