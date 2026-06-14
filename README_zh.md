# Streamlit 简单示例应用

本仓库提供了一个使用 Python 库 Streamlit 构建的简单 Web 应用示例。

---

## ✅ 概述

Streamlit 是一个开源库，只需编写 Python 代码即可构建数据应用。

---

## 🧰 环境要求

* Python 3.7 及以上
* pip

---

## 📦 安装

使用以下命令安装所需的库：

```bash
pip install streamlit
```

也可以从 `requirements.txt` 安装全部依赖：

```bash
pip install -r requirements.txt
```

---

## 🚀 运行应用

使用以下命令启动应用：

```bash
streamlit run run.py
```

浏览器会自动打开。如果没有自动打开，请手动访问：
[http://localhost:8501](http://localhost:8501)

> **说明：** 无需修改全局的 `~/.streamlit/config.toml`。本项目自带了 `.streamlit/config.toml`，已包含合理的默认配置。

---

## ⚠️ 常见问题排查

遇到问题时，请根据你的具体症状选择对应的解决方法。**只需尝试匹配的那一步，不需要全部都做。**

### 症状 1：提示 "Port 8501 is already in use"

端口 8501 已被其他程序占用。换一个端口启动：

```bash
streamlit run run.py --server.port 8502
```

然后访问 [http://localhost:8502](http://localhost:8502)。

### 症状 2：浏览器没有自动打开

在某些环境（如 WSL、远程服务器）下这是正常的。手动打开浏览器，访问 [http://localhost:8501](http://localhost:8501) 即可。

如果希望以后也不弹出自动打开的提示，可以在 `.streamlit/config.toml` 中取消注释 `headless = true`。

### 症状 3：需要从同一局域网内的其他设备访问

默认情况下，Streamlit 只监听 `localhost`。如需允许局域网内其他设备的连接，在 `.streamlit/config.toml` 中取消注释以下行：

```toml
[server]
address = "0.0.0.0"
```

然后使用本机的 IP 地址访问，例如 `http://<你的IP>:8501`。

> **重要：** 仅在可信网络中使用此配置。不要将 Streamlit 直接暴露到公网。

### 症状 4：浏览器控制台出现 CORS 错误

通常在反向代理或某些云环境下会出现此问题。作为**最后手段**，可以在 `.streamlit/config.toml` 中取消注释以下行：

```toml
[server]
enableCORS = false
```

在本地 `localhost` 开发时，**不需要**修改此设置。

### 还是不行？

试试以下快速检查：

1. **Python 是否已安装？** 运行 `python --version`（应为 3.7+）。
2. **Streamlit 是否已安装？** 运行 `streamlit --version`。
3. **内置 Demo 能跑吗？** 运行 `streamlit hello` —— 如果能跑通，说明问题在应用代码，而非环境。

---

## 📁 文件结构

```
.
├── .streamlit/
│   └── config.toml      # 项目级 Streamlit 配置（无需修改全局配置）
├── run.py               # Streamlit 应用主文件
├── requirements.txt     # 依赖列表
├── README.md            # 英文版
├── README_ja.md         # 日文版
└── README_zh.md         # 本文件（中文版）
```

---

## 📌 补充说明

Streamlit 非常适合快速原型开发和数据可视化。
它也支持构建更复杂、更定制化的应用，欢迎探索。

---

## 📚 参考资料

* [https://streamlit.io/](https://streamlit.io/)

---

如有疑问，请提交 issue。
