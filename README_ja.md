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

または、`requirements.txt` からまとめてインストール：

```bash
pip install -r requirements.txt
```

---

## 🚀 アプリの実行方法

以下のコマンドでアプリを起動します：

```bash
streamlit run run.py
```

ブラウザが自動的に開きます。開かない場合は以下にアクセスしてください：
http://localhost:8501

> **注意:** グローバルの `~/.streamlit/config.toml` を変更する必要はありません。このプロジェクトには適切なデフォルト値が設定された `.streamlit/config.toml` が含まれています。

---

## ⚠️ うまく動かない場合

問題の内容に合わせて、該当する項目だけを試してください。**すべてを行う必要はありません。**

### 症状 1：「Port 8501 is already in use」と表示される

ポート 8501 が他のプロセスに使われています。別のポートで起動してください：

```bash
streamlit run run.py --server.port 8502
```

起動後、http://localhost:8502 にアクセスしてください。

### 症状 2：ブラウザが自動で開かない

WSL やリモートサーバーなどの環境では正常な動作です。ブラウザを手動で開き、http://localhost:8501 にアクセスしてください。

自動起動のプロンプトを今後表示したくない場合は、`.streamlit/config.toml` の `headless = true` のコメントアウトを外してください。

### 症状 3：同じネットワーク内の別の端末からアクセスしたい

デフォルトでは Streamlit は `localhost` でのみリッスンしています。LAN 内の他のデバイスからの接続を許可するには、`.streamlit/config.toml` の以下の行のコメントアウトを外してください：

```toml
[server]
address = "0.0.0.0"
```

その後、マシンの IP アドレスを使ってアクセスしてください（例：`http://<あなたのIP>:8501`）。

> **重要:** 信頼できるネットワーク内でのみ行ってください。Streamlit を直接インターネットに公開しないでください。

### 症状 4：ブラウザのコンソールに CORS エラーが出る

リバースプロキシの背後や特定のクラウド環境で発生することがあります。**最終手段として**、`.streamlit/config.toml` の以下の行のコメントアウトを外してください：

```toml
[server]
enableCORS = false
```

ローカル開発（`localhost`）では、この設定を変更する必要は**ありません**。

### それでも動かない場合

以下のクイックチェックを試してください：

1. **Python はインストールされていますか？** `python --version` を実行（3.7 以上であること）。
2. **Streamlit はインストールされていますか？** `streamlit --version` を実行。
3. **組み込みデモは動きますか？** `streamlit hello` を実行 — これで動くなら、問題はアプリコード側にあり、環境の問題ではありません。

---

## 📁 ファイル構成

```
.
├── .streamlit/
│   └── config.toml      # プロジェクト固有の Streamlit 設定（グローバル変更不要）
├── run.py               # Streamlit アプリの本体
├── requirements.txt     # 使用ライブラリ一覧
├── README.md            # 英語版
├── README_ja.md         # 本ファイル（日本語版）
└── README_zh.md         # 中国語版
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
