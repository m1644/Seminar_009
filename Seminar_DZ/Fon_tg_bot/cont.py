
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я Бот БАЛАБОЛ)")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text('Пиши чего хочешь.. Удачи...)')
  
'''async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)'''
    
'''async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, я не понял эту команду(")'''

async def func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    entry = []
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Введи Фамилию:")
    surname = update.message.text
    entry.append(surname)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Введи Имя:")
    name = update.message.text
    entry.append(name)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Введи телефон:")
    phone = update.message.text
    entry.append(phone)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Введи описание:")
    description = update.message.text
    entry.append(description)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Запись сделана ✅")
 
  
if __name__ == '__main__':
    application = ApplicationBuilder().token('5633157833:AAHPma1xc5pNT6JpP-PVT9TJxiHFhBkAOZc').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)
    
    func_handler = CommandHandler('func', func)
    application.add_handler(func_handler)
    
    '''echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)'''
    
    '''unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)'''
    
    print('start bot')
    
    application.run_polling()
