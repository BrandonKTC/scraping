import scrapy
from scrapy.selector import Selector
from shutil import which
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CoinSpiderSelenium(scrapy.Spider):
    name = "coin_selenium"
    allowed_domains = ["www.coinmarketcap.com"]
    start_urls = [
        "https://www.coinmarketcap.com/"
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.get("https://www.coinmarketcap.com/")
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath('//tbody/tr'):
            yield {
                'currency name': currency.xpath(".//td/div/a/div/div/p[contains(@color,'text')]/text()").get(),
                'price': currency.xpath(".//td/div/a/span/text()").get()
            }
