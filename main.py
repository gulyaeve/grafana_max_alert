
from fastapi import FastAPI
from maxapi import Bot
import uvicorn
from config import settings
from schemas import GrafanaPayload


bot = Bot(settings.MAX_BOT_TOKEN)
app = FastAPI()


@app.post("/")
async def send_message_to_max(data: GrafanaPayload):
    print(data)
    custom_string = "\n".join(f"{k}: {v}" for k, v in data.commonLabels.items())
    # answer = ""
    # for label in data.commonLabels:
    #     answer += f"{label}\n"
    await bot.send_message(settings.MAX_CHAT_ID, text=custom_string)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)