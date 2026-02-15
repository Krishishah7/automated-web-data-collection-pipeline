import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import logging
import config


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

BASE_URL = config.BASE_URL

all_data = []
page = config.START_PAGE   # ✅ FIX 1

while True:
    url = BASE_URL.format(page=page)
    logging.info(f"Scraping page {page}")

    try:
        response = requests.get(url, timeout=config.TIMEOUT)

        if response.status_code != 200:
            logging.error("Request failed. Stopping scraping.")
            break

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        if not quotes:
            logging.info("No more quotes found. Scraping completed.")
            break

        for q, a in zip(quotes, authors):
            all_data.append({
                "Quote": q.text,
                "Author": a.text
            })

        page += 1

        # optional safety limit
        if config.MAX_PAGES and page > config.MAX_PAGES:
            logging.info("Reached max page limit. Stopping scraping.")
            break

    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred: {e}")
        break


timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{config.OUTPUT_DIR}/{config.FILENAME_PREFIX}_{timestamp}.csv"

df = pd.DataFrame(all_data)
df.to_csv(filename, index=False)

logging.info(f"Total quotes scraped: {len(df)}")
logging.info(f"Data saved to: {filename}")
