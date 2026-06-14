# Streamlit 简单示例应用

本仓库提供了一个使用 Python 库 Streamlit 构建的简单 Web 应用示例。

---

## ✅ 概述

Streamlit 是一个开源库，只用 Python 代码就能构建数据应用。

---

## 🧰 环境要求

* Python 3.7 或更高版本
* pip

---

## 📦 安装方法

使用以下命令安装所需的库：

```bash
pip install streamlit
```

---

## 🚀 运行方法

使用以下命令启动应用：

```bash
streamlit run run.py
```

启动后，访问：
[http://localhost:8501](http://localhost:8501)

---

## ⚠️ 排查问题

正常的本地环境下，只需 `streamlit run run.py` 即可运行，**无需修改任何配置文件**。如果遇到问题，请按下面的症状对号入座。每个处理方法都只是一次性的命令行参数，不会改动你全局的 Streamlit 配置。

### 端口 8501 被占用

症状：出现类似 `Port 8501 is already in use` 的错误，或者 `localhost:8501` 显示的是另一个应用。

处理 —— 仅本次运行换一个端口：

```bash
streamlit run run.py --server.port 8502
```

然后打开 [http://localhost:8502](http://localhost:8502)。

### 浏览器没有自动打开

启动时，Streamlit 会在终端打印本地 URL，例如：

```
Local URL: http://localhost:8501
```

在浏览器里手动打开这个 URL 即可，无需任何配置。
（如果是在远程服务器上、根本不希望弹出浏览器，可加上 `--server.headless true`。）

### 需要从另一台设备访问

默认情况下，应用只能从本机（`localhost`）访问，这对示例来说是最安全的设置。只有当你确实需要从**同一可信网络**中的另一台设备访问时，才在本次运行里绑定到所有网络接口：

```bash
streamlit run run.py --server.address 0.0.0.0
```

然后在另一台设备上打开 `http://<本机IP>:8501`。
注意：这会把应用暴露到你的局域网，请只在可信网络中这样做，并检查防火墙设置。

### 仍然无法解决？（进阶）

如果你确实需要把某项设置长期保留，请使用**项目内**配置，而不是 `~/.streamlit/config.toml`，以免污染全局环境。在本项目文件夹内创建 `.streamlit/config.toml`：

```toml
[server]
port = 8501
```

从项目目录运行时，Streamlit 会自动读取它。除非你打算改变本机上*所有*项目的 Streamlit 行为，否则请不要编辑 `~/.streamlit/config.toml`。

---

## 📁 文件结构

```
.
├── run.py             # Streamlit 应用主文件（运行的就是它）
├── requirements.txt   # 锁定版本的依赖列表
├── README_zh.md       # 本文件（中文）
├── README_ja.md       # 日文 README
└── README.md          # 英文 README
```

---

## 📌 补充说明

Streamlit 非常适合快速原型开发和数据可视化。
它也支持构建更复杂、更定制化的应用，欢迎自由探索。

---

## 📚 参考

* [https://streamlit.io/](https://streamlit.io/)

---

如有任何问题，请提交 issue。
