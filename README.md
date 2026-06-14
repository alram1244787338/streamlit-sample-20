# Streamlit Simple Sample App

This repository provides an example of a simple web application using the Python library Streamlit.

---

## ✅ Overview

Streamlit is an open-source library that allows you to build data applications using only Python code.

---

## 🧰 Requirements

* Python 3.7 or later
* pip

---

## 📦 Installation

You can install the required library using the following command:

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

You should see a page titled **"Streamlit Sample App"** with:

* A green success banner confirming "The application is running successfully."
* A "Welcome!" introduction describing the app's purpose
* A "What's next?" section with steps for customization
* A "How to run" expander with the launch command

The page defaults to English. Use the sidebar to switch between English and Japanese.

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
├── run.py                 # Main Streamlit app file
├── requirements.txt       # List of required libraries
├── check_consistency.py   # Verifies page text matches README
├── README_ja.md           # Japanese README
├── README.md              # This file
└── .gitignore             # Git ignore rules
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
