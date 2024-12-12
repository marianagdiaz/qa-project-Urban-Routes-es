

from selenium import webdriver
import data
from UrbanMethods import UrbanRoutesMethods
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options




# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code







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

    def test_add_number_and_code_number(self):
        self.URMethods.set_add_phone_number(data.phone_number)


    def test_add_number_code_phone(self):
        self.URMethods.set_enter_phone_code(retrieve_phone_code(self.driver))

    def test_set_add_payment_number_and_code_card(self):
        self.URMethods.set_add_method_payment(data.card_number,data.card_code)

    def test_send_comment_to_driver(self):
        self.URMethods.send_driver_comment(data.message_for_driver)


    def test_choose_blanket(self):
        self.URMethods.click_slider_round_blanket()

    def test_add_icecream(self):
        self.URMethods.double_click_icecream()

    def test_click_button_finish_order(self):
        self.URMethods.click_button_finish_order()


    def test_wait_information_modal(self):
        self.URMethods.wait_taxi_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
