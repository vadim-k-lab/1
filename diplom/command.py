import asyncio
from typing import Text
from requer import Requer
from aiogram.types import InlineKeyboardMarkup as km, InlineKeyboardButton as kb, ReplyKeyboardMarkup as rm, KeyboardButton as btn, reply_keyboard

# Словарь ответов
trust = {'start' : "<i><b>START</b>!</i>", '/hello_world' : "<b>HeLLWorD!</b>"}

# Генерация клавиатуры.
def get_keyboard():
    but = [
        kb(text="1", callback_data="1"),
        kb(text="2", callback_data="2"),
        kb(text="3", callback_data="3"),
        kb(text="4", callback_data="4")
    ]
    return km(row_width=2).add(*but)

def get_btn():
    return rm(resize_keyboard=True).add(btn('Привет! 👋'), btn('Выбор'))


async def startpars(dp, mes):
    await mes.answer('введите город')
    @dp.message_handler()
    async def echo_message(msg):
        if Requer(msg.text).set:
            await msg.reply(msg.text.title(), reply_markup=get_keyboard())
        else:
            await msg.reply('не принято')


async def command(dp, mes):
    if mes.text in trust:
        await mes.answer(trust[mes.text], parse_mode="HTML")
    else:
        await mes.answer("Привет!\nНапиши мне что-нибудь!")


async def callback(bot, query):
    await bot.answer_callback_query(query.id)
    await bot.send_message(query.from_user.id, f'Нажата кнопка {query.data}!')