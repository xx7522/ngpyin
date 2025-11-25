import logging
import telegram
from telegram.ext import Updater, MessageHandler, Filters
import openai
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

openai.api_key = OPENAI_KEY

def reply(update, context):
    user_text = update.message.text

    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_text}]
    )

    response = completion["choices"][0]["message"]["content"]
    update.message.reply_text(response)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
