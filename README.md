# AI_text_summarizer_GenAI***Project Overview***

The AI Text Summarizer is a React.js web application that takes a long text (e.g., an article, blog post, or research paper) and generates concise summaries using AI models. The summarizer helps users quickly grasp the key points of large texts without reading everything in detail.

***Features***

1.Paste or type text input.

2.Select summary length: Short, Medium, Detailed.

3.Generate AI-powered summaries using OpenAI / Hugging Face models.

4.Copy summary to clipboard.

5.Clean, responsive UI built with React + Tailwind CSS.

***Tech Stack***

Frontend: React.js, Tailwind CSS

AI API Options:

OpenAI GPT-3.5/GPT-4 API

Hugging Face Summarization model (facebook/bart-large-cnn)

Deployment: Vercel / Netlify

***Implementation Steps***

1. User Input

User pastes an article in a text area.

User selects summary length (short/medium/detailed).

2. API Integration

If using Hugging Face: Call the summarization endpoint with user text.

If using OpenAI: Send prompt → “Summarize this article in {length} format”.

3. Summary Generation

The AI model processes text → returns summary.

Apply post-processing (short/medium/detailed word trimming).

4. Display Output

Display summary in a styled card.

Add “Copy to Clipboard” button.

## System Prompt
You are an AI assistant specialized in summarizing text.  
Your role is to read the given content and produce a clear and concise summary.  
Always follow the requested summary length (short, medium, detailed).  

## User Prompt
Summarize the following article in a {length} format:  
{user_text}
