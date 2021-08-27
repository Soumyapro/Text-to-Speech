from gtts import gTTS
import os

text = input("Type Anything You Want :   ")  # Taking input

language = "en"  # Language used : English

# Here slow means read text slowly which defaults to false.
app = gTTS(text=text, lang=language, slow=False)

app.save("speak.mp3")

os.system("speak.mp3")  # will open the video file automatically
