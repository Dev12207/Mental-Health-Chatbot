# Mental Health Chatbot

A simple mental health support chatbot that uses local rule-based intent handling and optional Gemini API responses.

## Setup

1. Create and activate the virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file from the example:
   ```powershell
   copy .env.example .env
   ```

4. Open `.env` and add your Gemini API key:
   ```text
   GEMINI_API_KEY=your_api_key_here
   ```

## Run

```powershell
.venv\Scripts\activate
streamlit run app.py
```

## Notes

- The `.env` file is ignored by Git via `.gitignore`.
- If `GEMINI_API_KEY` is not set, the bot will fall back to rule-based responses.