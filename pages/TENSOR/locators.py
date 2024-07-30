from selenium.webdriver.common.by import By


class MainPageLocators:
    POWER_IN_PEOPLE_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg')
    POWER_IN_PEOPLE_TITLE = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg p.tensor_ru-Index__card-title')
    POWER_IN_PEOPLE_DETAILED = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg a')


class AboutPageLocators:
    WORKING_BLOCK = (By.CSS_SELECTOR, '.tensor_ru-About__block3')
    WORKING_IMAGES = (By.CSS_SELECTOR, '.tensor_ru-About__block3 img')
