import pytest
from pages.verticals import Vertical

@pytest.mark.smoke
def test_verticals(page):
    ver=Vertical(page)
    ver.mousehoververtical()
@pytest.mark.smoke
def test_trading(page):
    trade=Vertical(page)
    trade.tradinglist()
    trade.page.go_back()

@pytest.mark.smoke
def test_retail(page):
    retail=Vertical(page)
    retail.retaillist()

@pytest.mark.smoke
def test_health(page):
    health=Vertical(page)
    health.healthlist()

@pytest.mark.smoke
def test_fintech(page):
    fintech=Vertical(page)
    fintech.fintechlist()

@pytest.mark.smoke
def test_customapp(page):
    customapp=Vertical(page)
    customapp.customapplist()


 

