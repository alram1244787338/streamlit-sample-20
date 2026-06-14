# Streamlit 簡単サンプルアプリ

このリポジトリでは、Python ライブラリの Streamlit を使ったシンプルな Web アプリの例を紹介しています。

---

## ✅ 概要

Streamlit は、Python コードだけでデータアプリケーションを作成できるオープンソースのライブラリです。

---

## 🧰 必要な環境

* Python 3.7 以上
* pip

---

## 📦 インストール方法

以下のコマンドで必要なライブラリをインストールできます：

```bash
pip install streamlit
```

---

## 🚀 アプリの実行方法

以下のコマンドでアプリを起動します：

```bash
streamlit run run.py
```

実行後、
http://localhost:8501
にアクセスしてください

**「Streamlit サンプルアプリ」** というタイトルのページが表示され、アプリが正常に動作していることを示す緑色のバナーが表示されます。サイドバーから英語と日本語を切り替えることができます。

---

## ⚠️ うまく動かない場合

以下のコマンドを実行して
```bash
streamlit config show > ~/.streamlit/config.toml
```

お好きなエディタ(ここではnano)で~/.streamlit/config.tomlを開いて
以下の部分を修正、もしくは追加
```bash
nano ~/.streamlit/config.toml
```
```~/.streamlit/config.toml
[server]
headless = true
enableCORS = false
port = 8501
address = "0.0.0.0"
```
再実行
```bash
streamlit run run.py
```
---

## 📁 ファイル構成

```
.
├── run.py                 # Streamlit アプリの本体
├── requirements.txt       # 使用ライブラリ一覧
├── check_consistency.py   # ページ文案とREADMEの整合性チェック
├── README_ja.md           # 本ファイル
├── README.md              # 英語版README
└── .gitignore             # Git除外設定
```

---

## 📌 補足

Streamlit は高速なプロトタイピングやデータ可視化に非常に便利です。
より複雑なアプリやカスタマイズも可能ですので、ぜひ活用してください。

---

## 📚 参考

* [https://streamlit.io/](https://streamlit.io/)

---

ご不明点があれば issue を立ててください。

