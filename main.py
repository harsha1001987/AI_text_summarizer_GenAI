import requests

API_KEY = "YOUR_GEMINI_API_KEY"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def summarize_text(text):
    prompt = f"Summarize the following text:\n{text}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(
        f"{ENDPOINT}?key={API_KEY}",
        headers=headers,
        json=data
    )
    result = response.json()
    return result['candidates'][0]['content']['parts'][0]['text']

if __name__ == "__main__":
    input_text = "Artificial Intelligence is transforming industries by automating tasks, improving efficiency, and enabling new capabilities."
    summary = summarize_text(input_text)
    print("Summary:", summary)

