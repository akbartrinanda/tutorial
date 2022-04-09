import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://elements-cover-images-0.imgix.net/1080b852-02d8-4150-bb98-12e4f015c978?auto=compress%2Cformat&fit=max&w=2740&s=78e73b5f9e96c3c9c9937a6ea6a582e5',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, cb_kwargs={'fileName': "quotes"})

    def parse(self, response, fileName):
        with open("tutorial/spiders/download/angular/preview/" + fileName + ".jpg", 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {fileName}')
