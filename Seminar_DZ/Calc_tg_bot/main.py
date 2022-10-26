'''
Задача: 
Создать калькулятор для работы с рациональными и комплексными числами,
организовать меню, добавив в неё систему логирования. Привязать к нему TG Bot.
'''
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
import calk_complex
import calk_float
import logger

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я Бот калькулятор)")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(
    'Для работы калькулятора, введите выражение в формате (пробелы обязательны!)\n/calc 2 + 2'
    )
  
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, такой команды нет(")
  
async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
  msge = update.message.text
  #print(msge)
  items = msge.split() # /calc 10 (+,-,*,/) 6
  a = items[1]
  b = items[3]
  operation = items[2]
  if 'j' in a and 'j' in b:
    result = calk_complex.calc(a, b, operation)
  else:
    result = calk_float.calc(a, b, operation)
  #print(f'Результат = {result}')
  await update.message.reply_text(f'Результат = {result}')
  logger.log_to_file(a, b, operation, result)
  return result
    
if __name__ == '__main__':
    application = ApplicationBuilder().token('5633157833:AAHPma1xc5pNT6JpP-PVT9TJxiHFhBkAOZc').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)
    
    help_handler = CommandHandler('calc', calc)
    application.add_handler(help_handler)
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)
    
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    
    print('start bot')
    
    application.run_polling()
