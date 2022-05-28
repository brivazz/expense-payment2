import datetime
from peewee import IntegrityError
from peewee import (SqliteDatabase, Model,
                    CharField, DateField,
                    IntegerField, ForeignKeyField)


db = SqliteDatabase('expense_payments.db')


class BaseModel(Model):
    class Meta:
        database = db


class Expense(BaseModel):
    product_name = CharField(max_length=50, unique=True)

    class Meta:
        table_name = 'expenses'


class Payment(BaseModel):
    amount = IntegerField()
    payment_date = DateField(default=datetime.date.today())
    expense_id = ForeignKeyField(Expense)

    class Meta:
        table_name = 'payments'


async def create_tables():
    with db:
        db.create_tables([Expense, Payment])


async def fields_expense():
    fields_expense = [
        {'product_name': 'Продукты'},
        {'product_name': 'Табак'},
        {'product_name': 'Алкоголь'},
        {'product_name': 'Одежда и обувь'},
        {'product_name': 'Детский сад'},
        {'product_name': 'Проезд'},
        {'product_name': 'Моб.связь'},
        {'product_name': 'Досуг'},
        {'product_name': 'Аренда и ком.платежи'},
        {'product_name': 'Другие расходы'},
        {'product_name': 'Моя ЗП'},
        {'product_name': 'Родители'},
        {'product_name': 'Любимая ЗП'},
    ]
    with db:
        try:
            Expense.insert(fields_expense).execute()
        except IntegrityError:
            pass
