# this in an introduction to playwright and a simple example how to use it

# below ill explain the differance between asynchronous and synchronous versions of the Playwright API

"""
 this first part runs synchronous an the way it works is that:
    Each instruction blocks until it finishes
    Code runs step-by-step, top to bottom
    Simple mentalmodel
    """
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://playwright.dev")
    print(page.title())
    browser.close()

"""
 this first part runs asynchronous an the way it works is that:
    Instructions return promises
    You explicitly await operations
    Allow concurrent tasks(multiple pages, requests,waits)
    """

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main())