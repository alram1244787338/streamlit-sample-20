"""Streamlit Simple Sample App.

A minimal, self-explanatory Streamlit page used as a starter template.

Run it with:
    streamlit run run.py

Then open http://localhost:8501 in your browser.

The user-facing strings below (APP_TITLE / APP_DESCRIPTION) are the single
source of truth and are mirrored in README.md. ``test_consistency.py`` checks
that the page and the documentation never drift apart.
"""

import streamlit as st

# --- Single source of truth for user-facing text -------------------------
APP_TITLE = "Streamlit Simple Sample App"
APP_DESCRIPTION = "This is a minimal working example of a Streamlit web app."
RUNNING_MESSAGE = "The app started successfully — Streamlit is running."
LOCAL_URL = "http://localhost:8501"


def render() -> None:
    """Render the sample page."""
    st.set_page_config(page_title=APP_TITLE, page_icon="✅")

    st.title(APP_TITLE)
    st.caption(APP_DESCRIPTION)

    # Make it unmistakable that this is a working sample, not a placeholder
    # or an app that failed to start.
    st.success(RUNNING_MESSAGE)
    st.write(
        "If you can read this page in your browser, your local Streamlit "
        "setup works. Everything here is sample/demo content — not a "
        "placeholder and not an error state."
    )

    # A tiny interactive widget so first-time visitors can see Streamlit
    # actually doing something.
    st.subheader("Try it")
    name = st.text_input("Your name", value="world")
    st.write(f"Hello, {name}! 👋")

    st.divider()
    st.markdown(
        f"- **Local URL:** [{LOCAL_URL}]({LOCAL_URL})\n"
        "- **Entry point:** `run.py`\n"
        "- **Docs:** `README.md` (English) · `README_ja.md` (日本語)"
    )


if __name__ == "__main__":
    render()
