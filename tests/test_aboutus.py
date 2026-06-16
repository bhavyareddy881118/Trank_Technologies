import pytest
from pages.aboutus import Aboutus

@pytest.mark.smoke
def test_previous_click(page):
    previous=Aboutus(page)
    previous.before_click()
    previous.page.go_back()



