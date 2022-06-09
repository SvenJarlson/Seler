from selenium.webdriver.common.by import By

class HomePageLocators():
    """
    Locators used on Home Page
    """
    SIGN_IN_LINK = (By.CLASS_NAME, "sign-btn")
    # moze byc konieczny lokator najedz na konto aby byl widoczny przycisk zaloguj
    HOVER_ACCOUNT = (By.CLASS_NAME, "user-account-port")
    # miejsce do wpisania loginu
    LOGIN_BOX = (By.ID, "fm-login-id")
    # miejsce do wpisania hasla
    PASSWORD_BOX = (By.ID, "fm-login-password")
    # przycisk zaloguj
    LOGIN_BTN = (By.XPATH, "//button[@type="submit"]")
    # error message
    ERROR_MSG = (By.LINK_TEXT, "Nieprawidłowa nazwa logowania lub hasło logowania")


class PopUpsLocators():
    """
    Locators used on Pop ups
    """
    COOKIES_BTN = (By.LINK_TEXT, "Nie zezwalaj")
    DISCOUNT_AD_BTN = (By.CLASS_NAME, "btn-close")

class SelectWatchesLocators():
    """
    Locators used to access Watches page and filter it
    """
    #zakładka zegarki
    WATCHES_BTN = (By.LINK_TEXT, "Zegarki")
    #sortowanie po cenie
    PRICE_SORT = (By.CSS_SELECTOR, "span.sort-item[data-spm-anchor-id="a2g0o.productlist.0.i5.4b7f526ejsd1Be"]")
    #wybierz zegareki
    SELECT_WATCH = (By.CLASS_NAME, "_1RtJV product-img")
    #dodaj do koszyka
    ADD_TO_CART = (By.LINK_TEXT, "Dodaj do koszyka")
    #pokaż koszyk
    SHOW_CART = (By.XPATH, "//button[@ae_project_id="21200"]")
    #zaznacz przedmot w koszyku
    FIND_IN_CART = (By.XPATH, "//input[@ae_page_area="Item_card"]")
    #zlap cene
    GRAB_PRICE = (By.XPATH, "//div[@class="total-price"]//dd")