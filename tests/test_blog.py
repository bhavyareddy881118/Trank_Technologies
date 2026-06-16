import pytest
from pages.blog import Blog

@pytest.mark.smoke
def test_blog_click(page):
    blogg=Blog(page)
    blogg.blog_click()
    blogg.page.go_back()



