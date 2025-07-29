import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7581965351:AAEjl7DeWkMpC7V_MceD5ajDwfCYJRLBWbM"
SOURCE_CHANNEL_USERNAME = "modocapital"
DESTINATION_CHAT_ID = -1002623510061  # Ensure this is an int, not a string

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        try:
            await context.bot.forward_message(
                chat_id=DESTINATION_CHAT_ID,
                from_chat_id=update.channel_post.chat.id,
                message_id=update.channel_post.message_id
            )
            print(f"✅ Forwarded message from @{SOURCE_CHANNEL_USERNAME}")
        except Exception as e:
            print(f"❌ Error forwarding message: {e}")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, forward_message))
    print("🤖 Bot is running and listening...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
