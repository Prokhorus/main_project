from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Finish(Base):

    url = 'https://www.fishohota.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    continue_click = '//*[@id="one_click_buy_form_button"]'
    main_word = '//*[@id="main"]/div[13]/div[1]/div'

    """Getters"""

    def get_continue_click(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_click))
        )

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word))
        )

    """Actions"""

    def click_continue_click(self):
        element = self.get_continue_click()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        print("Click Place Order")

    """Methods"""

    def finish(self):
        self.get_current_url()
        self.click_continue_click()
        self.verify_successful_finish()

    """Methods assert word"""

    def verify_successful_finish(self):
        actual_text = self.get_main_word().text
        expected_text = 'Купить в 1 клик'
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
        print("Successful Finish")

