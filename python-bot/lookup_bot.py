#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
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

    # 根据不同的选项执行不同的操作
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
    """处理选项1"""
    # 执行选项1的操作
    result = subprocess.run(['curl', 'https://www.ipqualityscore.com/api/json/phone/2Q256k6NiskFPiM9tAIrWyV2bHMN7jEm/19548000001'], capture_output=True, text=True)
   
    # 获取Curl命令的输出结果
    output = result.stdout
    print(output) 
    print("\n")
    # 解析JSON结果
    data = json.loads(output)

    # 构建消息
    message = "Phone Check Results:\n"
    message += f"valid: {data['message']}\n"  
    message += f"success: {data['success']}\n"
    message += f"formatted number: {data['formatted']}\n"  
    message += f"local_format: {data['local_format']}\n"  
    message += f"fraud_score: {data['fraud_score']}\n"  
    message += f"recent_abuse: {data['recent_abuse']}\n"  
    message += f"VOIP: {data['VOIP']}\n"  
    message += f"prepaid: {data['prepaid']}\n"  
    message += f"risky: {data['risky']}\n"  
    message += f"active: {data['active']}\n"  
    message += f"carrier: {data['carrier']}\n"  
    message += f"line_type: {data['line_type']}\n"  
    message += f"country: {data['country']}\n"  
    message += f"city: {data['city']}\n"  
    message += f"zip_code: {data['zip_code']}\n"    
    message += f"region: {data['region']}\n"
    print(message) 
    await update.callback_query.message.reply_text(message)

async def handle_option2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """处理选项2"""
    # 执行选项2的操作
    current_datetime = datetime.now()
    date = current_datetime.strftime("%Y-%m-%d")
    time = current_datetime.strftime("%H:%M:%S")

    response = f"当前日期：\n{date}\n当前时间：\n{time}"
    await update.callback_query.message.reply_text(response)    

async def handle_option3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """处理选项3"""
    # 执行选项3的操作
    await update.callback_query.message.reply_text("你选择了选项3")

async def unknown_option(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """处理未知选项"""
    # 处理未知选项的操作
    await update.callback_query.message.reply_text("未知选项")


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