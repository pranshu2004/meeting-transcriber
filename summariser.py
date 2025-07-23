from llama_cpp import Llama
import textwrap
import os
import sys

def main():
    session_id = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SESSION_ID", "meeting")
    transcript_path = f"./transcripts/{session_id}_transcript.txt"
    summary_path = f"./summaries/{session_id}_summary.txt"

    with open(transcript_path) as f:
        full_text = f.read()

    chunks = textwrap.wrap(full_text, 1500)  
    llm = Llama(model_path="mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)
    summaries = []

    for i, chunk in enumerate(chunks):
        prompt = f"""
You are summarizing a long meeting transcript in smaller batches due to token size limitations.

This is batch {i+1} out of {len(chunks)}. Please summarize the content below in **clean bullet points**.

--- Transcript Segment (Batch {i+1}) ---
{chunk}
--- End of Segment ---

Summary (bullet points):
"""
        print(f"Summarizing batch {i + 1}/{len(chunks)}...")
        output = llm(prompt, max_tokens=512, stop=["</s>"])
        summary = output["choices"][0]["text"].strip()
        summaries.append(f"### Batch {i + 1}\n{summary}\n")

    with open(summary_path, "w") as f:
        f.write("\n".join(summaries))

    print(f"Saved final summary to {summary_path}")

if __name__ == "__main__":
    main()
