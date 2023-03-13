import scrapy
from scrapy_splash import SplashRequest


class CoinSpider(scrapy.Spider):
    name = "coin"
    allowed_domains = ["www.coinmarketcap.com"]

    script = '''
        function main(splash, args)
            splash:on_request(function(request)
                request:set_headers('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
            end)
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            splash:set_viewport_full()
            return splash:html()

        end
    '''

    def start_requests(self):
        yield SplashRequest(url="https://www.coinmarketcap.com/", callback=self.parse, endpoint="execute",
                            args={'lua_source': self.script})

    def parse(self, response):
        for currency in response.xpath('//tbody/tr'):
            yield {
                'currency name': currency.xpath(".//td/div/a/div/div/p[contains(@color,'text')]/text()").get(),
                'price': currency.xpath(".//td/div/a/span/text()").get()
            }
