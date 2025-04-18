from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Client_info(Base):

    url = 'https://www.fishohota.ru/'

    """Locators"""

    first_name = '//*[@id="one_click_buy_id_FIO"]'
    phone = '//*[@id="one_click_buy_id_PHONE"]'
    email = '//*[@id="one_click_buy_id_EMAIL"]'

    """Getters"""

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name))
        )

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone))
        )

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email))
        )

    """Actions"""

    def input_first_name(self, first_name):
        first_name_input = self.get_first_name()
        first_name_input.clear()  # Очищаем поле
        first_name_input.send_keys(first_name)  # Записываем новое значение
        print("Input First Name")

    def input_phone(self, phone):
        phone_input = self.get_phone()
        phone_input.clear()  # Очищаем поле
        phone_input.send_keys(phone)  # Записываем новое значение
        print("Input Phone")

    def input_email(self, email):
        email_input = self.get_email()
        email_input.clear()  # Очищаем поле
        email_input.send_keys(email)  # Записываем новое значение
        print("Input Postal Code")

    """Methods"""

    def client_information(self):
        self.get_current_url()
        self.input_first_name('Prokhorov Aleksey Andreevitch')
        self.input_phone('+7999999999')
        self.input_email('prokhorusp@gmail.com')



