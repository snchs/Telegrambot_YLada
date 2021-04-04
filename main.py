import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TOKEN

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
ANSWER = ""
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Напиши /start, чтобы начать работу')


def send_photo(update: Update, context: CallbackContext) -> None:
    import bullshit
    bytestring = bullshit.photo()
    with open('imgs/task.png', 'wb') as imagefile:
        imagefile.write(bytestring)
    update.message.reply_photo(bytestring)


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(CommandHandler("photo", send_photo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
