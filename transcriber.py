import whisper
import os
import sys

def main():
    session_id = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SESSION_ID", "meeting")
    audio_path = f"./recordings/{session_id}_audio.wav"
    transcript_path = f"./transcripts/{session_id}_transcript.txt"

    model = whisper.load_model("small")
    print("Transcribing...")
    result = model.transcribe(audio_path)
    transcript = result["text"]

    with open(transcript_path, "w") as f:
        f.write(transcript)

    print(f"Saved transcript to {transcript_path}")

if __name__ == "__main__":
    main()
