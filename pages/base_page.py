import time

import allure


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get(self, url):
        with allure.step(f'Переход на {url}'):
            return self.browser.get(url)

    @allure.step('Нажать "Назад" ')
    def back(self):
        return self.browser.back()

    @allure.step('Обновить страницу')
    def refresh(self):
        return self.browser.refresh()


    def url_startswith(self, url):
        with allure.step(f'Убедиться, что url начинается с {url}'):
            try:
                assert self.browser.current_url.startswith(url)
                return True
            except AssertionError:
                return False

    def url_contains(self, substring):
        with allure.step(f'Проверить, что url страницы содержит {substring}'):
            return substring in self.browser.current_url


    def validate_url(self, url):
        with allure.step(f'Убедиться, что url страницы соответствует {url}'):
            return self.browser.current_url == url

    def validate_title(self, title):
        with allure.step(f'Убедиться, что title страницы соответствует {title}'):
            return self.browser.title == title

    def title_contains(self, substring):
        with allure.step(f'Проверить, что title страницы содержит {substring}'):
            return substring in self.browser.title
