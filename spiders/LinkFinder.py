import scrapy
import pandas as pd
import numpy as np
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor, defer
from scrapy.utils.log import configure_logging

class LinkFinderSpider(scrapy.Spider):
    name = "LinkFinder"
    start_urls = ['https://www.linux.org/forums/']
    columns = ['Current Add', 'Current Page Title','Anchor Add','Anchor Text']

    def parse(self, response):
        links = np.array(self.getLinksOnPage(response)) # Converts it into a numpy array

        
        df = pd.DataFrame(links) # Converts it into a data frame

       # print(links)
        print(df)
        


    def getLinksOnPage(self, response):
        # The variable are in a form of array that will be converted to a 2d array after extracting
        currentURL = [response.url] # get the current page URL
        pageTitle = [response.xpath("//head/title/text()").get()] # Get the current page title
        anchorLinks = []
        anchorText = []
        
        for link in response.xpath('//a'):
            # For every link in this page, extract the link, the current page URL and the title
            anchorLinks += [link.xpath('@href').get()]
            currentURL += [currentURL[0]]
            pageTitle += [pageTitle[0]]

            # Checks whether does the link has a link text or not
            currAncText = link.xpath('text()').get()
            if currAncText:
                anchorText += [currAncText]
            else:
                anchorText += [' '] # if the link text is null then set it as empty string
            
        # Convert them into a 2D numpy array    
        mergedArray = list(zip(currentURL, pageTitle, anchorLinks, anchorText))
        mergedArray.insert(0, self.columns)

        # Return the zipped 2D array
        return mergedArray   
       

# Scripts to run this on its own
configure_logging()
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(LinkFinderSpider())
process.start()