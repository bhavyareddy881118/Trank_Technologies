import pytest
from pages.services import Services


# @pytest.mark.smoke
# def test_webdevelopment(page):
#     webdevelopment=Services(page)
#     webdevelopment.web_devlopment()
#     webdevelopment.page.go_back()

# @pytest.mark.smoke
# def test_uiuxdesign(page):
#     uiuxdesign=Services(page)
#     uiuxdesign.ui_ux_design()
#     uiuxdesign.page.go_back()

# @pytest.mark.smoke
# def test_appdevelopment(page):
#     appdevelopment=Services(page)
#     appdevelopment.ap_development()
#     appdevelopment.page.go_back()


# @pytest.mark.smoke
# def test_graphicdesign(page):
#     graphicdesign=Services(page)
#     graphicdesign.graphics_design()
#     graphicdesign.page.go_back()

# @pytest.mark.smoke
# def test_socialmedia(page):
#     socialmedia=Services(page)
#     socialmedia.social_media()
#     socialmedia.page.go_back()


@pytest.mark.smoke
def test_portfolio_click(page):
    portfolio_click=Services(page)
    portfolio_click.portfolio_page()
    portfolio_click.page.go_back()

