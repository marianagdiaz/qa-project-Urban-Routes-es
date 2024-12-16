from selenium import webdriver
import data
from UrbanMethods import UrbanRoutesMethods
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.add_argument("--enable-logging")
        options.add_argument("--v=1")
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.URMethods= UrbanRoutesMethods(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesMethods(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_click_button_order_taxi_and_comfort_travel(self):
        self.URMethods.set_choose_comfort()
        assert self.URMethods.get_selected_plan()== 'Comfort'

    def test_add_number_and_code_number(self):
        self.URMethods.set_add_phone_number(data.phone_number, self.driver)
        assert self.URMethods.get_number_phone()==data.phone_number

    def test_set_add_payment_number_and_code_card(self):
        self.URMethods.set_add_method_payment(data.card_number, data.card_code)
        assert self.URMethods.get_card_number()==data.card_number

    def test_send_comment_to_driver(self):
        self.URMethods.send_driver_comment(data.message_for_driver)
        assert self.URMethods.get_comment_driver()==data.message_for_driver

    def test_choose_blanket(self):
        self.URMethods.click_slider_round_blanket()
        #Esta prueba no tendrá assert porque ninguna propiedad de los divs del checkbox cambia cuando se le hace click

    def test_add_icecream(self):
        self.URMethods.double_click_icecream()
        assert self.URMethods.get_icecream_number()=='2'

    def test_information_modal(self):
        self.URMethods.set_finish_order_and_taxi_modal()
        assert self.URMethods.get_information_taxi_modal()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
