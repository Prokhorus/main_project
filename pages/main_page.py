from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://fishohota.ru/'

    """Locators"""

    product_category = '//*[@id="header"]/div[2]/div[1]/div/div/div[3]/div/div/nav/div/table/tbody/tr/td[2]/div/a'
    product_selection = '//*[@id="header"]/div[2]/div[1]/div/div/div[3]/div/div/nav/div/table/tbody/tr/td[2]/div/ul/li[1]/ul/li[4]/a'
    filter_min = '//*[@id="NEXT_SMART_FILTER_P1_MIN"]'
    filter_max = '//*[@id="NEXT_SMART_FILTER_P1_MAX"]'
    apply_filter = '//*[@id="modef"]/a'
    main_word = '//*[@id="pagetitle"]'

    """Getters"""

    def get_product_category(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_category))
        )

    def get_product_selection(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_selection))
        )

    def get_filter_min(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_min))
        )

    def get_filter_max(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_max))
        )

    def get_apply_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.apply_filter))
        )

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word))
        )

    """Actions"""

    def click_product_selection(self):
        element = self.get_product_selection()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        print("Click Select Product Selection")

    def click_product_category(self):
        element = self.get_product_category()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        print("Click Select Product Category")

    def input_filter_min(self, filter_min):
        self.get_filter_min().send_keys(filter_min)

    def input_filter_max(self, filter_max):
        self.get_filter_max().send_keys(filter_max)

    def click_apply_filter(self):
        element = self.get_apply_filter()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        print("Click Apply Filter")

    """Method"""

    def select_product(self):
        self.get_current_url()
        self.click_product_category()
        self.click_product_selection()
        self.input_filter_min('50000')
        self.input_filter_max('150000')
        self.click_apply_filter()
        self.assert_word(self.get_main_word(), "Мотоциклы дорожные")

