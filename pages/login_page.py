from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Login_page(Base):

    url = 'https://www.fishohota.ru/'

    """Locators"""

    LOGIN_WINDOW_LOCATOR = '//*[@id="header"]/div[1]/div/div/div/div[5]'
    USER_NAME_FIELD_LOCATOR = '//*[@id="USER_LOGIN_POPUP"]'
    PASSWORD_FIELD_LOCATOR = '//*[@id="USER_PASSWORD_POPUP"]'
    BUTTON_LOGIN_LOCATOR = '//*[@id="avtorization-form"]/div[3]/div[2]/input'
    MAIN_WORD_LOCATOR = '//*[@id="wrap_ajax_auth"]/div[1]/h2'

    """Getters"""

    def get_login_window(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LOGIN_WINDOW_LOCATOR))
        )

    def get_user_name_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.USER_NAME_FIELD_LOCATOR))
        )

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.PASSWORD_FIELD_LOCATOR))
        )

    def get_button_login(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.BUTTON_LOGIN_LOCATOR))
        )

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.MAIN_WORD_LOCATOR))
        )

    """Actions"""

    def click_login_window(self):
        self.get_login_window().click()
        print("Clicked Login Window")

    def enter_username(self, username):
        self.get_user_name_field().clear()
        self.get_user_name_field().send_keys(username)
        print(f"Entered Username: {username}")

    def enter_password(self, password):
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)
        print(f"Entered Password: {password}")

    def click_login_button(self):
        self.get_button_login().click()
        print("Clicked Login Button")

    """Methods"""

    def authorization(self, username, password):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_login_window()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.get_current_url()
        self.assert_word(self.get_main_word(), "Личный кабинет")

