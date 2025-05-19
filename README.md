# 🧠 AI Chat Log Summarizer

This is a command-line tool that analyzes AI chat logs and generates a smart summary using the **Gemini 2.0 Flash API** by Google. It processes chat logs, extracts message statistics, identifies key topics using either **word frequency** or **TF-IDF**, and returns a concise, human-readable summary.

---

## 📂 Project Structure

```bash
chat_summarizer/
├── __init__.py               # Marks the directory as a Python package
├── analyzer.py               # Extracts message counts and keywords
├── parser.py                 # Parses chat logs
├── summarizer.py             # Builds prompt and calls Gemini API
├── utils.py                  # Logger setup and helper utilities
│
├── __pycache__/              # Compiled Python cache files (auto-generated)
│
data/
└── sample_chat.txt           # Sample input chat log
│
.env                          # Contains your Google API key
.gitignore                    # Hides environment and cache files from Git
main.py                       # CLI entry point for summarization
README.md                     # Project documentation
requirements.txt              # Required Python packages
```