from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
I am 𝗔𝘂𝗿𝗮𝗫𝗠𝘂𝘀𝗶𝗰𝗕𝗼𝘁 VC Music Player, an open-source bot that lets you play music in your Telegram groups.
Maintained by [AuraX Owner](t.me/AuraX_Owner) ❤
Use the buttons below to know more about me.</b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗖𝗠𝗗𝗦 ⚡️", url="https://telegra.ph/AuraXMusicBot---A-TELEGRAM-VC-MUSIC-PLAYER-BOT-03-28"
                    ),
                    InlineKeyboardButton(
                        "𝗖𝗥𝗘𝗔𝗧𝗘𝗥⚡️", url="https://t.me/AuraX_Owner",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝗚𝗥𝗢𝗨𝗣 ⚡️", url="https://t.me/AuraXSupport"
                    ),
                    InlineKeyboardButton(
                        "𝗨𝗣𝗗𝗔𝗧𝗘𝗦 ⚡️", url="https://t.me/AuraXUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝗣𝗚𝗟𝗭𝗢𝗡𝗘 𝗖𝗛𝗔𝗧𝗚𝗥𝗢𝗨𝗣 ⚡️", url="https://t.me/PglZone"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
