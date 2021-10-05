from requer import Requer
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup as km, InlineKeyboardButton as kb, ReplyKeyboardMarkup as rm, KeyboardButton as btn

# Словарь ответов
trust = {'start' : "<i><b>START</b>!</i>", '/hello_world' : "<b>HeLLWorD!</b>"}

class Form(StatesGroup):
    city = State()

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

# START
async def startpars(dp, mes):
    await Form.city.set()
    await mes.answer('введите город')
    @dp.message_handler(state=Form.city)
    async def echo_mes(msg, state: FSMContext):
        if Requer(msg.text).set:
            await msg.answer(msg.text.title(), reply_markup=get_keyboard())
        else:
            await msg.reply('не принято')
        await state.finish()

async def command(dp, mes):
    if mes.text in trust:
        await mes.answer(trust[mes.text], parse_mode="HTML")
    else:
        await mes.answer("Привет!\nНапиши мне что-нибудь!")


async def callback(bot, query):
    await bot.answer_callback_query(query.id)
    await bot.send_message(query.from_user.id, f'Нажата кнопка {query.data}!')