from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time
# Define the authorized user ID
AUTHORIZED_USER_ID = 1653535224
@Bot.on_message(filters.command('stats') & filters.user(AUTHORIZED_USER_ID))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))
@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    if message.from_user.id == AUTHORIZED_USER_ID:
        if USER_REPLY_TEXT:
            await message.reply_text(USER_REPLY_TEXT)
