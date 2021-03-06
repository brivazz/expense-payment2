from aiogram.utils.markdown import hbold
from database.sqlite_db import (all_time_all_expenses_report_db,
                                all_expenses_month_report_db,
                                now_month)


async def show_report_all_expenses_btn_msg(data):
    if data == 'show_all_month_expenses_btn':
        return f"Общие расходы за {await now_month()}:\n{hbold(await all_expenses_month_report_db())} руб."
    elif data == 'show_all_time_all_expenses_btn':
        return f"Общие расходы за все время:\n{hbold(await all_time_all_expenses_report_db())} руб."
