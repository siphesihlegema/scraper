"""
This code show how we would run playwright code in the python repl,
because in the python repl we cant use 'with sync_playwight() as p'
we need to run the code line by line ourselves. As a result of
no longer having 'with ...' we need to start and end the playwright process ourselves
using 'playwright = sync_playwright().start(), and playwright.stop()'
"""

from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI
browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="example.png")
browser.close()
playwright.stop()