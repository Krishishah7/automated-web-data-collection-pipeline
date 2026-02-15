# Automated Web Data Collection Pipeline

This project implements a real-world style web scraping pipeline using Python.  
It is designed to collect structured textual data from a paginated website in a reliable and automated manner.

## Use Case
- Dataset generation for text analysis and NLP
- Content aggregation from public websites
- Automated data ingestion for analytics pipelines

## Features
- Pagination handling (multi-page scraping)
- Robust error handling with timeouts
- Logging for monitoring execution
- Timestamped output files to preserve historical data
- Clean separation between exploration (notebook) and automation (script)

## Tech Stack
- Python
- Requests
- BeautifulSoup
- Pandas
- Jupyter Notebook
- Logging

## Project Structure
- notebooks/ : Development and exploratory scraping
- scripts/ : Production-style automated scraper
- data/ : Timestamped scraped datasets

## Workflow
1. Send HTTP requests to paginated pages
2. Parse HTML using BeautifulSoup
3. Extract structured data
4. Handle errors and stop conditions safely
5. Save output with timestamps for tracking

## How to Run
1. Create a virtual environment
2. Install dependencies using `pip install -r requirements.txt`
3. Run the scraper using `python scripts/scraper.py`

## Configuration-Driven Design

This project follows a configuration-driven approach, where all changeable values such as
target URLs, pagination settings, network timeouts, output paths, and logging behavior are
defined separately in a configuration file (`config.py`).

This design ensures that:
- Scraping behavior can be modified without changing core logic
- The scraper is easy to maintain and extend
- The same scraping engine can be reused for different targets

In real-world data pipelines, separating configuration from logic is a common best practice
to improve reliability and scalability.

## Output
- CSV files such as `quotes_YYYY-MM-DD_HH-MM-SS.csv`
- A sample output file (`quotes_sample.csv`) is included for reference

## Disclaimer
This project is for educational purposes and scrapes a public practice website.

## What I Learned
- Handling pagination in real-world websites
- Writing defensive scraping code with error handling
- Using logging for monitoring automated scripts
- Designing configuration-driven data pipelines
