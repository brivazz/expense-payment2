from aiogram.utils.markdown import hbold
from database.sqlite_db import all_expenses_month_report


async def all_expenses_month_msg():
    return f"Общие расходы за месяц: \n{hbold(await all_expenses_month_report())} рублей"