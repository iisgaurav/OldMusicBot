from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!

I am {bn} Music Player, an open-source bot that lets you play music in your Telegram groups.
Join our support group @AuraXSupport.
/help to know my commands.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Assistant⚡️", url="https://t.me/AuraXMusic"
                    ),
                    InlineKeyboardButton(
                        "Creater⚡️", url="https://t.me/AuraX_Owner",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support⚡️", url="https://t.me/AuraXSupport"
                    ),
                    InlineKeyboardButton(
                        "PglZone⚡️", url="https://t.me/PglZone"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Add To Your Group⚡️", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
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


