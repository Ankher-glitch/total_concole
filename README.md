# 提效应用台（Python + pywebview + MYSQL）

一个运行在本机桌面窗口中的行业效率软件入口管理工具。应用界面使用 HTML、CSS 和 JavaScript，桌面窗口由 Python + pywebview 提供，行业与应用数据保存在本地 MYSQL 数据库中。

> 本项目是桌面管理工具，不是在线托管服务。每位使用者的数据默认保存在自己的电脑，不会自动同步给其他人。

## 目录

- [项目简介](#项目简介)
- [功能](#功能)
- [项目优势](#项目优势)
- [运行环境与依赖](#运行环境与依赖)
- [快速开始](#快速开始)
- [在 PyCharm 中运行](#在-pycharm-中运行)
- [如何使用](#如何使用)
- [MYSQL 数据说明](#sqlite-数据说明)
- [项目结构](#项目结构)
- [常见问题](#常见问题)
- [当前版本说明与限制](#当前版本说明与限制)

## 项目简介

提效应用台用于把不同业务行业和团队使用的效率软件集中整理。使用者可以通过行业列表找到相关软件入口，并维护行业、应用说明和分类标签。

程序采用本地桌面应用方式运行：

- **Python**：启动桌面程序、提供本地数据库读写接口。
- **pywebview**：在原生桌面窗口中显示应用页面。
- **HTML / CSS / JavaScript**：实现交互界面。
- **SQL**：在本机持久保存行业与应用信息。

首次启动时，程序会在项目目录下创建 `data/efficiency_hub.db`，并导入初始行业与应用数据。

## 功能

### 行业管理

- 显示预置的主流行业分类。
- 根据行业名称搜索、筛选列表。
- 新建自定义行业。
- 点击行业切换对应的软件入口。
- 新建的行业会保存到本地 SQLite 数据库，关闭再启动后仍然存在。

当前预置行业包括：

- 互联网 / 科技
- 金融服务
- 制造业
- 教育
- 医疗健康
- 零售与电商
- 专业服务
- 内容与传媒
- 房地产 / 建筑
- 物流与交通
- 销售行业

### 应用入口管理

- 为当前行业新增应用入口。
- 编辑已有应用的名称、描述和分类标签。
- 卡片显示应用名称、说明和分类标签。
- 显示当前行业的应用数量。
- 应用数据保存到 SQL，重启后继续保留。

### 独立访问按钮

每张应用卡片都有独立的“访问应用”按钮：

- 配置了 HTTP 或 HTTPS 链接时，使用系统默认浏览器打开链接。
- 尚未配置链接时，显示未配置提示。
- 初始数据中“销售行业 → 销售数据分析”的链接为 `http://localhost:3000`。

`localhost` 指运行本桌面程序的那台电脑。该电脑必须已经在 3000 端口运行目标应用，否则浏览器会提示无法连接。

### 本地持久化

- 行业和应用数据保存到 SQL 数据库文件。
- 关闭程序后数据不会因退出而丢失。
- 不需要启动 PostgreSQL、MySQL 或其他数据库服务。

## 项目优势

1. **本机运行**：数据默认保留在使用者自己的电脑上，不需要把应用数据上传到第三方服务。
2. **依赖轻量**：SQL 由 Python 标准库 `sqlite3` 提供，数据库不需要单独安装。
3. **桌面窗口体验**：pywebview 在桌面窗口中显示网页式界面，界面由 HTML/CSS 构建，方便调整样式。
4. **方便扩展**：前端页面与 Python 数据层分开，后续可增加删除、排序、导入导出、搜索应用等功能。
5. **可移植**：可以通过 GitHub 分享源码，也可以在具备 Python 环境的电脑上运行。

## 运行环境与依赖

### 软件要求

- Python 3.9 或更高版本；建议 Python 3.10 或 3.11。
- Windows、macOS 或 Linux 桌面环境。
- Windows 上如果系统缺少 WebView2，需要安装 Microsoft Edge WebView2 Runtime。

### Python 第三方依赖

只需要：

```text
pywebview
```



不需要安装 Node.js、npm 或 pnpm；运行桌面版不需要执行 `pnpm install`。

## 快速开始

### 1. 获取项目

从 GitHub 仓库点击绿色 **Code** 按钮，然后选择 **Download ZIP**。下载后解压到普通文件夹。

检查目录结构，确保这些文件在同一项目根目录：

```text
pywebview_efficiency_hub/
├── app.py
├── database.py
├── seed.json
├── README.md
└── web/
    ├── index.html
    ├── styles.css
    └── app.js
```

不能只复制 `app.py`；它依赖同级的 `database.py`、`seed.json` 和 `web` 文件夹。

### 2. 安装 pywebview

打开终端并进入项目根目录，然后运行：

```bash
python -m pip install pywebview
```

如果 Windows 上的命令是 `py` 而不是 `python`，可执行：

```powershell
py -m pip install pywebview
```

### 3. 启动程序

在项目根目录运行：

```bash
python app.py
```

或在 Windows 使用：

```powershell
py app.py
```

程序启动后会弹出“提效应用台”桌面窗口。

## 在 PyCharm 中运行

1. 下载并解压项目 ZIP。
2. 打开 PyCharm，选择 **文件 → 打开**，选中项目根目录。
3. 选择 **文件 → 设置 → 项目：项目名 → Python 解释器**。
4. 如果没有解释器，选择 **添加解释器 → 添加本地解释器 → Virtualenv 环境 → 新建**，基础解释器选择 Python 3.10 或更高版本。
5. 在 PyCharm 底部打开 **终端**，确认终端路径是项目根目录。
6. 安装依赖：

   ```bash
   python -m pip install pywebview
   ```

7. 在 PyCharm 左侧项目文件列表中，右键 `app.py`，选择 **运行“app”**。

也可以在 PyCharm 终端中运行：

```bash
python app.py
```

### 验证依赖和 Python 环境

检查 Python 版本：

```bash
python --version
```

检查 pywebview 是否安装到当前解释器：

```bash
python -c "import webview; print('pywebview 安装成功')"
```

如果出现 `ModuleNotFoundError: No module named 'webview'`，请确认 PyCharm 项目解释器与安装依赖时使用的是同一个虚拟环境，再执行 `python -m pip install pywebview`。

## 如何使用

### 搜索行业

在左侧搜索框输入行业名称，列表会按输入内容筛选。清空搜索框可重新显示全部行业。

### 切换行业

点击左侧行业标签，右侧会显示该行业下的应用入口。

### 新建行业

点击左侧上方的“＋”或下方的“新建行业”，输入行业名称并确认。新行业创建后会自动成为当前选中行业，并写入 SQL。

### 新增应用

1. 选中目标行业。
2. 点击右侧“＋ 添加应用”按钮，或应用列表中的“添加新的应用”卡片。
3. 填写应用名称、描述和分类标签。
4. 点击“保存”。

### 编辑应用信息

点击应用卡片右上角的 `···`，修改应用名称、描述或分类标签，然后保存。

### 访问应用

点击应用卡片上的“访问应用”按钮。链接已配置时会由系统默认浏览器打开；没有链接时会显示提示。

> 当前版本的应用编辑弹窗没有访问链接输入框。预置链接来自 `seed.json` 的首次初始化数据。需要修改或添加链接时，可直接编辑 SQLite 数据库中的 `apps.url` 字段；如果你希望在界面里管理链接，需要后续增加相应的编辑表单和 Python API。

## MYSQL 数据说明

### 数据库文件位置

首次运行后自动创建：

```text
data/efficiency_hub.db
```

其中：

- `industries` 表保存行业名称、图标和颜色主题。
- `apps` 表保存行业关联的应用名称、描述、标签、卡片颜色和访问链接。
- `metadata` 表记录初始数据是否已导入。

### 备份数据

1. 关闭提效应用台。
2. 复制整个 `data` 文件夹，或至少复制 `data/efficiency_hub.db`。
3. 将副本保存到其他安全位置。

恢复时关闭程序，将备份的数据库文件放回项目的 `data` 目录，再启动程序。

### 重置初始数据

程序启动后不会用 `seed.json` 覆盖已有数据库。若要重新初始化：

1. 关闭程序。
2. 备份后删除 `data/efficiency_hub.db`。
3. 再次启动，程序会重新创建数据库并导入 `seed.json` 的初始数据。

删除数据库会移除当前本机保存的行业与应用数据，请先备份。

### 多人使用和同步

MYSQL 数据库默认只保存在本机，不会自动同步到 GitHub 或其他电脑。不要让多人直接在网络共享目录中同时打开同一个 SQL 文件。如果需要多人共享，建议将数据层改成后端 API + 服务端 PostgreSQL/MySQL。

## 项目结构

```text
项目根目录/
├── app.py                 # pywebview 窗口与 JavaScript-Python API
├── database.py            # MYSQL 初始化、读取和写入逻辑
├── seed.json              # 首次启动时导入的默认行业与应用
├── README.md              # 项目说明
├── .gitignore             # 忽略本地数据库、缓存和虚拟环境
├── data/
│   └── efficiency_hub.db  # 运行时自动创建的本地数据库，不应提交到 GitHub
└── web/
    ├── index.html         # 页面结构
    ├── styles.css         # 页面样式
    └── app.js              # 搜索、行业切换和应用交互
```

## GitHub 上传注意事项

建议在 `.gitignore` 中忽略本地数据库和 Python 环境：

```gitignore
data/
*.db
*.sqlite
*.sqlite3
__pycache__/
*.py[cod]
.venv/
venv/
.idea/
.DS_Store
Thumbs.db
```

上传代码前运行：

```bash
git status
```

确认 `data/efficiency_hub.db` 没有出现在待提交文件列表中。数据库可能包含个人或团队数据，不建议公开上传。

## 常见问题

### 找不到 `app.py`

先进入项目根目录。该目录必须同时包含 `app.py`、`database.py`、`seed.json` 和 `web` 文件夹。

### 找不到 `webview`

在 PyCharm 当前项目解释器对应的终端执行：

```bash
python -m pip install pywebview
```

### Windows 提示 WebView2 Runtime 缺失

安装 Microsoft Edge WebView2 Runtime，重新打开 PyCharm 后再运行 `app.py`。Windows 10/11 通常已包含该运行时。

### 点击访问应用没有打开网页

检查应用是否配置了有效的 HTTP/HTTPS 链接，并确认目标服务正在运行。`http://localhost:3000` 需要目标程序已经在本机 3000 端口启动。

### 关闭程序后新增数据消失

检查是否每次都运行同一个项目目录中的 `app.py`。数据库位于该项目的 `data/efficiency_hub.db`；如果你运行了另一个副本，它会使用另一个目录下的数据库。

### `pnpm install` 找不到 `package.json`

这是 Python 桌面版项目，不需要 pnpm。请在包含 `app.py` 的目录运行：

```bash
python -m pip install pywebview
python app.py
```

## 当前版本说明与限制

- 本项目是本机桌面管理工具，不是部署在公网的在线服务。
- SQLite 数据是本机独立数据，不提供自动云同步。
- 当前应用入口表单可新增、编辑名称、描述和分类标签。
- 当前界面未提供访问链接编辑、删除应用、删除行业和应用排序功能。
- 初始访问链接从 `seed.json` 导入到 SQLite；已有数据库初始化后，修改 `seed.json` 不会自动覆盖数据库中的数据。
- 访问应用按钮使用本机默认浏览器打开地址。

## 许可

如需公开分发，请根据项目实际用途补充 LICENSE，并确认项目中使用的图片、字体及其他资源具有相应使用许可。
