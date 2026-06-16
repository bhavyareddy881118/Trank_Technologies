class Services:
    def __init__(self,page):
        self.page=page

        self.webdevlopment=page.locator('(//a[@href="https://www.tranktechnologies.com/web-development-company"])[1]')
        self.cms_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/cms-website-development-company"])[2]')
        self.ecom_dev=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.website_dev=page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]')
        self.custom_web_dev=page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')

        ## UI/UX

        self.mobapp_design=page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
        self.responsive_design=page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
        self.brand_design=page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')

        ## App development

        self.app_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
        self.android_dev=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        self.androidapp_dev=page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
        self.app_development=page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
        self.hybridapp_dev=page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
        self.crossapp_dev=page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')

        ## Graphic Design

        self.graphic_design=page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
        self.logo_design=page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
        self.banner_design=page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
        self.packaging_design=page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
        self.business_design=page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')


        ## Social Media

        self.facebook=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/facebook.png"]')
        self.linkdin=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/linkedin.png"]')
        self.insta=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]')
        self.pintrest=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/pinterest.png"]')
        self.twitter=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/twitter.png"]')
        self.youtube=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/youtube.png"]')
        self.quora=page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/quora.png"]')
     
     ## Portfolio
        self.portfolio=page.locator('//a[@href="https://www.tranktechnologies.com/portfolio"]')


    def web_devlopment(self):
        self.webdevlopment.click()
        self.page.wait_for_timeout(2000)
        self.cms_dev.click()
        self.page.wait_for_timeout(2000)
        self.ecom_dev.click()
        self.page.wait_for_timeout(2000)
        self.website_dev.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()
        self.custom_web_dev.click()
        self.page.wait_for_timeout(2000)

    def ui_ux_design(self):
        self.mobapp_design.click()
        self.page.wait_for_timeout(2000)
        self.responsive_design.click()
        self.page.wait_for_timeout(2000)
        self.brand_design.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()



    def ap_development(self):
        self.app_dev.click()
        self.page.wait_for_timeout(2000)
        self.android_dev.click()
        self.page.wait_for_timeout(2000)
        self.androidapp_dev.click()
        self.page.wait_for_timeout(2000)
        self.app_development.click()
        self.page.wait_for_timeout(2000)
        self.android_dev.click()
        self.page.wait_for_timeout(2000)
        self.hybridapp_dev.click()
        self.page.wait_for_timeout(2000)
        self.crossapp_dev.click()
        self.page.wait_for_timeout(2000)


    def graphics_design(self):
        self.graphic_design.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()
        self.logo_design.click()
        self.page.wait_for_timeout(2000)
        self.banner_design.click()
        self.page.wait_for_timeout(2000)
        self.packaging_design.click()
        self.page.wait_for_timeout(2000)
        self.business_design.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()


    def social_media(self):
        for social in self.social_media:
            with self.page.expect_popup() as new_page_info:
                self.new_tab = new_page_info.value
                self.new_tab.wait_for_load_state()
                self.page.wait_for_timeout(2000)
                self.linkdin.click()
                self.new_tab = new_page_info.value
                self.new_tab.wait_for_load_state()
                self.page.wait_for_timeout(2000)
                self.insta.click()
                self.new_tab = new_page_info.value
                self.new_tab.wait_for_load_state()
                self.page.wait_for_timeout(2000)
                self.pintrest.click()
                self.page.wait_for_timeout(2000)
                self.twitter.click()
                self.new_tab = new_page_info.value
                self.new_tab.wait_for_load_state()
                self.page.wait_for_timeout(2000)
                self.youtube.click()
                self.new_tab = new_page_info.value
                self.new_tab.wait_for_load_state()
                self.page.wait_for_timeout(2000)
                self.quora.click()
                self.new_tab = new_page_info.value
                self.new_tab.wait_for_load_state()
                self.page.wait_for_timeout(2000)
                self.page.go_back()
        
                
            
    def _safe_click(self, locator, timeout=8000):
            try:
                locator.wait_for(state="visible", timeout=timeout)
                locator.click(timeout=timeout)
            except Exception:
                try:
                    locator.scroll_into_view_if_needed()
                    locator.click(timeout=timeout)
                except Exception:
                    try:
                        locator.click(timeout=timeout, force=True)
                    except Exception:
                        self.page.wait_for_timeout(500)

    def portfolio_page(self):
        self._safe_click(self.portfolio)
        #self.page.wait_for_timeout(2000)
        self.page.wait_for_load_state("load")
        self.page.go_back()











