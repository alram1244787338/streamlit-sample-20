# Streamlit 簡単サンプルアプリ

このリポジトリでは、Python ライブラリの Streamlit を使ったシンプルな Web アプリの例を紹介しています。

---

## ✅ 概要

Streamlit は、Python コードだけでデータアプリケーションを作成できるオープンソースのライブラリです。

---

## 🧰 必要な環境

* Python 3.10 以上（固定された依存ライブラリ、例: `numpy==2.2.6` が必要とするため）
* pip

---

## 📦 インストール方法

`requirements.txt` に固定されたライブラリをインストールします：

```bash
pip install -r requirements.txt
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

---

## ⚠️ うまく動かない場合

上記の 2 つのコマンドだけでローカル実行は可能です。以下の手順は**任意**で、
カスタムのホスト/ポートで公開したい場合（例: リモートサーバー）のみ必要です。

デフォルトの設定ファイルを生成します（新しい環境でもリダイレクトが失敗しない
よう、先にディレクトリを作成します）：

```bash
mkdir -p ~/.streamlit
streamlit config show > ~/.streamlit/config.toml
```

お好きなエディタ（ここでは nano）で `~/.streamlit/config.toml` を開き、
サーバー設定を修正します：

```toml
[server]
headless = true
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
├── run.py            # Streamlit アプリ本体（エントリーポイント）
├── requirements.txt  # 固定された依存ライブラリ一覧
├── README.md         # 英語版
└── README_ja.md      # 本ファイル（日本語版）
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

