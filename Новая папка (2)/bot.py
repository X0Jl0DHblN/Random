Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
... from telegram import Update
... from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
... 
... # Укажите свой токен
... TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
... 
... # Папка с файлами
... FILES_DIR = 'files'  # Папка, где находятся Ваши файлы
... 
... # Команда /start
... def start(update: Update, context: CallbackContext) -> None:
...     update.message.reply_text('Привет! Отправьте мне название файла, и я его отправлю вам.')
... 
... # Обработка текстовых сообщений
... def handle_message(update: Update, context: CallbackContext) -> None:
...     file_name = update.message.text.strip()
...     file_path = os.path.join(FILES_DIR, file_name)
... 
...     if os.path.isfile(file_path):
...         with open(file_path, 'rb') as file:
...             update.message.reply_document(file)
...     else:
...         update.message.reply_text('Файл не найден. Пожалуйста, проверьте название.')
... 
... def main() -> None:
...     # Создание updater и dispatcher
...     updater = Updater(TELEGRAM_TOKEN)
...     dispatcher = updater.dispatcher
... 
...     # Обработка команд
...     dispatcher.add_handler(CommandHandler('start', start))
...     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
