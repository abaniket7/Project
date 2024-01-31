# Import pytube
from pytube import YouTube

# Create a YouTube object with the video URL
video = YouTube("https://youtube.com/shorts/jJFUGTSFqJI?feature=share")

# Get the highest resolution stream
stream = video.streams.get_highest_resolution()

# Download the stream
stream.download(filename="rickroll.mp4", output_path="C:\\Users\\Aniket")
