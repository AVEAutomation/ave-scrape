import scrapy, os

class AveSpider(scrapy.Spider):
    name = "ave"
    allowed_domains = ["vendorexpress.amazon.com"]
    start_urls = ["https://vendorexpress.amazon.com/orders"]     

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': os.getenv('AVE_ACCOUNT'), 'password': os.getenv('AVE_ACCOUNT_PW')},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        

