import os
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

app_id = int(os.environ.get("API_ID", 12345))
app_key = os.environ.get('API_HASH')
token = os.environ.get('BOT_TOKEN')

app = Client("banall", app_id, app_key, bot_token=token)


STARTED = 'Black Magic Begins...'
FINISH = 'done, {} users were removed from group'
ERROR = 'something Went Wrong Please Try Again.{} !'

@app.on_message(filters.group & filters.command("banall"))
def main(_, msg: Message):
    chat = msg.chat
    me = chat.get_member(app.get_me().id)
    if chat.get_member(msg.from_user.id).can_manage_chat and me.can_restrict_members and me.can_delete_messages:
        try:
            msg.reply(STARTED.format(chat.members_count))
            count_kicks = 0
            for member in chat.iter_members():
                if not member.can_manage_chat:
                    chat.kick_member(member.user.id)
                    count_kicks += 1
            msg.reply(FINISH.format(count_kicks))
        except Exception as e:
            msg.reply(ERROR.format(str(e)))
    else:
        msg.reply("i need to be admin In This Group To Perform This Action!")


@app.on_message(filters.group & filters.service, group=2)
def service(c, m):
    m.delete()


@app.on_message(filters.private)
def start(_, msg: Message):
    msg.reply("Hi, I'm a robot to help you remove all users from your group.\nNow add me to a group and don't forget to give me the permissions.\nThen send /banall in the group and I will start my work.", 
    reply_markup=InlineKeyboardMarkup(
                                      [
                                        [
                                           InlineKeyboardButton("Source", url="https://www.github.com/TheDeCode/BanAllBot"), 
                                           InlineKeyboardButton("Support", url="https://t.me/TheeDeCode")                                      
                                        ]
                                      ]
                                     )
)


app.run()
