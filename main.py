import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# --- Config ---
BOT_TOKEN = "7581965351:AAEjl7DeWkMpC7V_MceD5ajDwfCYJRLBWbM"
SOURCE_CHANNEL_USERNAME = "@modocapital"
DESTINATION_CHAT_ID = -1002623510061

# --- Logging ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# --- Handler ---
async def forward_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    if message and message.chat.username == SOURCE_CHANNEL_USERNAME.strip("@"):
        try:
            await context.bot.send_message(
                chat_id=DESTINATION_CHAT_ID,
                text=message.text or message.caption or "📢 (Unsupported message type)"
            )
            logging.info(f"✅ Forwarded message from @{SOURCE_CHANNEL_USERNAME}")
        except Exception as e:
            logging.error(f"❌ Failed to forward message: {e}")

# --- Start Bot ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POSTS, forward_channel_post))
    logging.info("🚀 Bot started and listening...")
    app.run_polling()
