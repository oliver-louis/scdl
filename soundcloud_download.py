from yt_dlp import YoutubeDL

url = input("Enter SoundCloud URL: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'writethumbnail': True,
    'postprocessors': [
        {  # Extract audio to MP3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        },
        {  # Embed metadata
            'key': 'FFmpegMetadata',
        },
        {  # Embed cover art
            'key': 'EmbedThumbnail',
        },
    ],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

