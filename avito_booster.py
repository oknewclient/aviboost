from playwright.async_api import async_playwright
import asyncio

async def promote_ad(city, search_query):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.avito.ru/")
        await page.click("button[data-marker='location/region-select']")
        await page.fill("input[placeholder='Поиск']", city)
        await page.keyboard.press("Enter")
        await asyncio.sleep(3)
        await page.fill("input[data-marker='search-form/suggest']", search_query)
        await page.keyboard.press("Enter")
        await asyncio.sleep(4)
        await browser.close()
