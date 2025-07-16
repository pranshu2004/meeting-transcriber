from llama_cpp import Llama
import textwrap

# Load the quantized Mistral model
llm = Llama(model_path="mistral-7b-instruct-v0.1.Q4_K_M.gguf", n_ctx=2048)

# Step 1: Load the full transcript
with open("transcript.txt") as f:
    full_text = f.read()

# Step 2: Split into manageable chunks
def split_text(text, max_chars=1500):
    return textwrap.wrap(text, max_chars)

chunks = split_text(full_text)
total_chunks = len(chunks)

# Step 3: Summarize each chunk with clear instructions
summaries = []
for i, chunk in enumerate(chunks):
    prompt = f"""
You are summarizing a long meeting transcript in smaller batches due to token size limitations.

This is batch {i+1} out of {total_chunks}. Please summarize the content below in **clean bullet points**.

--- Transcript Segment (Batch {i+1}) ---
{chunk}
--- End of Segment ---

Summary (bullet points):
"""
    print(f"Summarizing batch {i + 1}/{total_chunks}...")
    output = llm(prompt, max_tokens=512, stop=["</s>"])
    summary = output["choices"][0]["text"].strip()
    summaries.append(f"### Batch {i + 1}\n{summary}\n")

# Step 4: Join all summaries and save
final_summary = "\n".join(summaries)

# Save to file
with open("final_summary.txt", "w") as f:
    f.write(final_summary)

print("Final bullet-point summary written to final_summary.txt")
