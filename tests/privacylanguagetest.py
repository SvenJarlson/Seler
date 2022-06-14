from tests.basetest import BaseTest


class PrivacyTest(BaseTest):
    """
    Privacy Language Test
    """

    def test_if_language_is_Polish(self, ch=None):
        """
        TC 003 : Privacy policy content is in Polish
        """
        home_page = self.homepage.get_rid_of_popups()
        privacy_page = self.privacysettingspage
        # enter the privacy settings tab
        privacy_page.select_privacy_settings_page()
        # grab section text
        textlist = privacy_page.locate_and_grab_text()
        # check language
        langlist = []
        for i in range(len(textlist)):
            textlist[i] = list(textlist[i])

        for i in range(len(textlist)):
            for ch in textlist[i]:
                if ch in ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']:
                    langlist.append("polish")
                    break
                else:
                    pass
        # testing whether each element about privacy policy is indeed in polish
        self.assertEqual(len(textlist), len(langlist))
