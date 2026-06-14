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

> **In most cases, `streamlit run run.py` just works — no config changes needed.**
> This project ships a `.streamlit/config.toml` with everything commented out; Streamlit's built-in defaults are correct for local development. **Do not modify your global `~/.streamlit/config.toml`.**
>
> If something goes wrong, use the table below to identify your situation and apply **only** the matching fix.

### Quick self-check (do this first)

Before changing any configuration, narrow down the problem:

1. **Can Streamlit itself run?** Try `streamlit hello` — if the built-in demo works, your environment is fine and the issue is in the app code.
2. **Can you reach the URL?** Open [http://localhost:8501](http://localhost:8501) in a browser. If it loads, the app is running — your problem is just browser auto-open.
3. **Did the command fail at startup?** Read the terminal error. The most common one is a port conflict, covered below.

### Situation A: "Port 8501 is already in use"

Another process is occupying port 8501. Two ways to fix it — pick one:

* **Command-line flag (quickest, no file edits):**

  ```bash
  streamlit run run.py --server.port 8502
  ```

  Then open [http://localhost:8502](http://localhost:8502).

* **Persistent fix:** Uncomment `port = 8501` in `.streamlit/config.toml` and change the value.

### Situation B: App is running, but the browser didn't open

This is normal in WSL, SSH, Docker, or other headless environments. Just open your browser manually and go to [http://localhost:8501](http://localhost:8501).

To suppress the auto-open prompt permanently, uncomment `headless = true` in `.streamlit/config.toml`.

### Situation C: Need access from another device on the same network

By default, Streamlit binds to `localhost` only — other machines cannot connect. This is intentional for security.

To allow LAN access, uncomment this line in `.streamlit/config.toml`:

```toml
address = "0.0.0.0"
```

Then use your machine's local IP, e.g., `http://192.168.x.x:8501`.

> **⚠️ Security note:** This exposes the app to anyone on the network. Only use on trusted networks; never expose Streamlit directly to the public internet.

### Situation D: CORS errors in the browser console

This only happens behind a reverse proxy (nginx, Caddy) or in certain cloud-hosted setups. It does **not** happen during normal local development.

If you are sure this applies to you, uncomment the following in `.streamlit/config.toml`:

```toml
enableCORS = false
```

> **Do not change this for local `localhost` development** — it has no benefit and weakens browser security.

### Summary: which fix do I need?

| What you see | Situation | Fix |
|---|---|---|
| `Port 8501 is already in use` | A | Use `--server.port` flag |
| Terminal says "running" but no browser | B | Open URL manually |
| Connection refused from another device | C | Uncomment `address` in config.toml |
| CORS error in browser DevTools | D | Uncomment `enableCORS` in config.toml |
| Something else entirely | — | Run `streamlit hello` to verify environment |

### Still stuck? Environment sanity checks

If none of the above match, verify your basics:

1. `python --version` — should be 3.7 or later.
2. `streamlit --version` — should print a version number.
3. `streamlit hello` — if the built-in demo works, the problem is in the app code, not your setup.

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
