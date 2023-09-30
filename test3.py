from telethon import TelegramClient, events

api_id = 21831252
api_hash = '5bd1c0c1c26af62e9f62b629b8445c4b'
phone="89269549196"
client = TelegramClient(phone, api_id, api_hash, system_version="4.16.30-vxCUSTOM")

@client.on(events.NewMessage)
async def my_event_handler(event):
    print(event.raw_text)
    if 'Привет' in event.raw_text:
        await event.reply('спокойной ночи')

client.start()
client.run_until_disconnected()
