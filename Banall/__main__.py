import os
from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from . import bot 
from Banall import STARTED, FINISH, ERROR, OWN_UNAME


@bot.on_message(filters.group & filters.command("banall"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(bot.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply(STARTED.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    bot.ban_chat_member(chat_id=msg.chat.id, user_id=member.user.id)
                    count_kicks += 1
            msg.reply(FINISH.format(count_kicks))
        except Exception as e:
            msg.reply(ERROR.format(str(e)))
    else:
        msg.reply("i need to be admin In This Group To Perform This Action!")


@bot.on_message(filters.group & filters.service, group=2)
def service(c, m):
    m.delete()


@bot.on_message(filters.private)
def start(_, msg: Message):
    msg.reply_photo(
                    photo="https://telegra.ph/file/b2704f702734610934b9c.jpg", 
                    caption="Hi, I'm a Banall Robot to help you remove all users from your group.\nNow add me to a group and don't forget to give me the permissions.\nThen send /banall in the group and I will start my work.", 
                    reply_markup=InlineKeyboardMarkup(
                                                      [
                                                       [
                                                        InlineKeyboardButton("Source", url="https://www.github.com/TheDeCode/BanAllBot"), 
                                                        InlineKeyboardButton("Support", url="https://t.me/TheeDeCode")                                      
                                                       ], 
                                                       [
                                                        InlineKeyboardButton("Update", url="https://t.me/OfficialDeCode"), 
                                                        InlineKeyboardButton("Creator", url="https://t.me/DeCodeDevs")                                      
                                                       ], 
                                                       [
                                                        InlineKeyboardButton("Owner", url=f"https://t.me/{OWN_UNAME}")                                                                                              
                                                       ]                                                     
                                                      ]
                                                     )
)


bot.run()
idle()

print("Done BanAll Started...") 
print("Join @TheeDeCode || @OfficialDeCode For Help") 
