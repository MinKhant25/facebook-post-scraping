from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox()

# Go to the Facebook page
driver.get("url of Facebook page for scraping")

# Log in if necessary
time.sleep(5)  # Wait for the page to load and login manually if needed

# Scroll down to load posts (optional, depends on how many posts are visible)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(8)  # Wait for posts to load

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find posts by their specific class or tag and limit number of post to scrap
posts = soup.find_all('div', {'class': 'the class of the text you want to scrap'}, limit=12)
#The class of text can be found in Html of the page

# Extract text from posts
post_texts = [post.get_text() for post in posts]

# Output or save the text
for i, text in enumerate(post_texts):
    print(f"-{text}\n")

# Close the browser
driver.quit()
