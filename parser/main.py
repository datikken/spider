from playwright.async_api import async_playwright
import asyncio


async def parse(link):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        page.set_default_timeout(0)
        await page.goto(link)
        links = await page.query_selector_all("a")
        for link in links:
            print(await link.get_attribute('href'))
        await browser.close()

asyncio.run(parse('https://cointelegraph.com/'))