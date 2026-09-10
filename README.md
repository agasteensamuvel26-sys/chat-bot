# Domain-Specific Gemini 3.1 Flash-Lite Flask Chatbot

A responsive, no-login chatbot built with Flask and the Google GenAI Python SDK.

## Features

- No login or registration.
- Gemini `gemini-3.1-flash-lite`.
- Strict domain-only answering through a server-side system instruction.
- Temporary per-session chat history.
- Each browser session gets its own conversation cookie; chat history is not intentionally shared between users.
- Responsive mobile/tablet/laptop/desktop UI.
- UI title, domain, prompt, behavior, welcome text, colors and PORT are configurable in `config.py`.
- Gemini API key can be supplied through `.env`.
- Render + Gunicorn deployment support.
- Project can be renamed based on your chatbot title.

## 1. Configure the chatbot

Open `config.py` and change:

- `CHATBOT_TITLE`
- `DOMAIN`
- `SYSTEM_PROMPT`
- `BEHAVIOR`
- `WELCOME_MESSAGE`
- UI colors
- Gemini settings

For example:

```python
CHATBOT_TITLE = "Python Tutor AI"
DOMAIN = "Python programming"
```

The domain restriction is enforced in the backend prompt, so the model is instructed to refuse unrelated questions.

## 2. Add your Gemini API key

Edit `.env`:

```env
GEMINI_API_KEY=your_real_key_here
FLASK_SECRET_KEY=use-a-long-random-secret
PORT=5000
```

Do not commit `.env` to a public repository.

## 3. Install

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation, you can install without activating:

```powershell
py -3.12 -m pip install -r requirements.txt
```

## 4. Run locally

```powershell
python app.py
```

Then open:

`http://127.0.0.1:5000`

## 5. Production with Gunicorn

Linux/macOS:

```bash
gunicorn app:app
```

Render start command:

```bash
gunicorn app:app
```

Render automatically provides the `PORT` environment variable. The app reads it first and falls back to `config.PORT`.

## 6. Render environment variables

In your Render Web Service, add:

- `GEMINI_API_KEY` = your Gemini API key
- `FLASK_SECRET_KEY` = a long random secret
- `PYTHON_VERSION` = `3.12.10` (optional)

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
gunicorn app:app
```

## 7. Session privacy note

The app stores the temporary conversation in Flask's signed client-side session cookie. This means the server does not keep a shared chat database, and different browser sessions have separate histories.

For production applications handling sensitive information, do not put sensitive conversation data in client-side cookies. Use a server-side session store such as Redis with secure session configuration.

## 8. Important API-key security

Never put a real API key directly into `templates/index.html` or JavaScript. The browser calls your Flask backend, and only the backend talks to Gemini.

If you prefer configuration in `config.py`, you may set:

```python
GEMINI_API_KEY = "your_key"
```

but `.env` / Render environment variables are strongly recommended.

## Project structure

```text
your-chatbot/
├── app.py
├── config.py
├── .env
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```
