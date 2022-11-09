from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import logging


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO, filename="bot_log.txt")
logger = logging.getLogger(__name__)


async def hello(update: Update, context: CallbackContext):
    await update.message.reply_text(f'''Привет, {update.effective_user.first_name}. Добро пожаловать в калькулятор!
    Чтобы узнать, как пользоваться калькулятором, нажми {'/menu'}
    ''')


async def menu(update: Update, context: CallbackContext):
    await update.message.reply_text(f'''    
        /hello - Стартовая страница
        Чтобы сложить два числа набери /add, затем числа для сложения, например /add 10 12
        Чтобы вычесть из одного числа другое набери /sub, затем числа для вычитания, например /sub 10 12
        Чтобы умножить два числа набери /mult, затем числа для умножения, например /mult 10 12
        Чтобы разделить два числа набери /div, затем числа для деления, например /div 10 12
    ''')


async def add(update: Update, context: CallbackContext):
    msg = update.message.text.split()
    if len(msg) == 3:
        num1 = float(msg[1])
        num2 = float(msg[2])
        await update.message.reply_text(
            f'{num1} + {num2} = {num1 + num2}')
    else:
        msg = [
            'Некорректный ввод']
        await update.message.reply_text(
            '\n'.join(msg))


async def sub(update: Update, context: CallbackContext):
    msg = update.message.text.split()
    if len(msg) == 3:
        num1 = float(msg[1])
        num2 = float(msg[2])
        await update.message.reply_text(
            f'{num1} - {num2} = {num1 - num2}')
    else:
        msg = [
            'Некорректный ввод']
        await update.message.reply_text(
            '\n'.join(msg))


async def mult(update: Update, context: CallbackContext):
    msg = update.message.text.split()
    if len(msg) == 3:
        num1 = float(msg[1])
        num2 = float(msg[2])
        await update.message.reply_text(
            f'{num1} * {num2} = {num1 * num2}')
    else:
        msg = [
            'Некорректный ввод']
        await update.message.reply_text(
            '\n'.join(msg))


async def div(update: Update, context: CallbackContext):
    msg = update.message.text.split()
    if len(msg) == 3:
        num1 = float(msg[1])
        num2 = float(msg[2])
        await update.message.reply_text(
            f'{num1} / {num2} = {num1 / num2}')
    else:
        msg = [
            'Некорректный ввод']
        await update.message.reply_text(
            '\n'.join(msg))


app = ApplicationBuilder().token('').build()

print('Start')

app.add_handler(CommandHandler('menu', menu))
app.add_handler(CommandHandler('hello', hello))
app.add_handler(CommandHandler('add', add))
app.add_handler(CommandHandler('sub', sub))
app.add_handler(CommandHandler('div', div))
app.add_handler(CommandHandler('mult', mult))

app.run_polling()
