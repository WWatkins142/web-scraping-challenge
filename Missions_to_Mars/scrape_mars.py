# imports
# import Splinter, BeautifulSoup and Chrome Driver
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# scrape all function
def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # return json that has all of neccessary data  to load into MongoDB

    # stop webdriver
    browser.quit()
# scrape Mars News page

# scrape through Featured Image page

# scrape through Facts Page

# scrape through Hemisperes pages

# set up as Flask App
if __name__=="__main__":
    print(scrape_all())