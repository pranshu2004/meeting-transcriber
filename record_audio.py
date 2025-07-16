import threading
import subprocess
import pyaudio
import wave


def record_system(duration_seconds=5, output_filename="system_output.wav"):
    raw_file = "raw_system_output.pcm"
    
    # Step 1: Record raw PCM using parec for a fixed time
    subprocess.run([
        "timeout", str(duration_seconds),
        "parec",
        "-d", "alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink.monitor",
        "--rate=48000",
        "--channels=2",
        "--format=s16le",
        raw_file
    ])

    # Step 2: Convert raw PCM to WAV using ffmpeg
    subprocess.run([
        "ffmpeg", "-y",  # Overwrite output if exists
        "-f", "s16le",              # Input format
        "-ar", "48000",             # Sample rate
        "-ac", "2",                 # Number of channels
        "-i", raw_file,             # Input file
        output_filename             # Output file
    ])

    print(f"✅ System audio saved to {output_filename}")


def record_mic():
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 5
    FILENAME = "mic_output.wav"

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, input_device_index=5,
                    frames_per_buffer=CHUNK)
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))


# Start both recordings
t1 = threading.Thread(target=record_system)
t2 = threading.Thread(target=record_mic)

t1.start()
t2.start()

t1.join()
t2.join()
print("Both recordings finished.")
