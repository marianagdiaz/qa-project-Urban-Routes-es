from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button=(By.CSS_SELECTOR, "button.button.round")
    comfort_button= (By.CSS_SELECTOR, "div .tcard:nth-of-type(5)")
    comfort_button_title = (By.CSS_SELECTOR, "div .tcard:nth-of-type(5) .tcard-title")
    phone_button= (By.CLASS_NAME, 'np-button')
    phone_field =(By.ID,'phone')
    next_button=(By.XPATH, "//button[text()='Siguiente']")
    code_field=(By.ID,'code')
    confirmation_button = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_button= (By.CLASS_NAME,'pp-text')
    add_card_button=(By.CSS_SELECTOR,'div.pp-row.disabled')
    card_number_field=(By.ID,'number')
    card_code_field=(By.CSS_SELECTOR,'.card-code-input #code')
    add_payment_button=(By.XPATH, "//button[text()='Agregar']")
    close_method_button=(By.CSS_SELECTOR,'.payment-picker .modal .active .close-button')
    driver_comment_field=(By.ID,'comment')
    slider_round_blanket=(By.XPATH,'/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    icecream_button = (By.CSS_SELECTOR, '.r-counter-container .r-counter .counter .counter-plus')
    icecream_number=(By.XPATH,'/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    finish_order_taxi_button=(By.CLASS_NAME,'smart-button')
    taxi_modal=(By.CLASS_NAME, 'order-body')
    information_driver=(By.CLASS_NAME,'order-subbody')

