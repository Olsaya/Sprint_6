import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Выбор станции метро")
    def select_metro_station(self, station_name):
        self.send_keys_to_element(OrderPageLocators.METRO_STATION, station_name)
        self.wait_for_element_visible(OrderPageLocators.METRO_STATION_LIST)
        stations = self.driver.find_elements(*OrderPageLocators.METRO_STATION_LIST)
        stations[0].click()

    @allure.step("Выбор срока аренды")
    def select_rental_period(self, period_name):
        period_locators = {
            "сутки": OrderPageLocators.RENTAL_PERIOD_ONE_DAY,
            "двое суток": OrderPageLocators.RENTAL_PERIOD_TWO_DAYS
        }
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_on_element(period_locators[period_name])

    @allure.step("Выбор цвета самоката")
    def select_scooter_color(self, color_name):
        color_locators = {
            "black": OrderPageLocators.SCOOTER_BLACK_COLOUR,
            "grey": OrderPageLocators.SCOOTER_GREY_COLOUR
        }
        self.click_on_element(color_locators[color_name])

    @allure.step("Заполнение формы  Для кого самокат")
    def fill_first_form(self, data):
        self.wait_for_element_visible(OrderPageLocators.NAME)
        self.send_keys_to_element(OrderPageLocators.NAME, data["name"])
        self.send_keys_to_element(OrderPageLocators.LAST_NAME, data["last_name"])
        self.send_keys_to_element(OrderPageLocators.ADDRESS, data["address"])
        self.select_metro_station(data["metro_station"])
        self.send_keys_to_element(OrderPageLocators.PHONE_NUMBER, data["phone"])
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнение формы  Про аренду")
    def fill_second_form(self, data):
        self.send_keys_to_element(OrderPageLocators.DELIVERY_DATE, data["delivery_date"])
        self.click_on_element(OrderPageLocators.HEADER_ORDER)
        self.select_rental_period(data["rental_period"])
        self.select_scooter_color(data["scooter_color"])
        self.send_keys_to_element(OrderPageLocators.COMMENT, data["comment"])
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Подтверждение заказа нажатием на Да")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.BUTTON_YES)

    @allure.step("Успешное оформление заказа")
    def is_order_placed(self):
        return self.is_element_visible(OrderPageLocators.HEADER_SUCCESS)

    @allure.step("Текст сообщения об успешном заказе отображается")
    def get_success_message(self):
        return self.get_text_of_element(OrderPageLocators.HEADER_SUCCESS)