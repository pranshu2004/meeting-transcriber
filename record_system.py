import subprocess
import signal
import os
import sys

def start_recording(raw_filename):
    process = subprocess.Popen([
        "parec",
        "-d", "alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink.monitor",
        "--rate=48000",
        "--channels=2",
        "--format=s16le",
        raw_filename
    ])
    return process

def stop_recording(process):
    process.send_signal(signal.SIGINT)
    process.wait()

def convert_to_wav(raw_filename, output_filename):
    subprocess.run([
        "ffmpeg", "-y", "-f", "s16le",
        "-ar", "48000", "-ac", "2",
        "-i", raw_filename, output_filename
    ])
    os.remove(raw_filename)
    print(f"Saved: {output_filename}")

def main():
    session_id = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SESSION_ID", "meeting")
    raw_path = f"./recordings/{session_id}_audio.pcm"
    wav_path = f"./recordings/{session_id}_audio.wav"

    print("Recording system audio... Press Enter to stop.")
    process = start_recording(raw_path)
    input()
    print("Stopping...")
    stop_recording(process)
    convert_to_wav(raw_path, wav_path)

if __name__ == "__main__":
    main()
