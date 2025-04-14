from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.cart_page import Cart_page
from pages.client_info_page import Client_info
from pages.finish import Finish
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_by_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--headless")
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    print("Start Test")

    login = Login_page(driver)
    login.authorization('prokhorusp@gmail.com', 'Prokhorov92')

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.product_confirmation()

    ci = Client_info(driver)
    ci.client_information()

    f = Finish(driver)
    f.finish()

    driver.quit()
