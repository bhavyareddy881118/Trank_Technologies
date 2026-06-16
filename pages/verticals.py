class Vertical:
    def __init__(self,page):
        self.page=page
        self.vertical=page.locator('(//a[text()="Verticals"])[1]')
        self.trade=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/trade-mob.png"]')
        self.retail=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.health=page.locator('(//a[@href="https://www.tranktechnologies.com/healthcare-mobile-app-development-company"])[1]')
        self.fintech=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/fintech-mob.png"]')
        self.customap=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/submenu-icons/custom-mob.png"]')

        
        #### Trading options

        self.t1=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.t2=page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.t3=page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.t4=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.t5=page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.t6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.t7=page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.trading_list=[self.t1,self.t2,self.t3,self.t4,self.t5,self.t6,self.t7]


        # Retail and E-commerce
        self.r1=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.r2=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.retail_list=[self.r1,self.r2]

        # Health care
        self.h1=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.h2=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.health_list=[self.h1,self.h2]

        # Fintech 
        self.f1=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.f2=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.fintech_list=[self.f1,self.f2]

        # Custom App
        self.c1=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.c2=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.c3=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.c4=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.c5=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
        self.c6=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.c7=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.c8=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.c9=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.customapp_list=[self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9]

    def mousehoververtical(self):
        self._safe_hover(self.vertical)


    def mousehovertrading(self):   
        self._safe_hover(self.trade)
       

    def mousehoverretail(self):
        self._safe_hover(self.retail)
      

    def mousehoverhealth(self):
        self._safe_hover(self.health)
       

    def mousehoverfintech(self):
        self._safe_hover(self.fintech)
       

    def mousehovercustomapp(self):
        self._safe_hover(self.customap)

    def _safe_hover(self, locator, timeout=8000):
        try:
            locator.wait_for(state="visible", timeout=timeout)
            locator.scroll_into_view_if_needed()
            locator.hover(timeout=timeout)
            self.page.wait_for_timeout(200)
        except Exception:
            try:
                locator.scroll_into_view_if_needed()
                locator.hover(timeout=timeout)
                self.page.wait_for_timeout(200)
            except Exception:
                return

    def _safe_click(self, locator, timeout=8000):
        if self.page.is_closed():
            return
        try:
            locator.wait_for(state="visible", timeout=timeout)
            locator.scroll_into_view_if_needed()
            locator.click(timeout=timeout)
        except Exception:
            if self.page.is_closed():
                return
            try:
                locator.click(timeout=timeout, force=True)
            except Exception:
                if not self.page.is_closed():
                    self.page.wait_for_timeout(100)
                return


    def tradinglist(self):
        for i in self.trading_list:
            self.mousehoververtical()
            self.mousehovertrading()
            self._safe_click(i)
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(2000)

    def retaillist(self):
        for i in self.retail_list:
            self.mousehoververtical()
            self.mousehoverretail()
            self._safe_click(i)
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(1000)

    def healthlist(self):
        for i in self.health_list:
            self.mousehoververtical()
            self.mousehoverhealth()
            self._safe_click(i)
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(1000)

    def fintechlist(self):
        for i in self.fintech_list:
            self.mousehoververtical()
            self.mousehoverfintech()
            self._safe_click(i)
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(1000)

    def customapplist(self):
        for i in self.customapp_list:
            self.mousehoververtical()
            self.mousehovercustomapp()
            self.page.wait_for_timeout(200)
            self._safe_click(i)
            self.page.wait_for_load_state("load")
            self.page.go_back()
            self.page.wait_for_load_state("load")
            self.page.wait_for_timeout(1000)






