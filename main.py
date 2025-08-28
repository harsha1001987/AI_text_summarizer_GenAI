import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def count_tokens(text):
    # Simple approximation: split by whitespace
    return len(text.split())

def summarize_text(text, style="concise", top_p=0.8, temperature=0.5):
    prompt = (
        f"Summarize the following text in a {style} manner.\n"
        f"Text: {text}\n"
        "Summary:"
    )
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "topP": top_p,
            "temperature": temperature
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
    return result['candidates'][0]['content']['parts'][0]['text']

if __name__ == "__main__":
    input_text = "Artificial Intelligence is transforming industries by automating tasks, improving efficiency, and enabling new capabilities."
    summary = summarize_text(input_text, style="detailed", top_p=0.7, temperature=0.7)
    print("Summary:", summary)

