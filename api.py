import telegram
from dotenv import load_dotenv
import os


class Bot:
    def __init__(self) -> None:
        load_dotenv()
        self.bot = telegram.Bot(token=os.getenv("API_KEY"))

    async def msg(self, text):
        await self.bot.send_message(chat_id=6720376506, text=text)




