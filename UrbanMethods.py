
from  UrbanLocators import UrbanRoutesLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class UrbanRoutesMethods:
    def __init__(self, driver):
        self.driver = driver
        self.locators= UrbanRoutesLocators


    def set_from(self, address_from):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.locators.from_field))
        self.driver.find_element(*self.locators.from_field).send_keys(address_from)

    def set_to(self, address_to):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.locators.to_field))
        self.driver.find_element(*self.locators.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.locators.to_field).get_property('value')

    def set_route(self,address_from,address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_button_order_taxi(self):
        self.driver.find_element(*self.locators.order_taxi_button).click()

    def click_button_choose_comfort(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.locators.comfort_button))
        self.driver.find_element(*self.locators.comfort_button).click()
#Paso para escoger tarifa comfort
    def set_choose_comfort(self):
        self.click_button_order_taxi()
        self.click_button_choose_comfort()

    def click_add_phone_number(self):
        self.driver.find_element(*self.locators.phone_button).click()

    def enter_phone_number(self,number_phone):
        self.driver.find_element(*self.locators.phone_field).send_keys(number_phone)

    def click_next_button(self):
        self.driver.find_element(*self.locators.next_button).click()

    def enter_phone_code(self,code):
        self.driver.find_element(*self.locators.code_field).send_keys(code)

    def click_confirmation_button(self):
        self.driver.find_element(*self.locators.confirmation_button).click()

#Paso para agregar número de telefono

    def set_add_phone_number(self,number_phone):
        self.click_add_phone_number()
        self.enter_phone_number(number_phone)
        self.click_next_button()

    def set_enter_phone_code(self,code):
        self.enter_phone_code(code)
        self.click_confirmation_button()

    def click_payment_method_button(self):
        self.driver.find_element(*self.locators.payment_method_button).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.locators.add_card_button).click()

    def add_card_number(self,number_card):
        self.driver.find_element(*self.locators.card_number_field).send_keys(number_card)

    def add_card_code(self,code_card):
        self.driver.find_element(*self.locators.card_code_field).send_keys(code_card + Keys.TAB)

    def click_add_payment_button(self):
        self.driver.find_element(*self.locators.add_payment_button).click()

    def click_close_method_button(self):
        self.driver.find_element(*self.locators.close_method_button).click()

#Paso para agregar tarjeta como pago

    def set_add_method_payment(self,number_card,code_card):
        self.click_payment_method_button()
        self.click_add_card_button()
        self.add_card_number(number_card)
        self.add_card_code(code_card)
        self.click_add_payment_button()
        self.click_close_method_button()


    def send_driver_comment(self,message_driver):
        self.driver.find_element(*self.locators.driver_comment_field).send_keys(message_driver)



    def click_slider_round_blanket(self):
        element_blanket=self.driver.find_element(*self.locators.slider_round_blanket)
        self.driver.execute_script("arguments[0].scrollIntoView();",element_blanket)
        self.driver.execute_script("arguments[0].click();",element_blanket)



    def double_click_icecream(self):
        self.driver.find_element(*self.locators.icecream_button).click()
        self.driver.find_element(*self.locators.icecream_button).click()



    def click_button_finish_order(self):
        self.driver.find_element(*self.locators.finish_order_taxi_button).click()

    def wait_taxi_modal(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.locators.taxi_modal))






