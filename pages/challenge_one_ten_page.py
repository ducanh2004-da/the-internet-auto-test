from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.env_config import EnvConfig
from urllib.parse import urlparse
import time
import re

class ChallengeOneTenPage(BasePage):
    # Định nghĩa locator ở cấp Class
    IMAGES_LOCATOR = (By.TAG_NAME, "img")
    BASIC_AUTH_LINK = (By.XPATH, "//a[@href='/basic_auth']")
    CANVAS_LOCATOR = (By.ID, "canvas")
    RESULT_CANVAS = (By.ID, "canvas-log")
    BAZ_DARK_BTN = (By.CSS_SELECTOR, "a.button:not(.alert):not(.success)")
    BAZ_RED_BTN = (By.CSS_SELECTOR, "a.button.alert")
    BAZ_GREEN_BTN = (By.CSS_SELECTOR, "a.button.success")
    CHECKBOX_01 = (By.CSS_SELECTOR, "input[type='checkbox']:nth-of-type(1)")
    CHECKBOX_02 = (By.CSS_SELECTOR, "input[type='checkbox']:nth-of-type(2)")
    CONTEXT_MENU = (By.ID, "hot-spot")
    GALLERY_BTN = (By.LINK_TEXT, "Gallery")    
    BOX_A = (By.ID, "column-a")                               
    BOX_B = (By.ID, "column-b")                           

    def __init__(self, driver):
        super().__init__(driver)
        self.env_config = EnvConfig("dev")
        self.domain_basic_auth = urlparse(
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["basic_auth"]
        ).netloc
        self.domain_broken_image = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["broken_image"]
        )
        self.domain_canvas = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["canvas"]
        )
        self.domain_doom_challenge = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["challenge_DOM"]
        )
        self.domain_checkbox = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["check_boxes"]
        )
        self.domain_context_menu = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["context_menu"]
        )
        self.domain_disappear_element = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["disappear_elements"]
        )
        self.domain_drag_drop = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["drag_drop"]
        )

    def basic_auth(self):
        username = 'admin'
        password = 'admin'
        auth_url = f"https://{username}:{password}@{self.domain_basic_auth}/"
        self.open_page(auth_url)
        time.sleep(2)
        auth_link = self.click_element(self.BASIC_AUTH_LINK)
        time.sleep(2)

    def broken_image(self):
        # 1. Mở trang web trước
        self.open_page(self.domain_broken_image)
        time.sleep(2)
        
        # 2. Sau khi trang đã tải, mới tìm toàn bộ các thẻ img
        images = self.find_elements(self.IMAGES_LOCATOR)
        
        # 3. Đếm ảnh lỗi
        num_broken_image = 0
        for image in images:
            # Ép kiểu an toàn hoặc dùng JS execute
            width = self.driver.execute_script("return arguments[0].naturalWidth;", image)
            if width == 0:
                num_broken_image += 1
                
        self.logger.info(f"Number of broken images: {num_broken_image}")
        return num_broken_image

    def get_clicked_coordinate(self):
        result_text = self.get_text(self.RESULT_CANVAS)
        numbers = re.findall(r'\d+', result_text)
        if len(numbers) == 2:
            x = int(numbers[0])
            y = int(numbers[1])
            return x, y
        else:
            self.logger.error("Không tìm thấy tọa độ")
            return None, None

    def do_canvas(self):
        self.open_page(self.domain_canvas)
        time.sleep(2)

        canvas_inp = self.find_element(self.CANVAS_LOCATOR)
        
        self.click_at_coordinate(self.CANVAS_LOCATOR, 100, 100)
        
        actual_x, actual_y = self.get_clicked_coordinate()
        self.logger.info(f"UI nhận tọa độ click tại X: {actual_x}, Y: {actual_y}")
        assert actual_x is not None and actual_y is not None, "Không tìm thấy tọa độ trên UI"
        assert actual_x > 0 and actual_y > 0, "Tọa độ click không hợp lệ (phải lớn hơn 0)"
        
        self.click_and_type(self.CANVAS_LOCATOR, "Hello World")
        actual_result = self.get_text(self.RESULT_CANVAS)
        
        assert "Hello World" in actual_result, "Canvas test failed: Content not found"
        self.logger.info("Canvas test hoàn tất thành công")

    def click_edit_by_ipsum_value(self, ipsum_text):
        dynamic_edit_btn = f"//td[text()='{ipsum_text}']/parent::tr//a[@href='#edit']"
        specific_edit_btn = (By.XPATH, dynamic_edit_btn)
        self.click_element(specific_edit_btn)
        time.sleep(2)

    def doom_challenge(self):
        self.open_page(self.domain_doom_challenge)
        time.sleep(2)

        baz_dark_btn = self.find_element(self.BAZ_DARK_BTN)
        baz_red_btn = self.find_element(self.BAZ_RED_BTN)
        baz_green_btn = self.find_element(self.BAZ_GREEN_BTN)

        self.click_element(self.BAZ_DARK_BTN)
        self.click_element(self.BAZ_RED_BTN)
        self.click_element(self.BAZ_GREEN_BTN)

        time.sleep(2)

        self.click_edit_by_ipsum_value("Iuvaret4")

        time.sleep(2)

    def do_checkbox(self):
        self.open_page(self.domain_checkbox)
        time.sleep(2)
        self.click_element(self.CHECKBOX_01)
        time.sleep(2)
        self.click_element(self.CHECKBOX_02)
        time.sleep(2)

    def context_menu(self):
        self.open_page(self.domain_context_menu)
        time.sleep(2)
        self.right_click(self.CONTEXT_MENU)
        time.sleep(2)
        self.accept_alert()
        time.sleep(2)

    def do_disappear_element(self, max_retries = 5):
        self.open_page(self.domain_disappear_element)
        time.sleep(2)

        for i in range(max_retries):
            if self.is_element_present(self.GALLERY_BTN):
                self.click_element(self.GALLERY_BTN)
                self.logger.info("Gallery button is present")
                return True
            self.driver.refresh()
            self.logger.info(f"Page refreshed, retry {i + 1}/{max_retries}")
            time.sleep(2)
        
        self.logger.error(f"Gallery button not found after {max_retries} retries")
        return False
    
    def do_drag_and_drop(self):
        self.open_page(self.domain_drag_drop)
        time.sleep(2)
        self.drag_and_drop(self.BOX_A, self.BOX_B)
        time.sleep(2)


        

        
        
        

    