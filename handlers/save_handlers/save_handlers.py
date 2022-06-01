from aiogram.utils.markdown import hbold
from aiogram import types
from aiogram.utils.exceptions import MessageToDeleteNotFound

from utils.create_bot import dp, bot
from database.sqlite_db import save_to_db

from messages.save_messages.save_message import save_msg
from messages.start_message import start_msg

from keyboards.save_keyboards.save_keyboard import save_menu
from keyboards.start_keyboard import start_menu_kb
from keyboards.save_keyboards.replay_keyboard import replay_menu


@dp.callback_query_handler(text=['products_btn',
                                 'tabak_btn',
                                 'alcohol_btn',
                                 'clothing_and_shoes',
                                 'mob_tel_btn',
                                 'travel_btn',
                                 'rent_commun_payments_btn',
                                 'leisure_btn',
                                 'kindergarten_btn',
                                 'other_payments_btn',
                                 'my_zp_btn',
                                 'my_love_zp_btn',
                                 'parents_btn',
                                 'show_report_btn'])
async def question(call: types.CallbackQuery):
    await call.answer()

    global call_message_id
    call_message_id = call.message.message_id

    global button_text
    if call.data == 'products_btn':
        button_text = call.message.reply_markup.inline_keyboard[0][0].text
    elif call.data == 'tabak_btn':
        button_text = call.message.reply_markup.inline_keyboard[0][1].text
    elif call.data == 'alcohol_btn':
        button_text = call.message.reply_markup.inline_keyboard[0][2].text
    elif call.data == 'clothing_and_shoes':
        button_text = call.message.reply_markup.inline_keyboard[1][0].text
    elif call.data == 'kindergarten_btn':
        button_text = call.message.reply_markup.inline_keyboard[1][1].text
    elif call.data == 'travel_btn':
        button_text = call.message.reply_markup.inline_keyboard[2][0].text
    elif call.data == 'mob_tel_btn':
        button_text = call.message.reply_markup.inline_keyboard[2][1].text
    elif call.data == 'leisure_btn':
        button_text = call.message.reply_markup.inline_keyboard[2][2].text
    elif call.data == 'rent_commun_payments_btn':
        button_text = call.message.reply_markup.inline_keyboard[3][0].text
    elif call.data == 'other_payments_btn':
        button_text = call.message.reply_markup.inline_keyboard[3][1].text
    elif call.data == 'my_zp_btn':
        button_text = call.message.reply_markup.inline_keyboard[4][0].text
    elif call.data == 'parents_btn':
        button_text = call.message.reply_markup.inline_keyboard[4][1].text
    elif call.data == 'my_love_zp_btn':
        button_text = call.message.reply_markup.inline_keyboard[4][2].text
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await save_msg(),
        reply_markup=''
    )


@dp.callback_query_handler(text=['save_btn',
                                 'cancel_btn',
                                 'cancel_enter_btn'])
async def save_cancel_button(call: types.CallbackQuery):
    if call.data == 'save_btn':
        await save_to_db(button_text, amount)
        await call.answer('Сохранено', show_alert=True)
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=await start_msg(call.from_user.full_name),
            reply_markup=await start_menu_kb()
        )
    elif call.data in ['cancel_btn', 'cancel_enter_btn']:
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=await start_msg(call.from_user.full_name),
            reply_markup=await start_menu_kb()
        )


@dp.callback_query_handler(text=['replay_btn'])
async def replay_cancel_button(call: types.CallbackQuery):
    if call.data == 'replay_btn':
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=await save_msg(),
            reply_markup=''
        )
        global call_msg
        call_msg = call.message.message_id


@dp.message_handler()
async def read_message(message: types.Message):
    try:
        await bot.delete_message(message_id=call_message_id,
                                 chat_id=message.from_user.id)
    except MessageToDeleteNotFound:
        await bot.delete_message(message_id=call_msg,
                                 chat_id=message.from_user.id)
    msg_id = message.message_id
    await bot.delete_message(message_id=msg_id,
                             chat_id=message.from_user.id)
    text = message.text
    if text.isdigit():
        global amount
        amount = text
        await bot.send_message(
            text=f'Записать сумму:\n{hbold(text)} руб.?',
            chat_id=message.from_user.id,
            reply_markup=await save_menu()
        )
    else:
        await message.answer('Надо писать цифры!',
                             reply_markup=await replay_menu())
