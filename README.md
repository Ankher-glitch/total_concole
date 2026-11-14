# 提效应用台（Python + pywebview）

## 运行环境

- Python 3.9+
- 推荐 Python 3.10 或更高版本

## 安装依赖

```bash
pip install pywebview
```

Windows 如果安装后启动提示缺少 WebView2，请安装 Microsoft Edge WebView2 Runtime。

## 运行

在 PyCharm 中打开本目录，右键 `app.py`，选择 `Run 'app'`。

或在终端执行：

```bash
python app.py
```

## 功能

- 行业切换和搜索
- 新建行业
- 新增应用入口
- 编辑应用名称、描述、分类标签
- 独立访问应用按钮
- 销售行业中的销售数据分析默认访问地址为 `http://localhost:3000`

访问按钮打开的是当前电脑上的地址。使用前请确保本机 3000 端口已有程序运行。
