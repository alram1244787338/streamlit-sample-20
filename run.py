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
        "status": "✅ The application is running successfully.",
        "intro": (
            "This is a minimal demo built with "
            "[Streamlit](https://streamlit.io/). "
            "It shows that your environment is set up correctly "
            "and ready for further development."
        ),
        "run_header": "How to run",
        "run_cmd": "streamlit run run.py",
        "sidebar_header": "Language",
        "footer": "See `README.md` for installation and configuration details.",
    },
    "ja": {
        "title": "Streamlit サンプルアプリ",
        "status": "✅ アプリは正常に動作しています。",
        "intro": (
            "これは [Streamlit](https://streamlit.io/) で構築した"
            "最小限のデモアプリです。"
            "環境が正しくセットアップされ、"
            "開発を続けられる状態であることを示しています。"
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

with st.expander(t["run_header"]):
    st.code(t["run_cmd"], language="bash")

st.caption(t["footer"])
