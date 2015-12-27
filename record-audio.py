import sys
import pyaudio
import wave


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = 'Monoaudio.wav'

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,channels = CHANNELS,rate = RATE, input = True,input_device_index = 0,frames_per_buffer = CHUNK)

print(" Now recording audio. Speak into the microphone. ")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print(" Done recording audio. ")
stream.stop_stream()    # "Stop Audio Recording
stream.close()          # "Close Audio Recording
p.terminate()           # "Audio System Close

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
