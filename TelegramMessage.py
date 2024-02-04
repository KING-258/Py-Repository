from telegram import Bot
import asyncio
def main():
    Token = '6950245916:AAHx-3ZGwoXZmBOWDlQZw93lhC7HQhZ21Kg'
    Chat = '-4079773705'
    b = Bot(token= Token)
    asyncio.run(Message(b,Chat,'Motion'))
async def Message(bot,Chat, msg):
    await bot.send_message(chat_id =Chat, text=msg)
if __name__ == "__main__" :
    main()