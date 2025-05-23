from pages.accordion import Accordion
from pages.browser_tab import BrowserTab
from pages.alerts import Alerts
from pages.demoqa import DemoQa
import  pytest
import time


def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'

# помогает циклично тестировать страницы на одном тесте
@pytest.mark.parametrize("pages", [Accordion, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'