import streamlit as st

# -- Page configuration --
st.set_page_config(
    page_title="Streamlit Sample App",
    page_icon="👋",
    layout="centered",
)

# -- Multilingual content --
CONTENT = {
    "en": {
        "title": "Streamlit Sample App",
        "status": "The application is running successfully.",
        "intro": (
            "Welcome! This sample application demonstrates a working web app "
            "built with [Streamlit](https://streamlit.io/). "
            "Your environment is configured and ready to go. "
            "Use the sidebar to switch between English and Japanese."
        ),
        "next_header": "What's next?",
        "next_steps": (
            "1. Edit `run.py` to customize this page\n"
            "2. Add new pages under a `pages/` folder — Streamlit will pick "
            "them up automatically\n"
            "3. Check `README.md` for installation and configuration details"
        ),
        "run_header": "How to run",
        "run_cmd": "streamlit run run.py",
        "sidebar_header": "Language",
        "footer": "See `README.md` for installation and configuration details.",
    },
    "ja": {
        "title": "Streamlit サンプルアプリ",
        "status": "アプリは正常に動作しています。",
        "intro": (
            "ようこそ！このサンプルアプリは "
            "[Streamlit](https://streamlit.io/) で構築された、"
            "動作確認済みの Web アプリです。"
            "環境は正しく設定されています。"
            "サイドバーから英語と日本語を切り替えることができます。"
        ),
        "next_header": "次のステップ",
        "next_steps": (
            "1. `run.py` を編集してページをカスタマイズ\n"
            "2. `pages/` フォルダに新しいページを追加 — "
            "Streamlit が自動的に認識します\n"
            "3. インストールや設定の詳細は `README_ja.md` を参照"
        ),
        "run_header": "起動方法",
        "run_cmd": "streamlit run run.py",
        "sidebar_header": "言語",
        "footer": "インストールや設定の詳細は `README_ja.md` を参照してください。",
    },
}

# -- Sidebar: language selector --
lang_labels = {"English": "en", "日本語": "ja"}
lang_display = st.sidebar.selectbox(
    "Language / 言語", list(lang_labels.keys()), index=0
)
lang = lang_labels[lang_display]
t = CONTENT[lang]

# -- Main page --
st.title(t["title"])
st.success(t["status"])
st.markdown(t["intro"])

st.markdown(f"### {t['next_header']}")
st.markdown(t["next_steps"])

with st.expander(t["run_header"]):
    st.code(t["run_cmd"], language="bash")

st.caption(t["footer"])
