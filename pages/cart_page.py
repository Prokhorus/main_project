from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    url = 'https://www.fishohota.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    select_product = '//*[@id="bx_3966226736_358"]'
    add_to_cart = '//*[@id="bx_117848907_358_basket_actions"]/span'
    cart_button = '//*[@id="bx_117848907_358_basket_actions"]/a'
    place_order = '//*[@id="basket-root"]/div[1]/div/div/div[2]/div/div[4]/span'
    main_word = '//*[@id="pagetitle"]'

    """Getters"""

    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product))
        )

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart))
        )

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_button))
        )

    def get_place_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.place_order))
        )

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word))
        )

    """Actions"""

    def click_select_product(self):
        element = self.get_select_product()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        print("Click Select Product")

    def click_add_to_cart(self):
        element = self.get_add_to_cart()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        print("Click Add to Cart")

    def click_cart_button(self):
        element = self.get_cart_button()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        print("Click Cart Button")

    def click_place_order(self):
        element = self.get_place_order()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        print("Click Place Order")

    """Methods"""

    def product_confirmation(self):
        self.get_current_url()
        self.click_select_product()
        self.click_add_to_cart()
        self.click_cart_button()
        self.click_place_order()
        self.verify_successful_cart()

    """Methods assert word"""

    def verify_successful_cart(self):
        actual_text = self.get_main_word().text
        expected_text = 'Корзина'
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
        print("Successful Cart")
