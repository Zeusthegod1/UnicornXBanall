#Copyright @piroXpower ||| @IndianSupportGroup

import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from choot import Var


logging.basicConfig(level=logging.INFO)

print("Starting.....")

TeamIndia = TelegramClient('TeamIndia', Var.API_KEY, Var.API_HASH).start(bot_token=Var.TOKEN)


BANNER = []
for x in Var.SUDO: 
    BANNER.append(x)

print("Booting.....")

@TeamIndia.on(events.NewMessage(pattern="^/ping"))  
async def ping(e):
    if e.sender_id in BANNER:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**I'm Online Sir** \n\n __Pong__ !! `{ms}` ms")

print("Loading Ping.....")

@TeamIndia.on(events.NewMessage(pattern="^/online"))  
async def ping(e):
    if e.sender_id in BANNER:
        start = datetime.now()
        text = "Checking..."
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**Yes Am Online Boss\n\n __Pong__ !! `{ms}` ms")

print("Loading Banall.....")
@TeamIndia.on(events.NewMessage(pattern="^/banall"))
async def testing(event):
  if event.sender_id in BANNER:
   if not event.is_group:
        Reply = f"Noob !! Use This Cmd in Group."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       userchat = await event.get_chat()
       CHANDAN = await event.client.get_me()
       admin = userchat.admin_rights
       creator = userchat.creator
       if not admin and not creator:
           await event.reply("I Don't have sufficient Rights !!")
           return
       await event.reply("hey !! Black Magin Begins..")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == CHANDAN.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.2)

print("Loading Leave.....")

@TeamIndia.on(events.NewMessage(pattern="^/leave"))
async def _(e):
    if e.sender_id in BANNER:
        userchat = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = userchat[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            bc = e.chat_id
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left This Fucking Group")
            except Exception as e:
                await event.edit(str(e))   
          

print("Loading Restart.....")

@TeamIndia.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in BANNER:
        text = "__Restarting__ , Please Wait While Bot Being Rebooted!!"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await TeamIndia.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("Bot Deployed Successfully Join @IndianSupportGroup For Help")

TeamIndia.run_until_disconnected()
