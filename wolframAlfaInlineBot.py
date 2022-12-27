# from logging import getLogger
from telegram import InlineQueryResultArticle
from telegram import InlineQueryResultPhoto
from telegram import InputTextMessageContent
from telegram import ReplyKeyboardRemove
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telebot import types

from flask import Flask, request
import requests
import wolframalpha

app = Flask(__name__)

# VARS:
with open('./keys/telegram_token.txt') as file:
    TELEGRAM_TOKEN = file.readline()
with open('./keys/wolfram_key.txt') as file:
    WOLFRAM_KEY = file.readline()


# Ask wolfram API:
def get_wolfram_res(query):
    client = wolframalpha.Client(WOLFRAM_KEY)
    return client.query(query)

# Parse text answer
def get_wolfram_text_answer(res):
    try:
        return next(res.results).text
    except Exception as e:
        return "Wolfram не вернул текст"

# Parse img answers
def get_wolfram_img_answers(res):
    answer_urls = []
    for pod in res.pods:
        for sub in pod.subpods:
            answer_urls.append(sub['img']['@src'])
    return answer_urls


def echo_handler(update: Update, context: CallbackContext):
    if not update.message:
        return
    query = update.message.text
    print("QUERY = \n\n", query)
    if query in ["/help", "\help", "\start", "/start"]:
        answer_text = "Write a command in the walfram language\nFor example:\nintegral from 1 to 5 xdx"
        update.message.reply_text(
            text=f'Перейтиде в любой другой диалог и начните печатать юзернейм бота: @{update.message.bot.username}\nЛибо напишите Ваш вопрос здесь',
            parse_mode='MarkdownV2',
            reply_markup=ReplyKeyboardRemove(),
        )   
    elif len(query) > 0:    
        res = get_wolfram_res(query)
        try:
            answer_text = get_wolfram_text_answer(res)
            update.message.reply_text(
                text=f'`{answer_text}`',
                parse_mode='MarkdownV2',
                reply_markup=ReplyKeyboardRemove(),
            )
        except Exception as e:
            print(e)
            update.message.reply_text(
                text="Wolfram не вернул текст",
                parse_mode='MarkdownV2',
                reply_markup=ReplyKeyboardRemove(),
            )
        answer_img_urls = get_wolfram_img_answers(res)
        answer_types = [types.InputMediaPhoto(url) for url in answer_img_urls]
        update.message.reply_media_group(answer_types)
        

    else:
        answer_text = "Пустой запрос, попрубуй \help"
        update.message.reply_text(
            text=answer_text,
            parse_mode='MarkdownV2',
            reply_markup=ReplyKeyboardRemove(),
        )

    
def inline_handler(update: Update, context: CallbackContext):
    query = update.inline_query.query
    print("QUERY = \n\n", query)
    
    results = []
    res = get_wolfram_res(query)
    text_answer = get_wolfram_text_answer(res)
    results.append(
        InlineQueryResultArticle(
            id=1,
            title=f'`{text_answer}`',
            input_message_content=InputTextMessageContent(
                message_text=f'`{query} = \nanswer:  {text_answer}`',
                parse_mode='MarkdownV2'
            ),
        )
    )

    # Ничего не нашлось
    if query and not results:
        results.append(
            InlineQueryResultArticle(
                id=99999,
                title='Ничего не нашлось',
                input_message_content=InputTextMessageContent(
                    message_text=f'Ничего не нашлось по запросу "{query}"',
                ),
            )
        )

    update.inline_query.answer(
        results=results,
        cache_time=10,
    )

# Создать бота
updater = Updater(
    token = TELEGRAM_TOKEN,
    base_url=f"https://api.telegram.org/bot",
    use_context=True,
)
# Загрузить информацию о боте
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=echo_handler))
updater.dispatcher.add_handler(InlineQueryHandler(inline_handler))

@app.route("/", methods=["GET", "POST"])
def main():
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    app.run()
