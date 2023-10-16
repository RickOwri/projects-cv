## Roche Job Listing Scraper

This is a Python script that uses the Scrapy library to scrape job listings from the Roche website (https://www.roche.com). It collects information about job titles, job locations, and application dates. The scraped data is stored in lists and dictionaries for further processing.

### How to Use

To use this script, follow these steps:

1. **Install Scrapy**: Make sure you have Scrapy installed. You can install it using pip:

   ```
   pip install scrapy
   ```

2. **Create a Scrapy Project**: If you haven't already created a Scrapy project, you can do so by running the following command:

   ```
   scrapy startproject myproject
   ```

   Replace `myproject` with the desired name of your project.

3. **Create a Spider**: Inside your Scrapy project directory, create a spider by running:

   ```
   scrapy genspider rochee www.roche.com
   ```

   This will generate a spider named `rochee` for scraping the Roche website.

4. **Replace Spider Code**: Replace the code in the generated `rochee.py` spider file with the code provided in the README.

5. **Run the Spider**: To start scraping job listings, run the spider using the following command:

   ```
   scrapy crawl rochee
   ```

6. **View the Results**: The scraped data will be displayed in the terminal and saved in the `total` list.

### Configuration

- The spider is configured to start scraping from the URL specified in the `start_urls` attribute. You can modify this URL to match your desired starting point.
- You can adjust the number of job listings to scrape (`nbpost`) and the number of pages to crawl (`nbpage`) in the `parse` method.

### Data Storage

- Job information is stored in the following lists:
  - `lieu_du_taf`: Contains job locations.
  - `date_candidature`: Contains application dates.
  - `poste1`: Contains job titles.
- The `total` list stores a formatted string for each job listing.
- Scraped data is also yielded as dictionaries in the Scrapy items format.

### Note

- The code provided in the README may require adjustments, especially regarding XPath expressions and URL formats, to work correctly with the specific Roche website structure.
- Make sure to follow ethical web scraping practices and respect the website's terms of service and robots.txt file when using this script.
