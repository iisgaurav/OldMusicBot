from pyrogram import Client, filters



@Client.on_message(
    filters.command("help")
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
        
    ❤ The commands and there use is explained here ❤
- `/saavn` To search song on jio saavan and play the first result 
- `/ytt` To search the song on Youtube and play the first matching result.
- `/deezer` To search song on deezer and play good quality stream.
- `/play` Reply this in response to a link or any telegram audio file it will be played 
- `/skip` to skip current song 
- `/stop` to stop the streaming of song 
- `/pause` to pause the stream 
- `/resume` to resume the playback. 
- Inline search is also supported."""



    )
