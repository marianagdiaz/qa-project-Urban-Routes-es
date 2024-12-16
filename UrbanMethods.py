from UrbanLocators import UrbanRoutesLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

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
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.locators.order_taxi_button))
        self.driver.find_element(*self.locators.order_taxi_button).click()


    def click_button_choose_comfort(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.locators.comfort_button))
        self.driver.find_element(*self.locators.comfort_button).click()

#Paso para escoger tarifa comfort
    def set_choose_comfort(self):
        self.click_button_order_taxi()
        self.click_button_choose_comfort()

    def get_selected_plan(self):
        return self.driver.find_element(*self.locators.comfort_button_title).text

    def click_add_phone_number(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.phone_button))
        self.driver.find_element(*self.locators.phone_button).click()

    def enter_phone_number(self,number_phone):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.phone_field))
        self.driver.find_element(*self.locators.phone_field).send_keys(number_phone)

    def get_number_phone(self):
        return self.driver.find_element(*self.locators.phone_field).get_property('value')

    def click_next_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.next_button))
        self.driver.find_element(*self.locators.next_button).click()

    def enter_phone_code(self,code):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.code_field))
        self.driver.find_element(*self.locators.code_field).send_keys(code)

    def click_confirmation_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.confirmation_button))
        self.driver.find_element(*self.locators.confirmation_button).click()

#Paso para agregar número de telefono

    def set_add_phone_number(self,number_phone,driver):
        self.click_add_phone_number()
        self.enter_phone_number(number_phone)
        self.click_next_button()
        self.enter_phone_code(retrieve_phone_code(driver))
        self.click_confirmation_button()

    def click_payment_method_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.payment_method_button))
        self.driver.find_element(*self.locators.payment_method_button).click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.add_card_button))
        self.driver.find_element(*self.locators.add_card_button).click()

    def add_card_number(self,number_card):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.card_number_field))
        self.driver.find_element(*self.locators.card_number_field).send_keys(number_card)

    def get_card_number(self):
        return self.driver.find_element(*self.locators.card_number_field).get_property('value')

    def add_card_code(self,code_card):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.card_code_field))
        self.driver.find_element(*self.locators.card_code_field).send_keys(code_card + Keys.TAB)

    def click_add_payment_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.add_payment_button))
        self.driver.find_element(*self.locators.add_payment_button).click()

    def click_close_method_button(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.close_method_button))
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
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.driver_comment_field))
        self.driver.find_element(*self.locators.driver_comment_field).send_keys(message_driver)

    def get_comment_driver(self):
        return self.driver.find_element(*self.locators.driver_comment_field).get_property('value')

    def click_slider_round_blanket(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locators.slider_round_blanket))
        self.driver.find_element(*self.locators.slider_round_blanket).click()

    def double_click_icecream(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.locators.icecream_button))
        self.driver.find_element(*self.locators.icecream_button).click()
        self.driver.find_element(*self.locators.icecream_button).click()

    def get_icecream_number(self):
        return self.driver.find_element(*self.locators.icecream_number).text


    def click_button_finish_order(self):
        self.driver.find_element(*self.locators.finish_order_taxi_button).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.locators.taxi_modal))

    def wait_taxi_modal(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.locators.taxi_modal))

    def set_finish_order_and_taxi_modal(self):
        self.click_button_finish_order()
        self.wait_taxi_modal()

    def get_information_taxi_modal(self):
        modal=self.driver.find_element(*self.locators.taxi_modal).is_displayed()
        return modal




