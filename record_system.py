import subprocess
import threading
import signal
import os


def start_recording(raw_filename="raw_system_output.pcm"):
    # Start parec subprocess to capture system audio
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
    # Send SIGINT to stop parec cleanly
    process.send_signal(signal.SIGINT)
    process.wait()


def convert_to_wav(raw_filename="raw_system_output.pcm", output_filename="system_output.wav"):
    # Convert raw PCM to WAV using ffmpeg
    subprocess.run([
        "ffmpeg", "-y", "-f", "s16le",
        "-ar", "48000", "-ac", "2",
        "-i", raw_filename, output_filename
    ])
    print(f"Converted and saved to {output_filename}")
    os.remove(raw_filename)  # optional: clean up raw file


def main():
    raw_file = "raw_system_output.pcm"
    print("Recording system audio... Press Enter to stop.")
    process = start_recording(raw_file)

    input()  # Wait for Enter key
    print("Stopping recording...")
    stop_recording(process)

    convert_to_wav(raw_file, "system_output.wav")


if __name__ == "__main__":
    main()
