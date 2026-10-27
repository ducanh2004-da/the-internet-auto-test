from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.env_config import EnvConfig
from urllib.parse import urlparse
import time
import re
import os


class ChallengeTwentyThirtyPage(BasePage):
    GET_GEO_BTN = (By.XPATH, "//div[@class='example']/button")
    LONGITUDE_INFO = (By.XPATH, "//div[@id='long-value']")
    LATITUDE_INFO = (By.XPATH, "//div[@id='lat-value']")
    SLIDER = (By.XPATH, "//div[@class='sliderContainer']/input[@type='range']")
    NUMBER_RANGE = (By.ID, "range")
    JS_ALERT_BTN = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM_BTN = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT_BTN = (By.XPATH, "//button[text()='Click for JS Prompt']")
    CLICK_HERE_BTN = (By.LINK_TEXT, "Click Here")
    NEW_WINDOW_TEXT = (By.XPATH, "//h3[text()='New Window']")

    def __init__(self, driver):
        super().__init__(driver)
        self.env_config = EnvConfig("dev")
        self.domain_geolocation = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["geolocation"]
        )
        self.domain_horizontal_slider = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["horizontal_slider"]
        )
        self.domain_javascript_alerts = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["javascript_alerts"]
        )
        self.domain_windows = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["windows"]
        )
    
    def do_geolocation(self):
        self.open_page(self.domain_geolocation)
        time.sleep(2)
        self.wait_for_visible(self.GET_GEO_BTN)
        self.click_element(self.GET_GEO_BTN)
        lat_text = self.get_text(self.LATITUDE_INFO)
        long_text = self.get_text(self.LONGITUDE_INFO)
        assert lat_text != "", "Lỗi: Không lấy được Vĩ độ (Latitude)"
        assert long_text != "", "Lỗi: Không lấy được Kinh độ (Longitude)"
        self.logger.info("Geolocation test passed")

    def do_horizontal_slider(self):
        self.open_page(self.domain_horizontal_slider)
        time.sleep(2)
        self.click_element(self.SLIDER)
        slider = self.find_element(self.SLIDER)
        slider.send_keys(Keys.ARROW_RIGHT)
        current_val = self.get_text(self.NUMBER_RANGE)
        expected_val = "3"
        assert current_val == expected_val, "Lỗi: Giá trị hiện tại không bằng giá trị mong đợi"
        self.logger.info("Horizontal slider test passed")

    def do_javascript_alerts(self):
        self.open_page(self.domain_javascript_alerts)
        self.click_element(self.JS_ALERT_BTN)
        time.sleep(2)
        self.accept_alert()
        self.click_element(self.JS_CONFIRM_BTN)
        time.sleep(2)
        self.dismiss_alert()
        self.click_element(self.JS_PROMPT_BTN)
        time.sleep(2)
        self.enter_text_alert("Hello World")
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)
        self.logger.info("JavaScript alerts test passed")
    
    def do_switch_window(self):
        self.open_page(self.domain_windows)
        self.click_element(self.CLICK_HERE_BTN)
        time.sleep(2)
        self.switch_new_window()
        assert self.is_element_visible(self.NEW_WINDOW_TEXT), "Lỗi: Không chuyển được sang cửa sổ mới"
        time.sleep(2)
        self.back_to_origin_window()
        time.sleep(2)
        self.logger.info("Switch window test passed")




    