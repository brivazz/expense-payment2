from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from utils.create_bot import dp, bot
from utils.config import MY_ID
from messages.start_message import start_msg
from keyboards.start_keyboard import start_menu_kb


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    if MY_ID:
        await bot.delete_message(
            chat_id=message.from_user.id,
            message_id=message.message_id
        )
        await message.answer(
            text=await start_msg(message.from_user.full_name),
            reply_markup=await start_menu_kb()
        )
