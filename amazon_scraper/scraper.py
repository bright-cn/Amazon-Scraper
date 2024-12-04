from playwright.async_api import async_playwright
import csv
import logging
import os
from .models import Product
import asyncio


async def retry(func, retries=3, *args, **kwargs):
    logger = logging.getLogger(__name__)
    for i in range(retries):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logger.warning(f"Attempt {i+1} failed: {e}")
            if i == retries - 1:
                logger.error(f"All {retries} retries failed.")
                raise e
            await asyncio.sleep(2)  # Optional delay before retrying


async def amazon_shopping_search(search_query, domain="com", max_pages=None):
    logger = logging.getLogger(__name__)

    q = search_query.replace(" ", "+")
    base_url = f"https://www.amazon.{domain}/s?k={q}"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        page_number = 1

        with open("amazon_data.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(Product.csv_headers())

            while True:
                url = f"{base_url}&page={page_number}"
                logger.info(f"Scraping page {page_number} at URL: {url}")

                try:
                    # Use retry logic for page navigation
                    await retry(
                        page.goto, retries=3, url=url, wait_until="domcontentloaded"
                    )

                    # Try waiting for the main content slot; capture a screenshot if it fails
                    try:
                        await page.wait_for_selector(".s-main-slot")
                    except Exception as e:
                        screenshot_path = f"screenshots/page_{page_number}_error.png"
                        os.makedirs("screenshots", exist_ok=True)
                        await page.screenshot(path=screenshot_path)
                        logger.error(
                            f"Error waiting for .s-main-slot on page {page_number}. Screenshot saved at {screenshot_path}"
                        )
                        raise e

                    products = await page.query_selector_all(".s-result-item")

                    for product in products:
                        product_data = await extract_product_data(product, domain)
                        if product_data:
                            writer.writerow(product_data.to_csv())
                except Exception as e:
                    logger.error(f"Error on page {page_number}: {e}")
                    break

                next_page = await page.query_selector(".s-pagination-next")
                if not next_page or (max_pages and page_number >= max_pages):
                    logger.info("No more pages to scrape or maximum pages reached.")
                    break

                page_number += 1

        logger.info("Scraping completed successfully.")
        await browser.close()


async def extract_product_data(product, domain):
    logger = logging.getLogger(__name__)
    try:
        name = await product.query_selector("[data-cy=title-recipe]")
        current_price = await product.query_selector(".a-price > .a-offscreen")
        rating = await product.query_selector("[data-cy=reviews-ratings-slot]")
        reviews = await product.query_selector(
            "span[aria-label*='ratings'] a span.a-size-base"
        )
        asin = await product.get_attribute("data-asin")
        link_element = await product.query_selector("a.a-link-normal")

        if name and link_element:
            name_text = await name.inner_text()
            full_link = await link_element.get_attribute("href")
            link = f"https://www.amazon.{domain}{full_link.split('/ref=')[0]}"
            return Product(
                name=name_text,
                current_price=(
                    await current_price.inner_text() if current_price else "N/A"
                ),
                rating=await rating.inner_text() if rating else "N/A",
                reviews=await reviews.inner_text() if reviews else "N/A",
                asin=asin,
                link=link,
            )
    except Exception as e:
        logger.error(f"Error extracting product data: {e}")
        return None
