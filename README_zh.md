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

> **大多数情况下，`streamlit run run.py` 直接就能跑，无需改任何配置。**
> 本项目自带的 `.streamlit/config.toml` 中所有选项都是注释状态；Streamlit 内置默认值对本地开发完全够用。**不要去改全局的 `~/.streamlit/config.toml`。**
>
> 如果遇到问题，请对照下表定位你的情况，**只尝试对应的修复方案**。

### 先做快速自检（改配置之前先看这里）

在修改任何配置之前，先缩小问题范围：

1. **Streamlit 本身能跑吗？** 试试 `streamlit hello` —— 如果内置 Demo 能跑，说明环境没问题，问题出在应用代码。
2. **浏览器能访问这个地址吗？** 手动打开 [http://localhost:8501](http://localhost:8501)。如果能加载，说明应用在正常运行，你只是没自动弹出浏览器。
3. **命令在启动时就报错了？** 看终端里的报错信息。最常见的是端口冲突，见下方。

### 场景 A：提示 "Port 8501 is already in use"

端口 8501 被其他程序占用了。两种修复方式，任选其一：

* **命令行参数（最快，不用改文件）：**

  ```bash
  streamlit run run.py --server.port 8502
  ```

  然后访问 [http://localhost:8502](http://localhost:8502)。

* **持久修改：** 在 `.streamlit/config.toml` 中取消注释 `port = 8501`，改成你想要的端口号。

### 场景 B：应用在跑，但浏览器没弹出来

在 WSL、SSH、Docker 或其他无界面环境下这是正常的。手动打开浏览器，访问 [http://localhost:8501](http://localhost:8501) 即可。

如果希望以后也不弹浏览器，在 `.streamlit/config.toml` 中取消注释 `headless = true`。

### 场景 C：需要从同一局域网的其他设备访问

默认情况下，Streamlit 只绑定 `localhost`——其他机器无法连接。这是出于安全考虑的设计。

如需允许局域网访问，在 `.streamlit/config.toml` 中取消注释以下行：

```toml
address = "0.0.0.0"
```

然后用本机的局域网 IP 访问，例如 `http://192.168.x.x:8501`。

> **⚠️ 安全提示：** 这会把应用暴露给同一网络内的所有人。仅在可信网络中使用，绝对不要将 Streamlit 直接暴露到公网。

### 场景 D：浏览器控制台出现 CORS 错误

这只会在反向代理（nginx、Caddy）或某些云托管环境下出现。正常的本地开发**不会**遇到。

如果你确认属于这种情况，在 `.streamlit/config.toml` 中取消注释以下行：

```toml
enableCORS = false
```

> **本地 `localhost` 开发不需要改这个** —— 改了没有好处，反而会降低浏览器安全性。

### 速查：我该用哪个方案？

| 你看到的现象 | 场景 | 修复方式 |
|---|---|---|
| `Port 8501 is already in use` | A | 用 `--server.port` 参数 |
| 终端显示 "running" 但没弹浏览器 | B | 手动打开 URL |
| 从其他设备连接被拒绝 | C | 在 config.toml 中取消注释 `address` |
| 浏览器开发者工具报 CORS 错误 | D | 在 config.toml 中取消注释 `enableCORS` |
| 以上都不像 | — | 跑一下 `streamlit hello` 验证环境 |

### 还是不行？环境基础检查

如果上面的都不匹配，验证一下基础环境：

1. `python --version` —— 应该是 3.7 及以上。
2. `streamlit --version` —— 应该能输出版本号。
3. `streamlit hello` —— 如果内置 Demo 能跑，说明问题出在应用代码，不是环境问题。

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
