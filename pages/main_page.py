import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import Urls


class MainPage(BasePage):
    @allure.step("Клик на Заказать наверху страницы")
    def click_on_order_button_up(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_UP)
  
    @allure.step("Клик на Заказать внизу страницы")
    def click_on_order_button_down(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)
        self.wait_for_element_clickable(MainPageLocators.ORDER_BUTTON_DOWN)
        self.click_on_element(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Клик на логотип Самокат")
    def click_on_logo_scooter(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик на логотип Яндекс")
    def click_on_logo_yandex(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step("Клик на раздел FAQ 'Вопросы о важном'")
    def click_on_faq(self, question_number):
        self.scroll_to_element(MainPageLocators.FAQ_QUESTIONS[question_number])
        self.wait_for_element_clickable(MainPageLocators.FAQ_QUESTIONS[question_number])
        self.click_on_element(MainPageLocators.FAQ_QUESTIONS[question_number])

    @allure.step("Просмотр ответа в FAQ 'Вопросы о важном'")
    def get_faq_text_answers(self, answer_number):
        self.wait_for_element_visible(MainPageLocators.FAQ_ANSWERS[answer_number])
        return self.get_text_of_element(MainPageLocators.FAQ_ANSWERS[answer_number])

    @allure.step("Главная страница")
    def open_main_page(self):
        self.open_page(Urls.MAIN_URL)

    @allure.step("Главная страница открыта")
    def is_main_page_opened(self):
        return self.get_current_url() == Urls.MAIN_URL

    @allure.step("Переключение на вкладку Дзена и её открытие")
    def switch_to_dzen_and_wait(self):
        self.switch_to_another_tab()
        self.wait_for_url_to_contain("dzen.ru")

    @allure.step("Закрыть куки")
    def close_cookie_banner(self):
        if self.is_element_visible(MainPageLocators.COOKIE_BANNER_CLOSE_BUTTON):
            self.click_on_element(MainPageLocators.COOKIE_BANNER_CLOSE_BUTTON)