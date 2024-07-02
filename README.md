# Jumia Product Scraper

This Flask application allows users to search for products on Jumia and scrape information such as product names, prices, and images. The app uses Selenium to automate the web scraping process.

## Features

- Search Functionality: Users can enter a product name to search on Jumia.

- Web Scraping: The app uses Selenium to scrape product details (names, prices, and images) from the Jumia website.

- Dynamic Loading: The script scrolls the page until all products are loaded, ensuring comprehensive scraping.

-Error Handling: Handles stale element reference exceptions to ensure reliable scraping.

## Requirements

- Python 3.x

- Flask

- Selenium

- Chrome WebDriver

- WebDriver Manager for Chrome

## Installation

Clone the repository:

   ```bash
  git clone https://github.com/yourusername/jumia-product-scraper.git
  ```

```bash 
bashcd jumia-product-scraper
```

Install the required packages:

```bash 
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

## Usage

Navigate to ```http://192.168.1.106``` in your web browser.

Enter the name of the product you want to search for and click the search button.

The application will scrape the product names, prices, and images from Jumia and display them on the page.

## Code Explanation

The application consists of a single Flask route that handles both GET and POST requests. When a POST request is made (i.e., when the user submits a search query), the app uses Selenium to:

Open the Jumia website.

Close any pop-ups.

Enter the search query and submit the search form.

Scroll down the page until all products are loaded.

Scrape product names, prices, and images.

Render the scraped data on the results page.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

License

This project is licensed under the MIT License.


