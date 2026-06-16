class Aboutus:
    def __init__(self,page):
        self.page=page
        self.aboutus=page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')
        self.aboutus.click()
        self.page.wait_for_timeout(2000)
    #    self.page.go_back() 
        self.before=page.locator('//button[@aria-label="Previous"]')
        self.next=page.locator('//button[@aria-label="Next"]')
    
    def before_click(self):
            self.aboutus.click()
            self.before.click()
            self.page.wait_for_timeout(2000)
            self.next.click()
            self.page.wait_for_timeout(2000)








