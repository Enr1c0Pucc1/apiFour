import telegram
bot = telegram.Bot(token='6044295717:AAHzgphndfHFiMo_qUz02PJhVISoKlHCu_M')
chat_id = bot.get_updates()[-1].message.chat_id
bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")