class Technologies:
    def __init__(self,page):
        self.page=page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')
        self.ecomm=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ecomm-mob.png"]')
        self.mobileapp=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/mobileapp-mob.png"]')
        self.ai=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/ai-mob.png"]')
       # Ecommerce
        self.e1=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.e2=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.e3=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.e4=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.e5=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.e6=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.e7=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.e8=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.e9=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.e10=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.e11=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.e12=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.ecomm_list=[self.e1,self.e2,self.e3,self.e4,self.e5,self.e6,self.e7,self.e8,self.e9,self.e10,self.e11,self.e12]

        # Mobile app development
        self.m1=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.m2=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.m3=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.m4=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.m5=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.m6=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.m7=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.m8=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobileapp_list1=[self.m1,self.m2,self.m3,self.m4,self.m5,self.m6,self.m7,self.m8]        

        #Artificial Intelligence


    def mousehover_technologies(self):
        self.technologies.hover()
        
    def mousehover_ecommerce(self):
        self.ecomm.hover()
    
    def mousehover_mobileapp(self):
        self.mobileapp.hover()
    
    def mousehover_ai(self):
        self.ai.hover()
    
    def ecommerce_development(self):
        for i in self.ecomm_list:
            self.mousehover_technologies()
            self.mousehover_ecommerce()
            i.click()
    #        self.page.go_back()
            self.page.wait_for_timeout(2000)
    def mobileapp_development(self):
        for i in self.mobileapp_list1:
            self.mousehover_technologies()
            self.mousehover_mobileapp()
            i.click()
        #    self.page.go_back()
            self.page.wait_for_timeout(2000)
    def ai(self):
        self.mousehover_technologies()
        self.mousehover_ai()
        self.page.go_back()
        self.page.wait_for_timeout(5000)
