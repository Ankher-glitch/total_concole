from pathlib import Path
import webview

BASE_DIR = Path(__file__).resolve().parent
WEB_DIR = BASE_DIR / "web"


if __name__ == "__main__":
    webview.create_window(
        "提效应用台 | Efficiency Hub",
        str(WEB_DIR / "index.html"),
        width=1200,
        height=780,
        min_size=(900, 620),
        resizable=True,
    )
    webview.start(debug=False)
