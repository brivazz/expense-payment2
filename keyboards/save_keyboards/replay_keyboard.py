from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def replay_menu():
    replay_kb = InlineKeyboardMarkup(row_width=1)

    replay_btn = InlineKeyboardButton(text='Повторить ввод', callback_data='replay_btn')
    cancel_btn = InlineKeyboardButton(text='Отменить ввод', callback_data='cancel_enter_btn')

    replay_kb.add(replay_btn, cancel_btn)

    return replay_kb
