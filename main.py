from fastapi import FastAPI
from maxapi import Bot
from config import settings



bot = Bot(settings.MAX_BOT_TOKEN)


app = FastAPI()


@app.post("/")
async def send_message_to_max(data):
    await bot.send_message(settings.MAX_CHAT_ID, text=data)