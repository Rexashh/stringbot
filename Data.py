from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ʜᴇʏ {} [🚀](https://telegra.ph/file/d4d1f05aca9d71decf4ce.jpg)

sᴇʟᴀᴍᴀᴛ ᴅᴀᴛᴀɴɢ ᴅɪ {}

ɴᴏᴛᴇ : 
1) ᴊᴀɴɢᴀɴ ʙʟᴏᴄᴋ ʙᴏᴛ ɪɴɪ
2) ᴋᴀʀᴇɴᴀ ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴛʀɪɴɢ ᴍᴜ ᴊɪᴋᴀ ᴋᴀᴍᴜ ʙʟᴏᴋ ʙᴏᴛ ɪɴɪ

ᴀɴᴅᴀ ᴅᴀᴘᴀᴛ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀsɪʟᴋᴀɴ sᴇssɪᴏɴ sᴛʀɪɴɢ ᴘʏʀᴏɢʀᴀᴍ ᴅᴀɴ ᴛᴇʟᴇᴛʜᴏɴ. ɢᴜɴᴀᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴅɪʙᴀᴡᴀʜ ɪɴɪ ᴜɴᴛᴜᴋ ᴛᴀʜᴜ ʟᴇʙɪʜ ʙᴀɴʏᴀᴋ!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton(text="ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ʙʏ👨‍💻", url="https://t.me/JustRex")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/rexaprivateroom")],
    ]

    # Help Message
    HELP = """
⌨ **Available Commands** ⌨

/about - To Get About This Bot 🤖
/help - Check The Bot Commands 🔧
/start - Start The Bot
/generate - Generate Your String Now 😊
/cancel - Process Cancell 🥺
/restart - Restart And Start Generate String Session 😊
"""

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Bot To Generate Pyrogram And Telethon String Session...

sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : [xᴀ sᴜᴘᴘᴏʀᴛ](https://t.me/rexaprivateroom)

ғʀᴀᴍᴇᴡᴏʀᴋ : [ᴘʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [ᴘʏᴛʜᴏɴ](www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : @JustRex
    """
