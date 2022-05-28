import datetime
from .models import db, Expense, Payment


async def save_to_db(call):
    with db.atomic():
        query = Expense.get(Expense.product_name == call.message.text)
        Payment.create(
            amount=int(
                call['message']['reply_markup']['inline_keyboard'][0][1]['text']),
            expense_id=query
        )


async def all_time_all_expenses_report():
    with db:
        result = Payment.select()
        count = 0
        for res in result:
            count += res.amount
    return count


async def show_month(call):
    month = datetime.date.today()
    now_month = str(month).split('-')[1]
    count = 0
    with db:
        query = Expense.get(Expense.product_name == call.message.text)
        date = Payment.select().where(Payment.expense_id == query)
        for d in date:
            num = str(d.payment_date).split('-')[1]
            if num == now_month:
                count += d.amount
    return count


async def show_all(call):
    with db:
        query = Expense.get(Expense.product_name == call.message.text)
        result = Payment.select().where(Payment.expense_id == query)
        count = 0
        for res in result:
            count += res.amount
    return count
