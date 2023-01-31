# # from playsound import playsound
# from pydub import AudioSegment
# from pydub.playback import play
import gtts
text = gtts.gTTS("HEY my name is DYlan What is your name?")
text.save('audio.wav')
# # playsound('file.mp3')
# song = AudioSegment.from_mp3('audio.mp3')
# play(song)
# print(10)

import pyaudio
import wave

filename = 'audio.wav'

# Set chunk size of 1024 samples per data frame
chunk = 1024  

# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunks
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

# Close and terminate the stream
stream.close()
p.terminate()