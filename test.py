from telethon import events
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
client = TelegramClient('anon', 1272883, "aa63af9889f1502ee22080e07f7daaba")

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    print (chat.id)
    #print (sender)
    print (chat_id)
    #print (sender_id)
    print (event.raw_text)
    #destination_user_username='Destination'
    #entity=await client.get_entity("Destination")
    #updates = await client(ImportChatInviteRequest('AAAAAFUe_UyK1izc5Hu86Q'))
    if str(chat.id)=="1444042095":
        await client.send_message(1249866283,event.raw_text)

client.start()
client.run_until_disconnected()
