from allure_commons.types import AttachmentType
from urls import *
import pytest
import allure
from pages.SBIS.main_page import SbisMainPage
from pages.SBIS.contacts_page import SbisContactsPage
from pages.TENSOR.main_page import TensorMainPage
from pages.TENSOR.about_page import TensorAboutPage
from pages.SBIS.download_page import SbisDownloadPage
from regions import REGIONS
import os
import pathlib
import requests


# TODO: Вписать дополнительные браузеры в значение "params", если необходимо. Также в данном случае необходимо указать
#  пути к драйверам в файле "conftest", а также убедиться что браузеры установлены и обновлены на компьютере
@pytest.fixture(params=['chrome'], scope="function")  # firefox, tandex, opera, edge
def browser(request):
    return request.getfixturevalue(request.param)


@pytest.mark.test_task
class Test:

    @allure.feature('Сценарий №1')
    def test_scenario_1(self, browser):
        try:
            browser.get(URL1)
            sbis_main_page = SbisMainPage(browser=browser)
            assert sbis_main_page.validate_url(url=URL1)
            sbis_main_page.header.contacts.click()
            contacts_page = SbisContactsPage(browser=browser)
            assert contacts_page.url_startswith(url=URL2)
            contacts_page.tensor_logo.click()
            windows = browser.window_handles
            assert len(windows) == 2
            browser.switch_to.window(windows[1])
            tensor_main_page = TensorMainPage(browser=browser)
            tensor_main_page.power_in_people_block.is_visible()
            tensor_main_page.power_in_people_block.scroll_to_element()
            assert tensor_main_page.power_in_people_title.text() == 'Сила в людях'
            tensor_main_page.power_in_people_detailed.click()
            tensor_about_page = TensorAboutPage(browser=browser)
            assert tensor_about_page.validate_url(url=URL5)
            tensor_about_page.working_block.is_visible()
            tensor_about_page.working_block.scroll_to_element()
            images = tensor_about_page.working_images.count()
            assert images == 4
            heights = tensor_about_page.working_images.attribute('height')
            assert len(set(heights)) == 1
            widths = tensor_about_page.working_images.attribute('width')
            assert len(set(widths)) == 1
        except Exception:
            allure.attach(name='error_screen', body=browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            pytest.fail()

    # TODO: в данном тесте необходимо корректно задать стартовый регион в строке 69 через индекс.
    #  Индекс равен номеру региона
    @allure.feature('Сценарий №2')
    def test_scenario_2(self, browser):
        try:
            browser.get(URL1)
            sbis_main_page = SbisMainPage(browser=browser)
            assert sbis_main_page.validate_url(url=URL1)
            sbis_main_page.header.contacts.click()
            contacts_page = SbisContactsPage(browser=browser)
            assert contacts_page.url_startswith(url=URL2)
            assert contacts_page.region.text() == REGIONS[66]['name']
            partners = contacts_page.partners.text()
            contacts_page.region.click()
            assert contacts_page.region_modal.is_visible()
            assert contacts_page.region_modal_title.text() == 'Выберите свой регион'
            contacts_page.regions[REGIONS[41]['name']].click()
            new_contacts_page = SbisContactsPage(browser=browser)
            assert new_contacts_page.title_contains(REGIONS[41]['title_name'])
            assert new_contacts_page.url_contains(REGIONS[41]['url_name'])
            assert new_contacts_page.region.text() == REGIONS[41]['name']
            assert partners != new_contacts_page.partners.text()
        except Exception:
            allure.attach(name='error_screen', body=browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            pytest.fail()

    @allure.feature('Сценарий №3')
    def test_scenario_3(self, browser):
        try:
            browser.get(URL1)
            sbis_main_page = SbisMainPage(browser=browser)
            assert sbis_main_page.validate_url(url=URL1)
            sbis_main_page.footer.download_local_versions.scroll_to_element()
            sbis_main_page.footer.download_local_versions.click()
            download_page = SbisDownloadPage(browser=browser)
            file_expected_size = float(download_page.plugin_download.text().split(' ')[2])
            file_href = download_page.plugin_download.attribute('href')
            content = requests.get(file_href).content
            basepath = pathlib.Path(__file__).resolve().parents[1]
            path = os.path.join(basepath, '1.exe')
            with open(path, 'wb') as file:
                file.write(content)
            file_actual_size = (float('{:.2f}'.format(os.path.getsize(path) / 1024 / 1024)))
            assert file_expected_size == file_actual_size
        except Exception:
            allure.attach(name='error_screen', body=browser.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            pytest.fail()
        finally:
            if '1.exe' in os.listdir(pathlib.Path(__file__).resolve().parents[1]):
                os.remove(os.path.join(pathlib.Path(__file__).resolve().parents[1], '1.exe'))
