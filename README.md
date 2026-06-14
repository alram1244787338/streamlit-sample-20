# Streamlit Simple Sample App

*Read this in another language: [日本語 (README_ja.md)](README_ja.md)*

This repository provides an example of a simple web application using the Python library Streamlit. This is a minimal working example of a Streamlit web app.

---

## ✅ Overview

Streamlit is an open-source library that allows you to build data applications using only Python code.

---

## 👀 What you'll see when it runs

When the app starts, the page shows:

* the title **Streamlit Simple Sample App**,
* a green banner confirming that Streamlit is running successfully,
* a small text box that greets you by name.

Everything on the page is sample/demo content — it is not a placeholder and not an error state. The app interface is in English; the documentation is available in English (this file) and Japanese ([README_ja.md](README_ja.md)).

---

## 🧰 Requirements

* Python 3.7 or later
* pip

---

## 📦 Installation

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

To install only Streamlit:

```bash
pip install streamlit
```

---

## 🚀 How to Run the App

Start the app with the following command:

```bash
streamlit run run.py
```

After execution, access:
[http://localhost:8501](http://localhost:8501)

You should see the title, a green "running successfully" banner, and a greeting box — confirming the sample works.

---

## ⚠️ If the App Doesn't Work Properly

Run the following command:

```bash
streamlit config show > ~/.streamlit/config.toml
```

Open `~/.streamlit/config.toml` in your preferred editor (e.g., nano):

```bash
nano ~/.streamlit/config.toml
```

Add or modify the following settings:

```toml
[server]
headless = true
enableCORS = false
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
├── run.py              # Main Streamlit app (entry point)
├── requirements.txt    # Pinned dependencies
├── test_consistency.py # Checks that the page text matches this README
├── README.md           # This file (English)
└── README_ja.md        # Japanese translation
```

---

## 🔍 Verify the docs match the app

A small, dependency-free check confirms that the page text in `run.py` stays consistent with this README:

```bash
python test_consistency.py
```

---

## 📌 Additional Notes

Streamlit is very useful for rapid prototyping and data visualization.
It also supports creating more complex and customized applications.
Feel free to use this repository as a starting template and build on top of it.

---

## 📚 References

* [https://streamlit.io/](https://streamlit.io/)

---

If you have any questions, please open an issue.
