import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Load environment variables if needed (optional)
# from dotenv import load_dotenv
# load_dotenv()

# === CONFIG ===
BOT_TOKEN = "7581965351:AAEjl7DeWkMpC7V_MceD5ajDwfCYJRLBWbM"
SOURCE_CHANNEL_USERNAME = "@modocapital"
DESTINATION_CHAT_ID = -1002623510061  # Must be int

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# === Message Forwarder ===
async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        try:
            await context.bot.forward_message(
                chat_id=DESTINATION_CHAT_ID,
                from_chat_id=update.channel_post.chat_id,
                message_id=update.channel_post.message_id
            )
            print(f"✅ Forwarded message from {SOURCE_CHANNEL_USERNAME}")
        except Exception as e:
            print(f"❌ Failed to forward message: {e}")

# === Bot Setup ===
async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, forward))

    print("🚀 Forward bot running...")
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
