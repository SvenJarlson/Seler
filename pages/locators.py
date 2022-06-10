from selenium.webdriver.common.by import By


class HomePageLocators:
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
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    # error message
    ERROR_MSG = (By.LINK_TEXT, "Nieprawidłowa nazwa logowania lub hasło logowania")


class PopUpsLocators:
    """
    Locators used on Pop-ups
    """
    COOKIES_BTN2 = (By.CLASS_NAME, "_24EHh")
    COOKIES_BTN = (By.CLASS_NAME, "btn-accept")
    DISCOUNT_AD_BTN = (By.CLASS_NAME, "btn-close")


class SelectWatchesLocators:
    """
    Locators used to access Watches page and filter it
    """
    # watches page
    WATCHES_BTN = (By.LINK_TEXT, "Zegarki")
    # sort by price
    PRICE_SORT = (By.CSS_SELECTOR, "span.sort-item[ae_object_value='price(lowest)']")
    # select watch
    SELECT_WATCH = (By.CLASS_NAME, "_3t7zg")
    # add to cart
    ADD_TO_CART = (By.XPATH, "//*[@id='root']/div/div[2]/div/div[2]/div[13]/span[2]/button")
    # show cart
    SHOW_CART = (By.XPATH, "//button[@ae_project_id='21200']")
    # select item in cart
    FIND_IN_CART = (By.XPATH, "//input[@ae_page_area='Item_card']")
    # locate price
    GRAB_PRICE = (By.XPATH, "//div[@class='total-price']//dd")
