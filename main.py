import os
from pyrogram import Client, filters
from pytube import YouTube
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

app = Client("beatguru", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🎵 Hello! I'm BEATGURU — your Telegram music bot!\nType `/play <song name>` to begin.")

@app.on_message(filters.command("play"))
async def play(client, message):
    if len(message.command) < 2:
        await message.reply("❗ Usage: `/play <song name>`")
        return
    query = " ".join(message.command[1:])
    await message.reply(f"🔍 Searching for `{query}` on YouTube... (demo response)")

if os.environ.get('RENDER'):
    from flask import Flask
    flask_app = Flask(__name__)

    @flask_app.route('/')
    def index():
        return "BEATGURU is alive!"

    import threading
    threading.Thread(target=lambda: flask_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))).start()

app.run()
