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
    def __init__(self, driver):
        super().__init__(driver)
        self.env_config = EnvConfig("dev")
        self.domain_geolocation = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["geolocation"]
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