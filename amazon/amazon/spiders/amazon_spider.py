import scrapy
from amazon.items import AmazonItem
from scrapy.http import Request


class AmazonSpider(scrapy.spiders.Spider):
    name = "amazon"
    download_delay = 6
    allowed_domains = ["amazon.cn"]
    start_urls = [
            "https://www.amazon.cn/s/ref=nb_sb_noss_2?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=Apple+MacBook+Air&rh=i%3Aaps%2Ck%3AApple+MacBook+Air"
    ]

    def parse(self, response):
        goods = response.xpath("//li[re:match(@class, 's-result-item')]")

        print("goods--------", goods)

        for good in goods:
            item = AmazonItem()

            good_name = good.xpath("div/div/div/a/h2/text()").extract()
            good_url = good.xpath("div/div/div/div/a/@href").extract()
            good_price = good.xpath("div/div/div/a[@class='a-link-normal a-text-normal']/span/text()").extract()
            good_star = good.xpath("div/div/span/span/a/i/span/text()").extract()

            good_commentsnum = good.xpath(
                "div/div/a[@class='a-size-small a-link-normal a-text-normal']/text()").extract()
            good_commentsurl = good.xpath(
                "div/div/a[@class='a-size-small a-link-normal a-text-normal']/@href").extract()

            for n in good_name:
                print(n)

            item["good_name"] = [n for n in good_name]
            item["good_url"] = [n for n in good_url]
            item["good_price"] = [n for n in good_price]
            item["good_star"] = [n for n in good_star]
            item["good_commentsnum"] = [n for n in good_commentsnum]
            item["good_commentsurl"] = [n for n in good_commentsurl]

            yield item

        for url in response.xpath("//a[@id='pagnNextLink']/@href").extract():
            yield Request("http://www.amazon.cn" + url, callback=self.parse)