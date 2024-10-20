import scrapy
from phones.items import PhoneSpecItem
import re
from scrapy.exceptions import CloseSpider

class PhonespiderSpider(scrapy.Spider):
    name = 'phonespider'
    allowed_domains = ['www.gsmarena.com']
    start_urls = ['https://www.gsmarena.com/']

    def parse(self, response):
        # Extract all li elements within the specified div and ul
        li_elements = response.xpath("//div[@class='brandmenu-v2 light l-box clearfix']/ul/li")
        for li in li_elements:
            # Extract the href attribute of the a tag within each li
            href = li.xpath("./a/@href").get()
            if href:
                brand = re.search(r'(\w+)-phones', href).group(1)
                yield response.follow(href, callback=self.parse_phone_page, meta={'brand': brand})

    def parse_phone_page(self, response):
        self.log(f'\n\nVisited page: {response.url}\n\n')
        # Extract li elements inside ul element within the div with class 'makers'
        phone_brand = response.meta['brand']
        phone_elements = response.xpath("//div[@class='makers']/ul/li")
        for phone in phone_elements:
            # Extract the href attribute of the a tag within each li
            phone_href = phone.xpath("./a/@href").get()
            if phone_href:
                # Use response.follow to navigate to the new page
                yield response.follow(phone_href, callback=self.parse_phone, meta={'brand': phone_brand})
        next_page = response.xpath("//a[@class='prevnextbutton' and @title='Next page']/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_phone_page, meta={'brand': phone_brand})
        else:
            self.log('No next page found.')
        
    
    def parse_phone(self, response):
        self.log(f'\n\nVisited page: {response.url}\n\n')
        # Extract the phone model name
        phone_brand = response.meta['brand']
        phone_model = response.xpath("//h1[@class='specs-phone-name-title']/text()").get()
        # Extract the div with id 'specs-list'
        specs_div = response.xpath("//div[@id='specs-list']")
        
        # Initialize a dictionary to hold the aggregated data
        phone_data = {
            'phone_brand': phone_brand,
            'phone_model': phone_model,
            'specs': {}
        }
        
        # Iterate over each table within the div
        for table in specs_div.xpath(".//table"):
            category = table.xpath(".//th[1]/text()").get()
            for row in table.xpath(".//tr"):
                key = row.xpath(".//td[@class='ttl']/a/text()").get()
                value = row.xpath(".//td[@class='nfo']/text()").get()
                if key and value:
                    self.log(f"{phone_model} - {category} - {key}: {value}")
                    if category not in phone_data['specs']:
                        phone_data['specs'][category] = {}
                    phone_data['specs'][category][key] = value
                    
        if response.xpath("//td[@class='nfo' and @data-spec='price']/a/text()").get() is not None: 
            # Extract the price of the phone
            price = response.xpath("//td[@class='nfo' and @data-spec='price']/a/text()").get()
        else:
            price = response.xpath("//td[@class='nfo' and @data-spec='price']/text()").get()
            
        # Yield the aggregated item
        item = PhoneSpecItem(
            phone_brand=phone_data['phone_brand'],
            phone_model=phone_data['phone_model'],
            price=price,
            specs=phone_data['specs']
        )
        if response.xpath("//td[@class='nfo' and @data-spec='price']/a/@href").get() is not None:
            href = response.xpath("//td[@class='nfo' and @data-spec='price']/a/@href").get()
            yield response.follow(href, callback=self.parse_price_page, meta={'item': item})
        else:
            # Yield the item if there is no price page to follow
            yield item
        
    
    def parse_price_page(self, response):
        # Retrieve the item from the meta data
        item = response.meta['item']
        
        # Initialize a dictionary to hold the pricing data
        pricing_data = {}

        # Iterate over each table within the pricing-container div
        for table in response.xpath("//div[@class='pricing-container']/table"):
            region = table.xpath(".//caption/text()").get()
            pricing_data[region] = {}

            # Get the headers for the different storage options
            headers = table.xpath(".//thead/tr/th/text()").getall()[1:]  # Skip the first empty header

            # Iterate over each row in the tbody
            for row in table.xpath(".//tbody/tr"):
                store = row.xpath(".//th/img/@alt").get()
                prices = row.xpath(".//td/a/text()").getall()

                # Map the prices to the corresponding storage options
                pricing_data[region][store] = dict(zip(headers, prices))

        # Add the pricing data to the item
        item['pricing'] = pricing_data

        # Yield the final item
        yield item