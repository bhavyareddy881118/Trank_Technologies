import pytest
from pages.contactus import Contactus

@pytest.mark.smoke
def test_consultation_form(page):
    contactuss=Contactus(page)
    contactuss.consultation_form()
    contactuss.page.go_back()
