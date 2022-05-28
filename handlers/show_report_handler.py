from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.create_bot import dp, bot
from messages.show_report_btn_message import show_report_btn_msg
from keyboards.show_report_btn_keyboard import show_report_btn_menu


@dp.callback_query_handler(text='show_report_btn')
async def show_report(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await show_report_btn_msg(),
        reply_markup=await show_report_btn_menu()
    )
