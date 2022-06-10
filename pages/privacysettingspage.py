from pages.basepage import BasePage
from pages.locators import PrivacySettingsLocators
from time import sleep
from nltk import word_tokenize
from nltk.corpus import stopwords

class PrivacySettingsPage(BasePage):

    def select_privacy_settings_page(self):
        self.driver.get("https://sale.aliexpress.com/cookie-setting.htm?spm=a2g0o.home.1000001.6.6387405f6ap0d6")

    def locate_and_grab_text(self):
        # locate the text section and grab it
        textlist = self.driver.find_elements(*PrivacySettingsLocators.TEXT_SECTIONS)[0].get_attribute('textContent')

        # grab it

        #textlist[1].text()
        #textlist[2].text()
        #textlist[3].text()
        #textlist[4].text()
        #textlist[5].text()
        #textlist[6].text()


    def detect_lang(text):
        # detect language

        lang_ratios = {}

        tokens = word_tokenize(text)
        words = [word.lower() for word in tokens]

        for language in stopwords.fileids():
            stopwords_set = set(stopwords.words(language))
            words_set = set(words)
            common_elements = words_set.intersection(stopwords_set)

            lang_ratios[language] = len(common_elements)
        return max(lang_ratios, key=lang_ratios.get)