import scrapy


class UpdateSpider(scrapy.Spider):
    name = "update"

    def start_requests(self):
        urls = [
            'https://docs.microsoft.com/en-us/windows-insider/flight-hub/#windows-10-may-2021-update-21h1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # css select와 xpath로 가져오는 방법이 있고 css로 진행해보겠다.
        update_bots = response.css('.table table-sm > tbody > tr')
        for update_bot in update_bots:
            title = update_bot.css('.table table-sm > tbody > tr > td > a > text').get()
            print('title: ', title)