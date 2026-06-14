# Streamlit Simple Sample App

This repository provides an example of a simple web application using the Python library Streamlit.

---

## ✅ Overview

Streamlit is an open-source library that allows you to build data applications using only Python code.

---

## 🧰 Requirements

* Python 3.10 or later (required by the pinned dependencies, e.g. `numpy==2.2.6`)
* pip

---

## 📦 Installation

Install the pinned dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the App

Start the app with the following command:

```bash
streamlit run run.py
```

After execution, access:
[http://localhost:8501](http://localhost:8501)

---

## ⚠️ If the App Doesn't Work Properly

The two commands above are enough to run the app locally. The steps below are
**optional** — use them only if you want to serve the app on a custom host/port
(for example, on a remote machine).

Generate a default config file (create the directory first so the redirect
succeeds on a fresh machine):

```bash
mkdir -p ~/.streamlit
streamlit config show > ~/.streamlit/config.toml
```

Open `~/.streamlit/config.toml` in your preferred editor (e.g., nano) and adjust
the server settings:

```toml
[server]
headless = true
port = 8501
address = "0.0.0.0"
```

Then run again:

```bash
streamlit run run.py
```

---

## 📁 File Structure

```
.
├── run.py             # Main Streamlit app (entry point)
├── requirements.txt   # Pinned Python dependencies
├── README.md          # This file (English)
└── README_ja.md       # Japanese version
```

---

## 📌 Additional Notes

Streamlit is very useful for rapid prototyping and data visualization.
It also supports creating more complex and customized applications.
Please feel free to explore its capabilities.

---

## 📚 References

* [https://streamlit.io/](https://streamlit.io/)

---

If you have any questions, please open an issue.
