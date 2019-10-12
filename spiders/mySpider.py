# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from aScrapper.items import AscrapperItem
from scrapy.utils.log import configure_logging

## scrapy crawl mySpider -o links.json

class MyspiderSpider(CrawlSpider):
    name = 'mySpider'
    # allowed_domains = ['forum.lowyat.net', 'forum.xda-developers.com']
    start_urls = ['https://forum.lowyat.net/', 'https://forum.xda-developers.com/']

  
    # def parse(self, response):
    #     links = LinkExtractor(
    #         canonicalize=True,
    #         unique=True).extract_links(response)

        

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url, self.parse)

    def parse(self, response):
        classNames = {}
        links = []
        numOfLinksLimit = 10
        numOfClassLimit = 2

        # Get the title of the page the crawler is visiting
        pageTitle = response.xpath("//head/title/text()").get()

        # Count the occurance of all the class in the HTML
        for names in response.xpath("//@class").getall():
            if names not in classNames:
                classNames[names] = 1
            else:
                classNames[names] += 1

        # Sort the class occurance in decensing order
        classNamesSorted = sorted(classNames, key=classNames.get, reverse = True)

        # Get the number of links defined in numOfLinksLimit with respect to the number of class to use - numOfClassLimit
        for i in range(numOfClassLimit):
    
            links += response.xpath("//*[@class='"+ classNamesSorted[i] +"']//a/@href").getall()[:numOfLinksLimit]

       
        # print(classNames[classNamesSorted[1]] + classNames[classNamesSorted[0]])
        
        self.printDebug("DEBUG Start")
        print(classNames)
        print(classNamesSorted)
        print(pageTitle)
        print(links)
        print(len(links))
        self.printDebug("END OF DEBUG")

        
        i = 0
        for link in links:
            i +=1
            yield {i : link}
           
        # items = []


        # links = LinkExtractor(
        #     allow=self.allowed_domains,
        #     canonicalize=True,
        #     unique=True
        #     ).extract_links(response)


        # # Now go through all the found links
        # for link in links:
        #     print (link)


        #     item = AscrapperItem()
        #     item['FoundLinks'] = link.url
        #     items.append(item)
        # # Return all the found items
        # return items


    def printDebug(self, message):
        print("\n***********************************************\n" +
             "    *************"+ message +"*************\n" +
                 "***********************************************" )
