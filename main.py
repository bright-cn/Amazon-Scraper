import asyncio
import click
import logging
from amazon_scraper.scraper import amazon_shopping_search
from amazon_scraper.utils import setup_logging


@click.command()
@click.argument("search_query", required=True)
@click.option("--domain", default="com", help="Amazon domain to use (default: com)")
@click.option(
    "--pages",
    type=int,
    default=None,
    help="Number of pages to scrape (default: scrape all pages)",
)
def scrape_amazon(search_query, domain, pages):
    """Amazon product scraper CLI."""

    # Enable both file logging and console output
    setup_logging(console_output=True)

    logger = logging.getLogger(__name__)

    logger.info(f"Starting Amazon scraping for query: {search_query}")

    try:
        # Run the scraper function with provided or default arguments
        asyncio.run(
            amazon_shopping_search(
                search_query=search_query, domain=domain, max_pages=pages
            )
        )
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    scrape_amazon()
