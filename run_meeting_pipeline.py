import subprocess
import os
from datetime import datetime
from pathlib import Path

def run_recording(name):
    subprocess.run(["python3", "record_system.py", name])

def run_transcription(name):
    subprocess.run(["python3", "transcriber.py", name])

def run_summary(name):
    subprocess.run(["python3", "summariser.py", name])

def main():
    meeting_name = input("Enter a name for this meeting: ").strip().replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_id = f"{meeting_name}_{timestamp}"

    os.environ["SESSION_ID"] = session_id  # Pass to subprocesses via env var

    print(f"\nSession ID: {session_id}")
    run_recording(session_id)
    run_transcription(session_id)
    run_summary(session_id)
    print("\n✅ All done. Files saved under ./recordings, ./transcripts, ./summaries")

if __name__ == "__main__":
    main()
