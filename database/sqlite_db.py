import datetime
from .models import db, Expense, Payment


async def now_month():
    month_list = ['Январь', 'Февраль', 'Март',
                  'Апрель', 'Май', 'Июнь',
                  'Июль', 'Август', 'Сентябрь',
                  'Октябрь', 'Ноябрь', 'Декабрь']
    now_month = datetime.date.today()
    return month_list[now_month.month - 1]


async def now_year():
    now_date = datetime.date.today()
    return now_date.year


async def save_to_db(button_text, amount):
    with db.atomic():
        query = Expense.get(Expense.product_name == button_text)
        Payment.create(
            amount=int(amount),
            expense_id=query
        )


async def all_time_all_expenses_report_db():
    with db:
        result = Payment.select().where(
                    (Payment.expense_id != 11) &
                    (Payment.expense_id != 12) &
                    (Payment.expense_id != 13))
        count = 0
        for res in result:
            count += res.amount
    return count


async def all_expenses_month_report_db():
    date_now = datetime.date.today()
    count = 0
    with db:
        data = Payment.select().where(
                (Payment.payment_date.month == date_now.month) &
                (Payment.expense_id != 11) &
                (Payment.expense_id != 12) &
                (Payment.expense_id != 13))
        for d in data:
            count += d.amount
    return count


async def show_report_in_this_month_db(category_text):
    now_month = datetime.date.today()
    count = 0
    with db:
        query = Expense.get(Expense.product_name == category_text)
        date = Payment.select().where(
                (Payment.expense_id == query) &
                (Payment.payment_date.month == now_month.month))
        for d in date:
            count += d.amount
    return count


async def show_report_for_the_year_db(category_text):
    now_year = datetime.date.today()
    count = 0
    with db:
        query = Expense.get(Expense.product_name == category_text)
        data = Payment.select().where(
                (Payment.expense_id == query) &
                (Payment.payment_date.year == now_year.year))
        for d in data:
            count += d.amount

    return count


async def show_report_by_months_db(category_text):
    now_date = datetime.date.today()
    month_name = {'Январь': 1, 'Февраль': 2, 'Март': 3,
                  'Апрель': 4, 'Май': 5, 'Июнь': 6,
                  'Июль': 7, 'Август': 8, 'Сентябрь': 9,
                  'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}
    months_list = []
    with db:
        query = Expense.get(Expense.product_name == category_text)
        for k, v in month_name.items():
            if v > now_date.month:
                break
            count = 0
            data = Payment.select().where(
                    (Payment.expense_id == query) &
                    (Payment.payment_date.month == v) &
                    (Payment.payment_date.year == now_date.year))

            for d in data:
                count += d.amount
            month_dict = {
                f"{k}": count
            }
            months_list.append(month_dict)
    return months_list
