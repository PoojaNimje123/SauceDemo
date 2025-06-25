####pytest -v -s --html=Report/FirefoxReport.html --browser Firefox

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.Userlogin import Login
from utilities.read_properties import Read_Config


class Test_Login:
    url = Read_Config.get_url_page()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    name= Read_Config.get_name()
    lastname = Read_Config.get_lastname()
    postal_code = Read_Config.get_code()

    def test_user_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.PO_UL = Login(self.driver)
        self.PO_UL.enter_username(self.username)
        self.PO_UL.enter_password(self.password)
        self.PO_UL.click_login()
        success_login_msg = self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div').text
        if success_login_msg == 'Swag Labs':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_user_login.png")
            self.driver.close()
            assert False

    def test_add_to_card(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.PO_UL = Login(self.driver)
        self.PO_UL.enter_username(self.username)
        self.PO_UL.enter_password(self.password)
        self.PO_UL.click_login()
        self.PO_UL.click_product_add_card()
        self.PO_UL.click_cart_icon()
        success_add_cart_msg = self.driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
        if success_add_cart_msg == 'Your Cart':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_add_to_card.png")
            self.driver.close()
            assert False


    def test_checkout(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.PO_UL = Login(self.driver)
        self.PO_UL.enter_username(self.username)
        self.PO_UL.enter_password(self.password)
        self.PO_UL.click_login()
        self.PO_UL.click_product_add_card()
        self.PO_UL.click_cart_icon()
        self.PO_UL.click_checkout()
        self.PO_UL.enter_name(self.name)
        self.PO_UL.enter_last_name(self.lastname)
        self.PO_UL.enter_postal_code(self.postal_code)
        self.PO_UL.click_continue()
        self.PO_UL.click_finish()
        order_success_msg = self.driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2').text
        if order_success_msg=='Thank you for your order!':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_checkout.png")
            self.driver.close()
            assert False



