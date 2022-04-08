 # Web Scraping Challenge- Mission to Mars
For this project I built a web application that scrapes websites for data related to the Mission to Mars and displays the information in a single HTML page.    

![Mission_to_Mars_Screenshot](/Mission_to_Mars_Screenshot.png)  


## Step 1- Scraping
- Initial scraping performed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter
- [Jupyter notebook](/Missions_to_Mars/Mission_to_Mars-Starter.ipynb) used to complete all scraping and analysis tasks from the following websites.
  - [NASA Mars News](https://redplanetscience.com/)- Latest News Title and Paragraph Text 
  - [JPL Mars Space Images](https://spaceimages-mars.com/) - Featured Image
  - [Mars Facts](https://galaxyfacts-mars.com/)
  - [Mars Hemispheres](https://marshemispheres.com/)

## Step 2 - MongoDB and Flask Application
 - MongoDB with Flask templating was used to create a new HTML page that displays all of the information scraped from the Mission to Mars related websites above.
