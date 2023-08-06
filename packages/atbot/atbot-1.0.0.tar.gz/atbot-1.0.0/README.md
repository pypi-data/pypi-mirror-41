# Asynchronous Telegram Bot
This project allows you to create asynchrounous Telegram Bots using Python 3.

At the moment the API is sparse, feel free to add more methods via Pull Requests or submit Issues.

## Getting Started
1. Get the source using `git`

    ```git clone https://github.com/naim94a/atbot.git```

2. Install using `pip`

    ```pip install atbot```

## Example
```python
import os
import asyncio
from atbot import TelegramBot, TelegramMessage, ChatAction

API_KEY = os.getenv('API_KEY')

async def handle_message(bot, msg):
    if msg.text == '/start':
        await bot.send_chat_action(msg.chat.id, ChatAction.TYPING)
        await asyncio.sleep(0.2)
        await bot.send_message(msg.chat.id, 'Hello, {0}!'.format(msg.sender.first_name))

async def my_bot():
    bot = TelegramBot(API_KEY)
    while True:
        updates = await bot.get_updates()
        for update in updates:
            obj = update.get_obj()
            if isinstance(obj, TelegramMessage):
                await handle_message(bot, obj)

asyncio.run(my_bot())
```