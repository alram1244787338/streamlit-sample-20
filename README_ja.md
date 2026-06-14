# Streamlit 簡単サンプルアプリ

*他の言語で読む: [English (README.md)](README.md)*

このリポジトリでは、Python ライブラリの Streamlit を使ったシンプルな Web アプリの例を紹介しています。これは Streamlit Web アプリの最小限の動作サンプルです。

---

## ✅ 概要

Streamlit は、Python コードだけでデータアプリケーションを作成できるオープンソースのライブラリです。

---

## 👀 起動すると表示される内容

アプリを起動すると、ページには次の内容が表示されます。

* タイトル **Streamlit Simple Sample App**
* Streamlit が正常に動作していることを示す緑色のメッセージ
* 名前を入力するとあいさつを返す小さな入力欄

ページの内容はすべてサンプル（デモ）です。プレースホルダーでもエラー状態でもありません。アプリの画面は英語で、ドキュメントは英語（[README.md](README.md)）と日本語（本ファイル）で提供しています。

---

## 🧰 必要な環境

* Python 3.7 以上
* pip

---

## 📦 インストール方法

以下のコマンドで必要なライブラリをインストールできます：

```bash
pip install -r requirements.txt
```

Streamlit だけをインストールする場合：

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
[http://localhost:8501](http://localhost:8501)
にアクセスしてください。

タイトル、緑色の「正常に動作しています」メッセージ、あいさつ用の入力欄が表示されれば、サンプルは正しく動いています。

---

## ⚠️ うまく動かない場合

以下のコマンドを実行してください：

```bash
streamlit config show > ~/.streamlit/config.toml
```

お好きなエディタ（ここでは nano）で `~/.streamlit/config.toml` を開き、以下の部分を修正または追加します：

```bash
nano ~/.streamlit/config.toml
```

```toml
[server]
headless = true
enableCORS = false
port = 8501
address = "0.0.0.0"
```

その後、再実行します：

```bash
streamlit run run.py
```

---

## 📁 ファイル構成

```
.
├── run.py              # Streamlit アプリの本体（エントリーポイント）
├── requirements.txt    # 依存ライブラリ一覧
├── test_consistency.py # ページの文言が README と一致しているか確認
├── README.md           # 英語版
└── README_ja.md        # 本ファイル（日本語版）
```

---

## 🔍 ドキュメントとアプリの一致を確認する

ページの文言（`run.py`）と README が食い違っていないことを、追加の依存なしで確認できます：

```bash
python test_consistency.py
```

---

## 📌 補足

Streamlit は高速なプロトタイピングやデータ可視化に非常に便利です。
より複雑なアプリやカスタマイズも可能なので、このリポジトリをテンプレートとして活用してください。

---

## 📚 参考

* [https://streamlit.io/](https://streamlit.io/)

---

ご不明点があれば issue を立ててください。
