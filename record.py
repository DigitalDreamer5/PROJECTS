import pyaudio
import wave

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILE = "output.wav"


DEVICE_INDEX = 1
p = pyaudio.PyAudio()

# Open a recording stream
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, input_device_index=DEVICE_INDEX,
                frames_per_buffer=CHUNK)

print("🎤 Recording...")
frames = []

for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("✅ Recording finished!")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()


with wave.open(OUTPUT_FILE, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"📁 Audio saved as {OUTPUT_FILE}")

