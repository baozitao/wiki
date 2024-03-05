#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
import emoji
import pytz
import subprocess
import json
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("look up number", callback_data="1"),
            InlineKeyboardButton("echo date", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    selected_option = query.data

    # ���ݲ�ͬ��ѡ��ִ�в�ͬ�Ĳ���
    if selected_option == "1":
        await handle_option1(update, context)
    elif selected_option == "2":
        await handle_option2(update, context)
    elif selected_option == "3":
        await handle_option3(update, context)
    else:
        await unknown_option(update, context)

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

async def handle_option1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """����ѡ��1"""
    # ִ��ѡ��1�Ĳ���
    result = subprocess.run(['curl', 'https://www.ipqualityscore.com/api/json/phone/2Q256k6NiskFPiM9tAIrWyV2bHMN7jEm/19548000001'], capture_output=True, text=True)
   
    # ��ȡCurl�����������
    output = result.stdout
    print(output) 
    print("\n")
    # ����JSON���
    data = json.loads(output)

    # ������Ϣ
    message = "Phone Check Results:\n"
    message += f"[{emoji.emojize(':information:')}valid] :     {data['message']}\n"  
    message += f"[{emoji.emojize(':hot_springs:')}success] :     {data['success']}\n"
    message += f"[{emoji.emojize(':telephone_receiver:')}formatted number] :     {data['formatted']}\n"  
    message += f"[{emoji.emojize(':telephone:')}local_format] :     {data['local_format']}\n"  
    message += f"[{emoji.emojize(':potato:')}fraud_score]  :     {data['fraud_score']}\n"  
    message += f"[{emoji.emojize(':popcorn:')}recent_abuse] :     {data['recent_abuse']}\n"  
    message += f"[{emoji.emojize(':radioactive:')}VOIP] :     {data['VOIP']}\n"  
    message += f"[{emoji.emojize(':roller_coaster:')}prepaid] :     {data['prepaid']}\n"  
    message += f"[{emoji.emojize(':scarf:')}risky] :     {data['risky']}\n"  
    message += f"[{emoji.emojize(':shamrock:')}active] :     {data['active']}\n"  
    message += f"[{emoji.emojize(':bank:')}carrier] :     {data['carrier']}\n"  
    message += f"[{emoji.emojize(':mobile_phone_with_arrow:')}line_type] :     {data['line_type']}\n"  
    message += f"[{emoji.emojize(':black_flag:')}country] :     {data['country']}\n"  
    message += f"[{emoji.emojize(':cityscape_at_dusk:')}city] :     {data['city']}\n"  
    message += f"[{emoji.emojize(':closed_mailbox_with_lowered_flag:')}zip_code] :     {data['zip_code']}\n"    
    message += f"[{emoji.emojize(':potato:')}region] :     {data['region']}\n"
    print(message) 
    await update.callback_query.message.reply_text(message)

async def handle_option2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """����ѡ��2"""
    # ִ��ѡ��2�Ĳ���
    # ��ȡ��ǰ���ں�ʱ��
    current_datetime = datetime.now()

    # ����һ��ʱ������
    timezone = pytz.timezone('Asia/Shanghai')

    # �����ں�ʱ������Ϊָ��ʱ��
    current_datetime = current_datetime.astimezone(timezone)

    # ��ʽ�������ַ���
    date = current_datetime.strftime("%Y-%m-%d")

    # ��ʽ��ʱ���ַ���
    time = current_datetime.strftime("%H:%M:%S")

    response = f"{emoji.emojize(':calendar:')}��ǰ���ڣ�\n{date}\n{emoji.emojize(':timer_clock:')}��ǰʱ�䣺\n{time}"
    await update.callback_query.message.reply_text(response)    

async def handle_option3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """����ѡ��3"""
    # ִ��ѡ��3�Ĳ���
    await update.callback_query.message.reply_text("��ѡ����ѡ��3")

async def unknown_option(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """����δ֪ѡ��"""
    # ����δ֪ѡ��Ĳ���
    await update.callback_query.message.reply_text("δ֪ѡ��")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.callback_query.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6331146612:AAF6GNnyi9fvNG3lwfACsKFuqN0qfXZTKDg").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()