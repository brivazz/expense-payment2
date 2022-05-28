from aiogram.utils.markdown import hbold
from database.sqlite_db import all_time_all_expenses_report


async def all_time_all_expenses_msg():
    return f"Общие расходы за все время: \n{hbold(await all_time_all_expenses_report())} рублей"
