from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_contracts(contracts):
    for contract in contracts:
        message = f"📄 {contract['title']}\n🔗 {contract['link']}"
        bot.send_message(chat_id=CHAT_ID, text=message)
