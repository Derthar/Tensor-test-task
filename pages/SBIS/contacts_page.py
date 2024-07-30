import time
from pages.base_page import BasePage
from pages.SBIS.locators import ContactsPageLocators
import allure
from pages.SBIS.header import Header
from pages.SBIS.footer import Footer
from pages.web_element import WebElement, WebElements


class SbisContactsPage(BasePage):
    @allure.step('Переход на страницу контактов портала "sbis.ru"')
    def __init__(self, browser):
        self.browser = browser
        super().__init__(browser=self.browser)
        self.locators = ContactsPageLocators
        self.header = Header(browser=self.browser)
        self.footer = Footer(browser=self.browser)
        self.tensor_logo = WebElement(browser=self.browser, locator=self.locators.LOGO,
                                      description='Баннер "Тензор" в блоке контактов')
        self.region = WebElement(browser=self.browser, locator=self.locators.REGION, description='Название региона')
        self.region_modal = WebElement(browser=self.browser, locator=self.locators.REGION_MODAL,
                                       description='Окно выбора региона')
        self.region_modal_title = WebElement(browser=self.browser, locator=self.locators.REGION_MODAL_TITLE,
                                             description='Заголовок окна выбора региона')
        self.regions = {
            'Камчатский край': WebElement(browser=browser, locator=self.locators.REGIONS['Камчатский край'],
                                          description='Камчатский край'),
            'Свердловская область': WebElement(browser=browser, locator=self.locators.REGIONS['Свердловская область'],
                                               description='вердловская область'),
            'Ярославская область': WebElement(browser=browser, locator=self.locators.REGIONS['Ярославская область'],
                                              description='Ярославская область')
                        }
        self.partners = WebElements(browser=self.browser, locator=self.locators.PARTNERS,
                                    description='Cписок партнеров')
        time.sleep(1)
