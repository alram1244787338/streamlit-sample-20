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

Or install all dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the App

Start the app with the following command:

```bash
streamlit run run.py
```

Your browser should open automatically. If it doesn't, navigate to:
[http://localhost:8501](http://localhost:8501)

> **Note:** No changes to your global `~/.streamlit/config.toml` are needed. This project includes its own `.streamlit/config.toml` with sensible defaults.

---

## ⚠️ Troubleshooting

If something doesn't work, find the symptom that matches your situation below. **Try only the step that matches — no need to do all of them.**

### Symptom 1: "Port 8501 is already in use"

Another process is using port 8501. Start on a different port:

```bash
streamlit run run.py --server.port 8502
```

Then access [http://localhost:8502](http://localhost:8502).

### Symptom 2: Browser doesn't open automatically

This is normal in some environments (e.g., WSL, remote servers). Simply open your browser manually and go to [http://localhost:8501](http://localhost:8501).

If you want to suppress the auto-open prompt in the future, uncomment `headless = true` in `.streamlit/config.toml`.

### Symptom 3: Need to access from another device on the same network

By default, Streamlit only listens on `localhost`. To allow connections from other devices on your LAN, uncomment the following line in `.streamlit/config.toml`:

```toml
[server]
address = "0.0.0.0"
```

Then access the app using your machine's IP address, e.g., `http://<your-ip>:8501`.

> **Important:** Only do this on trusted networks. Do not expose Streamlit directly to the public internet.

### Symptom 4: CORS errors in the browser console

This usually happens when running behind a reverse proxy or in certain cloud environments. As a **last resort**, you can uncomment the following in `.streamlit/config.toml`:

```toml
[server]
enableCORS = false
```

For local development on `localhost`, you should **never** need to change this.

### Still not working?

Try these quick checks:

1. **Is Python installed?** Run `python --version` (should be 3.7+).
2. **Is Streamlit installed?** Run `streamlit --version`.
3. **Can you run the built-in demo?** Run `streamlit hello` — if this works, the issue is in the app code, not your environment.

---

## 📁 File Structure

```
.
├── .streamlit/
│   └── config.toml      # Project-level Streamlit config (no global changes needed)
├── run.py               # Main Streamlit app file
├── requirements.txt     # List of required libraries
├── README.md            # This file (English)
├── README_ja.md         # Japanese version
└── README_zh.md         # Chinese version
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
