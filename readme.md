# Meeting Transcriber & Summarizer

This project was created to help me **transcribe and summarize meetings**, including both:

- **Online meetings** (by recording system audio)
- **In-person or hybrid meetings** (by switching to microphone input instead)

Everything here is built with **free and open source software** and designed to run **entirely offline**, including transcription and summarization. This is especially helpful for privacy-sensitive contexts like interviews or internal team discussions.

---

## Features

- Record system audio (or mic)
- Transcribe using [OpenAI Whisper](https://github.com/openai/whisper)
- Summarize using [Mistral-7B Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) via `llama-cpp-python`
- CPU-only — no GPU required
- Auto-saves recordings, transcripts, and summaries in session-specific folders
- Hackable, scriptable, fully offline


---

## Tested Environment

- **OS**: Ubuntu 20.04.6 LTS
- **Python**: 3.11
- **Virtual environment**: created with `venv`
- **Hardware**: CPU-only (no GPU)

---



## Setup Instructions

### 1. Install system dependencies

Before running the scripts, make sure you have the following system tools installed:

```bash
sudo apt install ffmpeg pulseaudio-utils
```
These are used to capture system audio (`parec` from PulseAudio), convert audio formats (`ffmpeg`), and list available devices (`pactl`).

Create the required folders if they don't already exist:

```bash
mkdir -p recordings transcripts summaries
```

### 2. Clone this repo

```bash
git clone https://github.com/yourusername/meeting-transcriber.git
cd meeting-transcriber
```

### 3. Create virtual environment

```bash
python3.11 -m venv audio_venv
source audio_venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Download models

- Whisper (automatic on first run)
- Mistral 7B Instruct (Q4\_K\_M)
  - Download from [TheBloke/Mistral-7B-Instruct-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-GGUF)
  - Place the `.gguf` model in the root directory and update the path in `summariser.py`

---

## How to Run

### Full Pipeline (One Command)

```bash
python run_meeting_pipeline.py
```

- Prompts you to name the meeting
- Records until you press `Enter`
- Make sure the source monitor is correct (edit `record_system.py`, update the `parec -d` device if needed)
- Use `pactl list sources short` to find the correct monitor
- Automatically transcribes and summarizes it
- Saves everything in:
    -`./recordings/<name>_audio.wav`
    -`./transcripts/<name>_transcript.txt`
    -`./summaries/<name>_summary.txt`

### Output File Structure

```bash
recordings/
  meeting123_20250722_audio.wav

transcripts/
  meeting123_20250722_transcript.txt

summaries/
  meeting123_20250722_summary.txt

```

---

## Future Work / Improvements

- **Speaker diarisation** (label different speakers)
  - Might require some level of user input
- Make it more usable for non-devs (e.g., GUI or CLI prompts)
- No hardcoding: auto-detect system source instead of manually editing `record_system.py`
- Maybe deploy it as a simple app, browser extension, or Electron GUI
- Possibly explore real-time meeting assistant extensions

---

## Contributions

Pull requests welcome — this is a very rough but functional start. If you have ideas for better UX, diarisation, efficient streaming, real-time handling, etc., feel free to contribute.

---

## License

This project is fully open source and licensed under the MIT License.

---

Built for people who prefer local control, privacy, and open tools.

## Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) for transcription
- [Mistral-7B](https://huggingface.co/mistralai) + [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- Ubuntu + PulseAudio + parec/ffmpeg ecosystem
- Hugging Face community for incredible model access

---

Happy hacking!

