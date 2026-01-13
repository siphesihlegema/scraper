"""
this part is to show that we can use pyinstaller to package a playwright script
"""

PLAYWRIGHT_BROWSERS_PATH=0 playwright install chromium
pyinstaller -F main.py