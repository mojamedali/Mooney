# Mooney

**Mooney** is a personal finance management tool designed to help individuals track their expenses, analyze spending habits, and gain insight into their financial health.

## ✨ Features (Planned)

- ✅ Add and categorize expenses and income
- ✅ View summaries and detailed transaction history
- 📊 Visual analytics of financial data (via Bokeh or Plotly)
- 🏷️ Custom tags and categories
- 🔍 Search and filter transactions
- 📅 Date-based summaries (daily/weekly/monthly/yearly)
- 🔐 Secure local storage and optional user accounts
- 📁 Import/export data (CSV, JSON)
- 🌐 Web interface using Flask

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML/CSS (Jinja2 templates), optionally enhanced with Bokeh
- **Database**: SQLite (initially), extensible to PostgreSQL

## 📂 Project Structure (WIP)

```
mooney/
├── app/
│   ├── templates/
│   ├── static/
│   ├── routes/
│   ├── models/
│   └── __init__.py
├── tests/
├── migrations/
├── requirements.txt
└── run.py
```

## 🚀 Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/youruser/mooney.git
   cd mooney
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   flask run
   ```

## 🧪 Running Tests

Tests will be added gradually. For now:

```bash
pytest tests/
```

## 📝 Roadmap

You can find the development roadmap in `docs/roadmap.md`.

## 🤝 Contributing

This project is part of a personal development journey and currently not open to contributions. Feedback and ideas are welcome!

## 📄 License

MIT License – see `LICENSE` for details.
