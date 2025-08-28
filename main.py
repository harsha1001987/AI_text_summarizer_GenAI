import os
import requests
import json

API_KEY = os.getenv("GEMINI_API_KEY")
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def count_tokens(text):
    # Simple approximation: split by whitespace
    return len(text.split())

def summarize_text(text, style="concise", top_p=0.8, temperature=0.5, top_k=40):
    prompt = (
        f"Summarize the following text in a {style} manner.\n"
        f"Return the summary in JSON format with a 'summary' key.\n"
        f"Text: {text}\n"
        "Summary:"
    )
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "topP": top_p,
            "temperature": temperature,
            "topK": top_k
        }
    }
    response = requests.post(
        f"{ENDPOINT}?key={API_KEY}",
        headers=headers,
        json=data
    )
    result = response.json()
    # Log token count
    token_count = count_tokens(prompt)
    print(f"Tokens used in prompt: {token_count}")
    # Parse structured output
    summary_text = result['candidates'][0]['content']['parts'][0]['text']
    try:
        summary_json = json.loads(summary_text)
        return summary_json['summary']
    except Exception:
        return summary_text

if __name__ == "__main__":
    input_text = "Artificial Intelligence is transforming industries by automating tasks, improving efficiency, and enabling new capabilities."
    summary = summarize_text(input_text, style="detailed", top_p=0.7, temperature=0.7, top_k=50)
    print("Summary:", summary)

