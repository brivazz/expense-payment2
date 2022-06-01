from aiogram.utils.markdown import hbold
from database.sqlite_db import (show_report_in_this_month_db,
                                show_report_by_months_db,
                                show_report_for_the_year_db,
                                now_month, now_year)


async def show_report_in_by_for_btn_msg(data, category_text):
    if data == 'show_report_in_this_month_btn':
        return f"=== {category_text} ===\n\n{await now_month()}: {hbold(await show_report_in_this_month_db(category_text))} руб."

    elif data == 'show_report_for_the_year_btn':
        return f"=== {category_text} ===\n\n{await now_year()}: {hbold(await show_report_for_the_year_db(category_text))} руб."

    elif data == 'show_report_by_months_btn':
        result: list = await show_report_by_months_db(category_text)
        message = ''
        for item in result:
            for k, v in item.items():
                message += f"{k}: {hbold(v)} р.\n"
        return f"=== {category_text} ===\n\n___{await now_year()}___\n{message}"
