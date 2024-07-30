import pytest
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='function')
def chrome():
    options = ChromeOptions()
    options.add_argument('--headless')
    options.page_load_strategy = 'eager'
    chrome = (webdriver.Chrome(options=options))
    chrome.set_window_size(1920, 1080)
    chrome.implicitly_wait(15)
    yield chrome
    chrome.quit()


@pytest.fixture(scope='function')
def firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.page_load_strategy = 'eager'
    firefox = webdriver.Firefox(options=options)
    firefox.set_window_size(1920, 1080)
    firefox.implicitly_wait(10)
    yield firefox
    firefox.quit()


@pytest.fixture(scope='function')
def opera():
    service = ChromeService('path to webdriver')  # TODO: Необходимо указать путь до корректного вебдрайвера
    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_experimental_option('w3c', True)
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    options.page_load_strategy = 'eager'
    opera = webdriver.Chrome(service=service, options=options)
    opera.set_window_size(1920, 1080)
    opera.implicitly_wait(10)
    yield opera
    opera.quit()


@pytest.fixture(scope='function')
def edge():
    options = EdgeOptions()
    options.add_argument('--headless')
    options.page_load_strategy = 'eager'
    edge = webdriver.Edge(options=options)
    edge.set_window_size(1920, 1080)
    edge.implicitly_wait(10)
    yield edge
    edge.quit()


@pytest.fixture(scope='function')
def yandex():
    service = ChromeService('path to webdriver')  # TODO: Необходимо указать путь до корректного вебдрайвера
    options = ChromeOptions()
    options.add_argument('--headless')
    options.page_load_strategy = 'eager'
    yandex = webdriver.Chrome(service=service, options=options)
    yandex.set_window_size(1920, 1080)
    yandex.implicitly_wait(10)
    yield yandex
    yandex.quit()
