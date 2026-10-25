from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.env_config import EnvConfig
from urllib.parse import urlparse
import time
import re

class ChallengeElevenTwentyPage(BasePage):
    # Định nghĩa locator ở cấp Class                     

    DROPDOWN = (By.ID, "dropdown")   
    OPTION = (By.XPATH, "//option[@value='2']")  
    IMG_01 =(By.XPATH, "//div[@id='content']/div[@class='row'][1]/div[1]/img")
    CONTENT_IMG_01 = (By.XPATH, "//div[@id='content']/div[@class='row'][1]/div[2]")
    IMG_02 =(By.XPATH, "//div[@id='content']/div[@class='row'][2]/div[1]/img")
    CONTENT_IMG_02 = (By.XPATH, "//div[@id='content']/div[@class='row'][2]/div[2]")
    IMG_03 =(By.XPATH, "//div[@id='content']/div[@class='row'][3]/div[1]/img")
    CONTENT_IMG_03 = (By.XPATH, "//div[@id='content']/div[@class='row'][3]/div[2]")
    CLOSE_BTN_MODAL = (By.XPATH, "//div[@id='modal']/div[@class='modal']/div[@class='modal-footer']/p")
    HEADER_MODAL = (By.XPATH, "//div[@class='modal-title']/h3[contains(text(), 'modal window')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.env_config = EnvConfig("dev")
        self.domain_dropdown = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["dropdown"]
        )
        self.domain_dynamic_content = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["dynamic_content"]
        )
        self.domain_entry_ad = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["entry_ad"]
        )

    def do_dropdown(self):
        self.open_page(self.domain_dropdown)
        time.sleep(2)
        self.click_element(self.DROPDOWN)
        time.sleep(2)
        self.click_element(self.OPTION)
        time.sleep(2)
        dropdown_element = self.find_element(self.DROPDOWN)
        select_obj = Select(dropdown_element)
        select_obj.select_by_value("2")
        time.sleep(2)
        actual_text = select_obj.first_selected_option.text
        assert actual_text == "Option 2", f"Verify failed, Expected 'Option 2', but got '{actual_text}'"
        self.logger.info("Dropdown test passed")
    
    def do_dynamic_content(self):
        self.open_page(self.domain_dynamic_content)
        time.sleep(2)
        initial_content_img_01_text = self.get_text(self.CONTENT_IMG_01)
        initial_content_img_02_text = self.get_text(self.CONTENT_IMG_02)
        initial_content_img_03_text = self.get_text(self.CONTENT_IMG_03)
        if self.is_element_visible(self.IMG_01) or self.is_element_visible(self.IMG_02) or self.is_element_visible(self.IMG_03):
            self.logger.info("All images are visible")
        else:
            self.logger.error("One of three images are not visible")
            assert False, "All images are not visible"
        self.driver.refresh()
        new_content_img_01_text = self.get_text(self.CONTENT_IMG_01)
        new_content_img_02_text = self.get_text(self.CONTENT_IMG_02)
        new_content_img_03_text = self.get_text(self.CONTENT_IMG_03)
        if self.is_element_visible(self.IMG_01) or self.is_element_visible(self.IMG_02) or self.is_element_visible(self.IMG_03):
            self.logger.info("All images are visible")
        else:
            self.logger.error("One of three images are not visible")
            assert False, "All images are not visible"  
        
        assert initial_content_img_01_text != new_content_img_01_text, f"Text is not change {initial_content_img_01_text} -> {new_content_img_01_text}"
        assert initial_content_img_02_text != new_content_img_02_text, f"Text is not change {initial_content_img_02_text} -> {new_content_img_02_text}"
        assert initial_content_img_03_text != new_content_img_03_text, f"Text is not change {initial_content_img_03_text} -> {new_content_img_03_text}"
        self.logger.info("Dynamic content test passed")

    def do_entry_ad(self):
        self.open_page(self.domain_entry_ad)
        time.sleep(2)
        assert self.is_element_visible(self.HEADER_MODAL), "Entry ad test failed"
        self.click_element(self.CLOSE_BTN_MODAL)
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        assert self.is_element_visible(self.HEADER_MODAL) == False, "Entry ad test failed"
        self.logger.info("Entry ad test passed")
