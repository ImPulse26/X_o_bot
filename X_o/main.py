from asyncio import sleep

from aiogram import executor
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher
from aiogram.utils.callback_data import CallbackData

from KeyBoardButton import*

player = ''
bot = ''
win_list = []
table_dict = {}
counter = 0
token = ""

action_callback = CallbackData("move", "item_name")

bot = Bot('5745492836:AAGmG7RFfZ1DN8nr1WCbDUgDRyIkkfBV1Aw')
dp = Dispatcher(bot)


@dp.message_handler(Command("start"))
async def show_field(message: Message):
    global table_dict, counter

    table_dict = {i: k for i, k in zip(range(1, 10), "123456789")}
    counter = 0
    await message.answer(text="Выберите сторону",
                         reply_markup=choice_xo)


@dp.callback_query_handler(action_callback.filter(item_name=["X", "O"]))
async def choice_sign(call: CallbackQuery, callback_data: dict):
    global player, bot, token
    await call.answer(cache_time=10)
    player = callback_data["item_name"]
    token = player
    await call.message.answer(text="Выберите номер",
                              reply_markup=fun_choice(table_dict))
    await sleep(3)


@dp.callback_query_handler(action_callback.filter(item_name=["1", "2", "3", "4", "5", "6", "7", "8", "9"]))
async def nums_choice(call: CallbackQuery, callback_data: dict):
    global table_dict, counter, token

    counter += 1
    text = "Ходит игрок"
    data = callback_data["item_name"]

    answer = place_sign(token, data, table_dict)
    if not isinstance(answer, str):
        table_dict = answer
        token = "O" if token == "X" else "X"
    else:
        text = answer

    await call.answer(cache_time=1)

    await call.message.edit_text(f"{text} {token}",
                                 reply_markup=fun_choice(table_dict))
    if counter > 3:
        if check_win(table_dict):
            await call.message.edit_text(
                f"{check_win(table_dict)} - WIN!",
                reply_markup=fun_choice(table_dict))
            await restart(call)

    if counter == 9:
        await call.message.edit_text("Ничья!",
                                     reply_markup=fun_choice(table_dict))
        await restart(call)


async def restart(call):
    await show_field(call.message)
    await sleep(3)


def place_sign(token, data, table_dict):
    data = int(data)
    pos = table_dict[data]
    if pos not in (chr(128581), chr(128582)):
        table_dict[data] = chr(128581) if token == "X" else chr(128582)
        return table_dict
    return "Данная позиция уже занята!"


def check_win(table_dict):
    win_coord = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                 (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))

    n = [table_dict[x[0]] for x in win_coord if table_dict[x[0]]
         == table_dict[x[1]] == table_dict[x[2]]]
    return n[0] if n else n


if __name__ == "__main__":
    executor.start_polling(dp)