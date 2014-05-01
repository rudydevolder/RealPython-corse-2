# wikicrawl.py crawlspider


from scrapy.spider import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from wikipedia.items import WikipediaItem
from urlparse import urljoin

class MySpider(BaseSpider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
       "http://en.wikipedia.org/wiki/Category:2013_films"
       ]

    rules = (Rule (SgmlLinkExtractor(allow=("index\d00\.html", ),restrict_xpaths=('//p[@class="nextpage"]',))
    , callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//tr[@style="vertical-align: top;"]//li')
        items = []
        for title in titles:
            item = WikipediaItem()
            url = title.select("a/@href").extract()
            item["title"] = title.select("a/text()").extract()
            item["url"] = urljoin("http://en.wikipedia.org", url[0])
            items.append(item)
        return(items)
