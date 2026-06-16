import pytest
from pages.technologies import Technologies

@pytest.mark.smoke
def test_ecommerce_Dev(page):
    ecom=Technologies(page)
    ecom.ecommerce_development()
    ecom.page.go_back()

@pytest.mark.smoke
def test_mobile_Dev(page):
    mbl=Technologies(page)
    mbl.mobileapp_development()
    mbl.page.go_back()

@pytest.mark.smoke
def artin(page):
    art=Technologies(page)
    art.ai()
