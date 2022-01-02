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

    # get the information from the news page
    news_title, news_paragaph = scrape_MarsNews(browser)

    # Build dictionary with information from scrapes
    mars_Data = {
        "newsTitle": news_title,
        "newsParagraph": news_paragaph,
        "featuredImage": scrape_FeaturedImage(browser),
        "facts": scrape_Facts(browser)
    }

    # stop webdriver
    browser.quit()

    # output
    return mars_Data

# scrape Mars News page
def scrape_MarsNews(browser):
    # Visit the Mars news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')
    # grab news title
    news_title = slide_elem.find('div', class_='content_title').get_text()
    # grab the paragraph for the hedline
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    # return title and paragraph for dictionary
    return news_title, news_p

# scrape through Featured Image page
def scrape_FeaturedImage(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_button = browser.find_by_tag('button')[1]
    full_image_button.click()

    # Parse the resulting html with soup
    html = browser.html
    image_soup = soup(html, 'html.parser')

     # find the relative image url
    img_url_rel = image_soup.find('img', class_='fancybox-image').get('src')
    
    # Use the base url to create an absolute url
    featured_image_url = f'https://spaceimages-mars.com/{img_url_rel}'

    # return image url
    return featured_image_url

# scrape through Facts Page
def scrape_Facts(browser):
    # Visit URL
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    # Parse the resulting html with soup
    html = browser.html
    facts_soup = soup(html, 'html.parser')

    # find the facts location
    facts_location = facts_soup.find('div', class_="diagram mt-4")
    factTable = facts_location.find('table') # grab html code for facts table

    # create empty string, add text then return
    Facts = ""

    Facts += str(factTable)

    return Facts

# scrape through Hemisperes pages

# set up as Flask App
if __name__=="__main__":
    print(scrape_all())