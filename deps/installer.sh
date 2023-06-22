# pyinstaller --onefile ../main.py --hidden-import="PIL._tkinter_finder"
pyinstaller --onefile ../blessed_tui.py --hidden-import="PIL._tkinter_finder"
