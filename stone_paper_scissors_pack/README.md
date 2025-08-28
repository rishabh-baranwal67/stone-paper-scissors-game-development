
# Stone • Paper • Scissor (Python)

Three ways to play:

1. **CLI** — `python sps_cli.py`
2. **Desktop GUI (Tkinter)** — `python sps_tkinter.py`
3. **Web App (Streamlit)** — `streamlit run app.py` (inside `streamlit_app/`)

## Quick Start

```bash
# 1) CLI
python sps_cli.py

# 2) Tkinter GUI
python sps_tkinter.py  # Tkinter comes with Python on Windows/macOS; on Linux: sudo apt install python3-tk

# 3) Streamlit Web App (local)
cd streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

## One-Click Online Deployment (Free)

### Option A: Streamlit Community Cloud
1. Push the `streamlit_app` folder to a public GitHub repo.
2. Go to https://share.streamlit.io/ → "New app".
3. Select your repo/branch and set **Main file path** to `streamlit_app/app.py`.
4. Deploy. You’ll get a public URL.

### Option B: Render (Free Web Service)
1. Push `streamlit_app` to GitHub.
2. Create a new **Web Service** at https://render.com
3. Build command: `pip install -r requirements.txt`
4. Start command: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

## Make a Windows Executable (Offline Desktop)
Use PyInstaller to create an `.exe` for the Tkinter app.
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile sps_tkinter.py
# The .exe will appear in the dist/ folder
```

## Files
- `sps_cli.py` — terminal version
- `sps_tkinter.py` — desktop GUI version
- `streamlit_app/app.py` — web version
- `streamlit_app/requirements.txt` — dependencies for web
