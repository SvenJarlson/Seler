from pages.basepage import BasePage
from pages.locators import PrivacySettingsLocators
from time import sleep


class PrivacySettingsPage(BasePage):

    def select_privacy_settings_page(self):
        sleep(1)
        self.driver.get("https://sale.aliexpress.com/cookie-setting.htm?spm=a2g0o.home.1000001.6.6387405f6ap0d6")

    def locate_and_grab_text(self):
        # locate the text section and grab it
        sleep(1)
        txt1 = self.driver.find_elements(*PrivacySettingsLocators.TEXT_SECTIONS)[0].get_attribute('textContent')
        txt2 = self.driver.find_elements(*PrivacySettingsLocators.TEXT_SECTIONS)[1].get_attribute('textContent')
        txt3 = self.driver.find_elements(*PrivacySettingsLocators.TEXT_SECTIONS)[2].get_attribute('textContent')
        txt4 = self.driver.find_elements(*PrivacySettingsLocators.TEXT_SECTIONS)[3].get_attribute('textContent')
        txt5 = self.driver.find_elements(*PrivacySettingsLocators.TEXT_SECTIONS)[4].get_attribute('textContent')
        txt6 = self.driver.find_elements(*PrivacySettingsLocators.TEXT_SECTIONS)[5].get_attribute('textContent')
        txt7 = self.driver.find_elements(*PrivacySettingsLocators.TEXT_SECTIONS)[6].get_attribute('textContent')
        textlist = [txt1, txt2, txt3, txt4, txt5, txt6, txt7]
        return textlist


