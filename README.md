


## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku
 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sddgr807/YTB-MusicBot.git)

### StringSession

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@itzgauravv/AuraXVCBot#main.py) 

## Commands
-The commands and there use is explained here-:
- `/saavn` To search song on jio saavan and play the first result 
- `/ytt` To search the song on Youtube and play the first matching result.
- `/deezer` To search song on deezer and play good quality stream.
- `/song` To download a song from youtube.
- `/play` Reply this in response to a link or any telegram audio file it will be played 
- `/skip` to skip current song 
- `/stop` to stop the streaming of song 
- `/pause` to pause the stream 
- `/resume` to resume the playback. 
- Inline search is also supported.






