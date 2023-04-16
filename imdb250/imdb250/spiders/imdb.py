import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.transvias.com.br/transportadoras/estados/sao-paulo"]

    def parse(self, response):
        trp = response.css('.m-boxCompany__A')
        pass

        print(trp)