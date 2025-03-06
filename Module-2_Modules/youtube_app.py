"""from pytube import YouTube


url = "https://www.youtube.com/shorts/3SbDz1L1AnA"

YouTube(url=url).streams.filter().first().download()


"""

from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/shorts/3SbDz1L1AnA"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()
