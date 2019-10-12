import os
import datetime
from scrapy.cmdline import execute


# filename = currDateTime.strftime("%d:%m|%H:%M:%S.json")
# print(filename)

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    execute(
        [
            'scrapy',
            'crawl',
            'LinkFinder',
            '-o',
            'Results %(time)s.json',
        ]
    )
except SystemExit:
    pass

# from verbalexpressions import VerEx

# veEx = VerEx()
# string = [
#     "https://forum.lowyat.net/FinanceBusinessandInvestmentHouse",
#     "https://forum.lowyat.net/StockExchange",
#     "https://forum.lowyat.net/topic/4475872/+40"
# ]


# tester = veEx.range('a', 'z', 'A', 'Z')