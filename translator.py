# REQS --> telethon, googletrans==4.0.0-rc1


"""
SYSTEM OPERATION:
----------------------------

1) gets from user his phone number *** WITH COUNTRY CODE ***
2) the program reads user's groups from telegram
3) the user choose a group he wants to read from and click on it
4) the program recognize the origin language using 'Google Translate' and translate the latest message
    to the user's preferred language. (default language - english)
5) the user have the option to translate the older message or the newer (if possible), or change group.


NOTICE: for now, this program translate only from 'gaza now' channel to hebrew.
        if you want to change the channel, change in line 34 the 'gazaalannet' to your choice.
"""

from telethon import TelegramClient
from googletrans import Translator


api_id = "YOUR API ID KEY - AS AN INTEGER"
api_hash: str = 'YOUR API HASH KEY AS A STRING'

phone_number: str = "PHONE NUMBER STARTING WITH YOUR COUNTRY CODE"
username: str = 'CHOOSE YOUR CLIENT USERNAME'
client = TelegramClient(username, api_id, api_hash)
translator = Translator()

async def main():
    message_offset = 0
    async for message in client.iter_messages('gazaalannet', offset_id=message_offset):
        text = message.text
        print(f"message id: {message.id}\nmessage date: {message.date}\nmessage content:\n{message.text}")
        print('\nTRANSLATED:\n')
        translated = translator.translate(text, dest='he')
        print(translated.text)
        message_offset += 1
        i = input('\n\nDO YOU WANT TO TRANSLATE OLDER MESSAGE? Y\\N: ')
        while i not in ('Y', 'y', 'n', 'N'):
            i = input()
        if i in ('n', 'N'):
            break


with client:
    client.loop.run_until_complete(main())

