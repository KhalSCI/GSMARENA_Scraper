# Phone Scraper

This project is a web scraping application built using **Scrapy** to extract phone specifications and pricing information from **GSMArena**. The scraper navigates through the website, collects data on various phone models, and exports the data to **JSON** and **CSV** files.

## Table of Contents
- [Installation](#installation)
- [ScrapeOps API for Proxy Management](#scrapeops-api-for-proxy-management)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/phone-scraper.git
   cd phone-scraper
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
## ScrapeOps API for Proxy Management

**Important:** GSMArena imposes strict rate limits and may ban your IP address after just a few requests. To avoid this, we recommend using **ScrapeOps** for proxy management to rotate IPs automatically.

### Setting Up ScrapeOps

1. **Sign up for ScrapeOps**  
   Go to [ScrapeOps](https://scrapeops.io) and create an account to get an API key for proxy services.

2. **Configure ScrapeOps in Scrapy**

   In your `settings.py` file, add the following configuration:

   ```python
   # ScrapeOps API Key (replace with your key)
   SCRAPEOPS_API_KEY = 'your_scrapeops_api_key'

   # Enable ScrapeOps Proxy Middleware
   DOWNLOADER_MIDDLEWARES = {
       'scrapeops_scrapy_proxy_sdk.scrapeops.ScrapeOpsProxyMiddleware': 725,
   }

   # Set up ScrapeOps proxy settings
   SCRAPEOPS_PROXY_ENABLED = True

## Usage
   **To run the Scrapy spider and start scraping data from GSMArena, use the following command:**
   ```bash
   scrapy crawl phonespider
   ```
   **Output Files:**
   The scraped data will be saved as data.json and data.csv files in the project directory.
## Project-Structure
   ```bash
phone_scraper/
│
├── scrapy.cfg                 # Scrapy project configuration file
├── data/
│   ├── data_final_final.csv   # Scraped data exported in CSV format
│   └── data.json              # Scraped data exported in JSON format
├── phones/
│   ├── __init__.py            # Python package initializer
│   ├── items.py               # Defines the data structure for scraped items
│   ├── middlewares.py         # Custom middlewares for handling requests/responses
│   ├── pipelines.py           # Pipelines for processing/exporting scraped data
│   ├── settings.py            # Scrapy project settings and configurations
│   └── spiders/
│       └── phonespider.py     # Main spider to scrape phone data from GSMArena
│
├── requirements.txt    
└── README.md                  
```
## Configuration

The Scrapy settings can be configured in the `settings.py` file. Key configurations include:

- **FEEDS**: Specifies the output format and filenames for the scraped data.
- **DOWNLOADER_MIDDLEWARES**: Configures custom downloader middlewares.
- **ITEM_PIPELINES**: Configures item pipelines for processing scraped data.

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit your changes:
   ```bash
   git commit -am 'Add some feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/your-feature
   ```
5. **Create a new Pull Request.**
## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.



