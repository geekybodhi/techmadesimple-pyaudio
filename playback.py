import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:
    print(" The script plays the provided wav file.\n Proper usage: %s filename.wav" % sys.argv[0]))
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

# read data
data = wf.readframes(CHUNK)

while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()
