import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


TIMEOUT = 15

class WebElement:
    def __init__(self, browser, locator=None, description=None, timeout=TIMEOUT):
        self._browser = browser
        self._timeout = timeout
        self._locator = locator
        self._description = description

    def _find(self, timeout):
        element = None
        try:
            element = WebDriverWait(self._browser, timeout=timeout).until(
                ec.presence_of_element_located(self._locator)
            )
        except TimeoutException:
            print('Element not found on the page!', 'red')
        return element

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        with allure.step(f'Кликнуть на элемент "{self._description}"'):

            element = self._wait_to_be_clickable()

            if element:
                time.sleep(2)
                action = ActionChains(self._browser)
                action.move_to_element_with_offset(element, x_offset, y_offset). \
                    pause(hold_seconds).click(on_element=element).perform()
                time.sleep(2)
            else:
                msg = 'Element with locator {0} not found'
                raise AttributeError(msg.format(self._locator))

    def text(self):
        with allure.step(f'Сравнить значение атрибута "text" элемента {self._description}'):
            time.sleep(1)
            element = self._find(timeout=self._timeout)
            time.sleep(1)
            text = ''
            try:
                text = str(element.text)
            except Exception as e:
                print('Error: {0}'.format(e))

            return text

    def value(self):
        with allure.step(f'Сравнить значение атрибута "value" элемента {self._description}'):
            _value = self._browser.get_attribute('value')
            if _value is not None:
                return _value
            return False

    def move_to(self):
        with allure.step(f'Навести курсор на элемент {self._description}'):
            _element = self._find(timeout=self._timeout)
            return ActionChains(self._browser).move_to_element(_element).perform()

    def send_keys(self, keys, wait=2):
        with allure.step(f'Ввести символы в элемент {self._description}'):
            keys = keys.replace('\n', '\ue007')

            element = self._find(timeout=self._timeout)

            if element:
                element.click()
                element.clear()
                element.send_keys(keys)
                time.sleep(wait)
            else:
                msg = 'Element with locator {0} not found'
                raise AttributeError(msg.format(self._locator))

    def _wait_to_be_clickable(self, timeout=TIMEOUT):
        _element = None
        try:
            _element = WebDriverWait(self._browser, timeout).until(
                ec.element_to_be_clickable(self._locator)
            )
        except TimeoutException:
            print('Element not clickable!')
        return _element

    def is_clickable(self):
        with allure.step(f'Убедиться что элемент {self._description} кликабелен'):
            element = self._wait_to_be_clickable(timeout=1)
            return element is not None

    def is_presented(self):
        with allure.step(f'Убедиться что элемент {self._description} присутствует на странице'):
            element = self._find(timeout=1)
            return element is not None

    def is_visible(self):
        with allure.step(f'Убедиться что элемент {self._description} видимый'):
            element = self._find(timeout=1)

            if element:
                return element.is_displayed()

            return False

    def wait_until_not_visible(self, timeout=TIMEOUT):

        with allure.step(f'Убедиться что элемент {self._description} не видимый'):

            try:
                element = WebDriverWait(self._browser, timeout=timeout).until_not(
                    ec.visibility_of_element_located(self._locator)
                )
            except Exception:
                raise
        return element

    def scroll_to_element(self):
        with allure.step(f'Пролистать страницу до элемента {self._description}'):
            element = self._find(timeout=self._timeout)
            self._browser.execute_script("arguments[0].scrollIntoView();", element)

    def delete(self):
        with allure.step(f'Удалить элемент {self._description}'):
            element = self._find(timeout=self._timeout)
            self._browser.execute_script("arguments[0].remove();", element)

    def attribute(self, attribute):
        with allure.step(f'Получить значение атрибуте {attribute} элемента{self._description}'):
            _element = self._find(timeout=self._timeout)
            if _element:
                _result = _element.get_attribute(attribute)
            if _result is not None:
                return _result
            return False


class WebElements(WebElement):
    def __init__(self, browser, locator, description, timeout=TIMEOUT):
        super().__init__(browser=browser)
        self._browser = browser
        self._locator = locator
        self._description = description
        self._timeout = timeout

    def _find(self, timeout):
        return self._browser.find_elements(*self._locator)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        print('Данный метод недоступен для списочных классов')
        return False

    def count(self):
        with allure.step(f'Посчитать количество элементов {self._description}'):
            _elements = self._find(timeout=self._timeout)
            return len(_elements)

    def move_to(self):
        print('Данный метод недоступен для списочных классов')
        return False

    def text(self):
        with allure.step(f'Сравнить значение "text" элементов {self._description}'):
            _elements = self._find(timeout=self._timeout)
            _result = []
            for elem in _elements:
                _result.append(elem.text)
            if len(_result) != 0:
                return _result
            return False

    def value(self):
        with allure.step(f'Сравнить значение "value" элементов {self._description}'):
            _elements = self._find(timeout=self._timeout)
            _result = []
            for elem in _elements:
                _result.append(elem.get_attribute('value'))
            if len(_result) != 0:
                return _result
            return False

    def attribute(self, attribute):
        with allure.step(f'Сравнить значение "{attribute}" элементов {self._description}'):
            _elements = self._find(timeout=self._timeout)
            _result = []
            for elem in _elements:
                _result.append(elem.get_attribute(attribute))
            if len(_result) != 0:
                return _result
            return False
