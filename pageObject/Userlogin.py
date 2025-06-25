from selenium.webdriver.common.by import By

class Login:
        user_id = 'user-name'
        user_password_id = 'password'
        login_button_id = 'login-button'
        product_click_add_card_id = '//*[@id="add-to-cart-sauce-labs-backpack"]'
        click_cart_xpath= ' //*[@id="shopping_cart_container"]/a'
        click_checkout_button_id = 'checkout'
        enter_name_id = 'first-name'
        enter_lastname_id = 'last-name'
        enter_code_id = 'postal-code'
        click_continue_button_id = 'continue'
        click_finish_button_id= 'finish'


        def __init__(self, driver):
            self.driver = driver


        def enter_username(self, username):
            self.driver.find_element(By.ID, self.user_id).send_keys(username)

        def enter_password(self, password):
            self.driver.find_element(By.ID, self.user_password_id).send_keys(password)

        def click_login(self):
            self.driver.find_element(By.ID, self.login_button_id).click()

        def click_product_add_card(self):
            self.driver.find_element(By.XPATH, self.product_click_add_card_id).click()

        def click_cart_icon(self):
            self.driver.find_element(By.XPATH, self.click_cart_xpath).click()

        def click_checkout(self):
            self.driver.find_element(By.ID, self.click_checkout_button_id).click()

        def enter_name(self,name):
            self.driver.find_element(By.ID, self.enter_name_id).send_keys(name)

        def enter_last_name(self,surname):
            self.driver.find_element(By.ID, self.enter_lastname_id).send_keys(surname)

        def enter_postal_code(self,code):
            self.driver.find_element(By.ID, self.enter_code_id).send_keys(code)

        def click_continue(self):
            self.driver.find_element(By.ID, self.click_continue_button_id).click()

        def click_finish(self):
            self.driver.find_element(By.ID, self.click_finish_button_id).click()


