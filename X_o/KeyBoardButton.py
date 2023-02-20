from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def fun_choice(table_dict):
    choice = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=table_dict[1], callback_data="move:1"),
                InlineKeyboardButton(
                    text=table_dict[2], callback_data="move:2"),
                InlineKeyboardButton(
                    text=table_dict[3], callback_data="move:3"),
            ],
            [
                InlineKeyboardButton(
                    text=table_dict[4], callback_data="move:4"),
                InlineKeyboardButton(
                    text=table_dict[5], callback_data="move:5"),
                InlineKeyboardButton(
                    text=table_dict[6], callback_data="move:6"),
            ],
            [
                InlineKeyboardButton(
                    text=table_dict[7], callback_data="move:7"),
                InlineKeyboardButton(
                    text=table_dict[8], callback_data="move:8"),
                InlineKeyboardButton(
                    text=table_dict[9], callback_data="move:9"),
            ],
        ]
    )

    return choice


choice_xo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="X", callback_data="move:X"),
            InlineKeyboardButton(text="O", callback_data="move:O"),
        ],
    ]
)