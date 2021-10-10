import asyncio
from typing import Text
from states import Form
from requer import Requer
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup as km, InlineKeyboardButton as kb, ReplyKeyboardMarkup as rm, KeyboardButton as btn, ReplyKeyboardRemove as rem

# Словарь ответов
trust = {'start' : "START!", '/hello_world' : "HeLLWorD!"*3}

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

# START #
async def startpars(dp, mes):
    #await msg.answer(f'Привет, чего хотел?')
    await Form.city.set()
    await mes.answer('введите город')
    @dp.message_handler(state=Form.city)
    async def echo_mes(msg, state: FSMContext):
        if Requer(msg.text).set:
            await msg.answer(msg.text.title(), reply_markup=get_keyboard())
        else:
            await msg.reply('не принято')
        await state.finish()

# HELP #
async def help(mes):
    #await mes.answer(f'Привет, чем помочь?')
    text = """
    <b>
    Список команд:                 
    /start       - Начать диалог   
    /help        - Получить справку
    /form        - Ввод данных     
    /cancel      - Сброс           
    /hello_world - Тест            
    </b>"""
    await mes.answer(text, parse_mode="HTML")

# CANSEL #
async def cansel(mes, state):
    await mes.answer('Canceled.', reply_markup=rem())
    await state.finish()

# OTHER COM #
async def command(dp, mes):
    ms, user = mes.text.lower(), mes.from_user.full_name
    if ms in trust:
        await edprint(dp, mes, trust[ms])
    elif any(ms.startswith(w) for w in ['hi', 'hey', 'hello']):
        await edprint(dp, mes, f"Hello, {user}!")
    elif any(w in ms for w in ['прив', 'здрав', 'здрас', 'здоров', 'добр']):
        await edprint(dp, mes, f"Привет, {user}!")
    else:
        await mes.answer("Привет!\nНапиши мне что-нибудь!")

# print message(edit)#10.10.21
async def edprint(d, mes, ans):
    mid = await mes.answer('*')
    for i in range(1, len(ans.split()[0])):
        await d.bot.edit_message_text(ans[:i], chat_id=mid.chat.id, message_id=mid.message_id)
    await d.bot.edit_message_text(ans, chat_id=mid.chat.id, message_id=mid.message_id)


async def callback(bot, query):
    await bot.answer_callback_query(query.id)
    await bot.send_message(query.from_user.id, f'Нажата кнопка {query.data}!')