from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape_coveo_links(url):
    # Set up the WebDriver with the command line flag for Edge
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('--enable-chrome-browser-cloud-management')

    driver = webdriver.Edge(options=edge_options)

    try:
        # Make a request using Selenium
        driver.get(url)

        # Wait for the dynamic content to load (you may need to adjust the sleep duration)
        time.sleep(5)

        # Get the page source after dynamic content has loaded
        page_source = driver.page_source

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all the links with class 'coveo'
        coveo_links = soup.find_all('a', class_='CoveoResultLink')

        # Extract and write the href attribute of each coveo link to a file
        with open("coveo_links.txt", "a") as file:
            for link in coveo_links:
                href = link.get('href')
                if href:
                    file.write(href + '\n')

        # Print the total number of coveo links
        print(f"Total number of Coveo class links: {len(coveo_links)}")
        print("Coveo class links saved to 'coveo_links.txt'")

    finally:
        # Close the WebDriver in a 'finally' block to ensure it is closed even if an exception occurs
        driver.quit()

# Example usage
count = 2
while(count>=0):
    url = f"https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#first={count*100}&sort=%40refreadingcurriculumyear%20descending&numberOfResults=100"
    scrape_coveo_links(url)
    count = count - 1    
# url1 = "https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending&numberOfResults=100"
# url2 = "https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#first=100&sort=%40refreadingcurriculumyear%20descending&numberOfResults=100"
# url3 = "https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#first=200&sort=%40refreadingcurriculumyear%20descending&numberOfResults=100"
# scrape_coveo_links(url1)
# scrape_coveo_links(url2)
# scrape_coveo_links(url3)
