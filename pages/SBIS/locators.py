from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class HeaderLocators:
    HEADER = (By.CSS_SELECTOR, '.sbisru-Header__container')
    CONTACTS = (By.CSS_SELECTOR, '.sbisru-Header__menu-item-1 a')

class FooterLocators:
    DOWNLOAD_LOCAL = (By.CSS_SELECTOR, '.sbisru-Footer__container div:nth-child(3) ul li:nth-child(8)')

class ContactsPageLocators:
    LOGO = (By.CSS_SELECTOR, '#contacts_clients .sbisru-Contacts__logo-tensor img')
    REGION = (By.CSS_SELECTOR, '.sbisru-Contacts__relative .sbis_ru-Region-Chooser__text')
    REGION_MODAL = (By.CSS_SELECTOR, '.sbis_ru-Region-Panel')
    REGION_MODAL_TITLE = (By.CSS_SELECTOR, '.sbis_ru-Region-Panel h5')
    REGIONS = {
        'Камчатский край': (By.CSS_SELECTOR, '.sbis_ru-Region-Panel__list-l li:nth-child(43) span span'),
        'Свердловская область': (By.CSS_SELECTOR, '.sbis_ru-Region-Panel__list-l li:nth-child(69) span span'),
        'Ярославская область': (By.CSS_SELECTOR, '.sbis_ru-Region-Panel__list-l li:nth-child(69) span span')
    }
    PARTNERS = (By.CSS_SELECTOR, '.sbisru-Contacts-List__col div.sbisru-Contacts-List__item div.sbisru-Contacts-List__name')

class DownloadPageLocators:
    DOWNLOAD_PLUGIN_EXE = (By.CSS_SELECTOR, '.ws-SwitchableArea__item.ws-has-focus div:nth-child(4) .sbis_ru-DownloadNew-flex__child div a')
