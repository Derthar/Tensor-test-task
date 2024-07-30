from pages.base_page import BasePage
from pages.TENSOR.locators import AboutPageLocators
import allure
from pages.web_element import WebElement, WebElements
import time


class TensorAboutPage(BasePage):
    @allure.step('Переход на cтраницу "О компании" портала "tensor.ru"')
    def __init__(self, browser):
        self.browser = browser
        super().__init__(browser=self.browser)
        self.locators = AboutPageLocators
        self.working_block = WebElement(browser=self.browser, locator=self.locators.WORKING_BLOCK,
                                        description='Блок "Работаем"')
        self.working_images = WebElements(browser=self.browser, locator=self.locators.WORKING_IMAGES,
                                          description='Изображения блока "Работаем"')
        time.sleep(1)
