from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""❤ The commands and there use is explained here ❤
- `/play` Reply this in response to a link or any telegram audio file it will be played 
- `/play <song name>` To play a song from youtube
- `/song <Song Name>` To download a song
- `/skip` to skip current song 
- `/stop` to stop the streaming of song 
- `/pause` to pause the stream 
- `/resume` to resume the playback. 
- Inline search is also supported.""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""❤ The commands and there use is explained here ❤
- `/play` Reply this in response to a link or any telegram audio file it will be played 
- `/play <song name>` To play a song from youtube
- `/song <Song Name>` To download a song
- `/skip` to skip current song 
- `/stop` to stop the streaming of song 
- `/pause` to pause the stream 
- `/resume` to resume the playback. 
- Inline search is also supported.""")