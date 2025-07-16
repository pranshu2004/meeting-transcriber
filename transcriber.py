import whisper

# Load the Whisper model (tiny/base/small/medium/large)
model = whisper.load_model("small")  # you can use "medium" or "large" if GPU available

# Path to your recorded system audio
AUDIO_FILE = "system_output.wav"

# Transcribe the audio
print("Transcribing...")
result = model.transcribe(AUDIO_FILE)

# Print transcript
transcript = result["text"]
print("\nTranscript:\n")
print(transcript)

# Save to text file
with open("transcript.txt", "w") as f:
    f.write(transcript)

print("\nSaved transcript to transcript.txt")
