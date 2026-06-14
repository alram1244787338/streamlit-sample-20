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

---

## ⚠️ Troubleshooting

For a normal local setup, `streamlit run run.py` works **without any extra configuration** — you should not need to edit a config file. If something goes wrong, find your symptom below. Each fix is a one-off command-line flag, so your global Streamlit settings stay untouched.

### Port 8501 is already in use

Symptom: an error such as `Port 8501 is already in use`, or `localhost:8501` shows a different app.

Fix — choose another port for this run only:

```bash
streamlit run run.py --server.port 8502
```

Then open [http://localhost:8502](http://localhost:8502).

### The browser doesn't open automatically

When it starts, Streamlit prints the local URL in the terminal, for example:

```
Local URL: http://localhost:8501
```

Just open that URL in your browser manually — nothing needs to be configured.
(On a remote server where you never want a browser to launch, add `--server.headless true`.)

### You need to reach the app from another device

By default the app is reachable only from your own machine (`localhost`), which is the safest setting for a sample. Only if you explicitly need access from another device on the **same trusted network**, bind to all interfaces for this run:

```bash
streamlit run run.py --server.address 0.0.0.0
```

Then open `http://<this-machine-ip>:8501` from the other device.
Note: this exposes the app to your local network, so only do it on a trusted network and check your firewall.

### Still stuck? (advanced)

If you genuinely need to persist a setting, keep your global environment clean by using a **project-local** config instead of `~/.streamlit/config.toml`. Create `.streamlit/config.toml` inside this project folder:

```toml
[server]
port = 8501
```

Streamlit picks it up automatically when you run from the project directory. Avoid editing `~/.streamlit/config.toml` unless you intend to change Streamlit's behavior for *every* project on your machine.

---

## 📁 File Structure

```
.
├── run.py             # Main Streamlit app file (the one you run)
├── requirements.txt   # Pinned list of required libraries
├── README_ja.md       # Japanese README
└── README.md          # This file (English)
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
