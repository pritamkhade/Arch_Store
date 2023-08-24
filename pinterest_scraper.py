import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scrape_pinterest_images(tags):
    url = "https://www.pinterest.com/search/pins/?q={}".format('+'.join(tags))
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed
    driver.get(url)
    
    # Scroll down to load more images (adjust the range as needed)
    for _ in range(5):  # Scroll down 5 times, you can adjust this
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for content to load
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()  # Close the browser window
    
    images = soup.find_all("img")
    image_urls = [img.get("src") for img in images if img.has_attr("src")]
    
    return image_urls

# Function to save URLs to CSV file
def save_urls_to_csv(image_urls, filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Image URLs"])
        writer.writerows([[url] for url in image_urls])

if __name__ == "__main__":
    from bs4 import BeautifulSoup
    from selenium import webdriver
    
    tags = input("Enter Pinterest tags (comma-separated): ").strip().split(",")
    image_urls = scrape_pinterest_images(tags)

    if image_urls:
        output_filename = "pinterest_images.csv"
        save_urls_to_csv(image_urls, output_filename)
        print(f"Image URLs saved to {output_filename}")
    else:
        print("No image URLs found.")
