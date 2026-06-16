class Blog:
    def __init__(self,page):
        self.page=page
        self.blog=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.b_app_dev=page.locator('//a[@href="/blog/category/app-development/"]')
        self.b_web_dev=page.locator('//a[@href="/blog/category/web-development/"]')
        self.b_sw_dev=page.locator('//a[@href="/blog/category/software-development/"]')
        self.b_digital_marketing=page.locator('//a[@href="/blog/category/digital-marketing/"]')
        self.b_email_marketing=page.locator('//a[@href="/blog/category/email-marketing/"]')
        self.b_ai=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.b_uiux=page.locator('//a[@href="/blog/category/ui-ux-design/"]')
        self.b_search=page.locator('(//i[@class="fa fa-search"])[2]')

        self.blog_list=[self.b_app_dev,self.b_web_dev,self.b_sw_dev,self.b_digital_marketing,self.b_email_marketing,self.b_ai,self.b_uiux,self.b_search]

    def blog_click(self):
        self.blog.click()
        self.page.wait_for_timeout(2000)
        for i in self.blog_list:
            i.click()
            self.page.wait_for_timeout(3000)

        

