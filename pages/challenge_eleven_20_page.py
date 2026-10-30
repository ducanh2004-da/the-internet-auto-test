from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.env_config import EnvConfig
from urllib.parse import urlparse
import time
import re
import os

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
    MODAL_WINDOW_TITLE = (By.XPATH, "//div[@class='modal-title']/h3")
    CLOSE_MODAL_WINDOW = (By.XPATH, "//div[@class='modal-footer']/p[contains(text(), 'Close')]")
    TEXT_FILE_DOWNLOAD = (By.LINK_TEXT, "2026-10-22-acme-some-file.txt")
    FILE_UPLOAD_INP = (By.ID, "file-upload")
    UPLOAD_BTN = (By.ID, "file-submit")
    UPLOAD_SUCCESS_HEAD = (By.XPATH, "//div[@class='example']/h3")
    UPLOADED_FILES = (By.XPATH, "//div[@class='example']/div[@id='uploaded-files']")
    FLOAT_MENU = (By.ID, "menu")
    FRAME_BODY_TEXT = (By.TAG_NAME, "body")
    FRAME_CONTENT_TEXT = (By.ID, "content")
    NESTED_FRAME_LINK = (By.LINK_TEXT, "Nested Frames")
    IFRAME_LINK = (By.LINK_TEXT, "iFrame")
    IFRAME_INP = (By.ID, "mce_0_ifr")
    TINY_MCE = (By.ID, "tinymce")

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
        self.domain_exit_intent = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["exit_intent"]
        )
        self.domain_file_downloader = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["file_download"]
        )
        self.domain_file_upload = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["file_upload"]
        )
        self.domain_floating_menu = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["floating_menu"]
        )
        self.domain_frame = (
            self.env_config.config["base_url"] + self.env_config.config["endpoints"]["i_frame"]
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
        assert self.is_element_invisible(self.HEADER_MODAL), "Entry ad test failed"
        self.logger.info("Entry ad test passed")

    def do_exit_intent(self):
        self.open_page(self.domain_exit_intent)
        time.sleep(2)
        modal_js = """
        var event = new MouseEvent('mouseleave', {
            'bubbles': true,
            'cancelable': true,
            'clientX': 0,
            'clientY': -10 
        });
        document.documentElement.dispatchEvent(event);
        """
        self.execuate_script(modal_js)
        time.sleep(2)
        modal_window_title = self.get_text(self.MODAL_WINDOW_TITLE)
        modal_close = self.find_element(self.CLOSE_MODAL_WINDOW)
        assert modal_window_title == "THIS IS A MODAL WINDOW", f"Exit intent test failed, Expected 'THIS IS A MODAL WINDOW', but got '{modal_window_title}'"
        self.logger.info("Exit intent test passed")
        self.wait_for_visible(self.CLOSE_MODAL_WINDOW)
        self.click_element(self.CLOSE_MODAL_WINDOW)

    def do_file_downloader(self, download_folder):
        self.open_page(self.domain_file_downloader)
        self.click_element(self.TEXT_FILE_DOWNLOAD)
        
        file_name = "2026-10-22-acme-some-file.txt"
        file_path = os.path.join(download_folder, file_name)
        
        timeout = 15
        for i in range(timeout):
            if os.path.exists(file_path):
                self.logger.info(f"File downloaded successfully at: {file_path}")
                break
            time.sleep(1) 
        else:
            # Nếu hết 15 vòng lặp (15s) mà vẫn không thấy file
            self.logger.error(f"File not downloaded after {timeout} seconds")
            assert False, "File not downloaded"

    def do_upload_file(self, file_name):
        self.open_page(self.domain_file_upload)
        
        # Dùng os.getcwd() kết hợp abspath để đảm bảo đường dẫn chuẩn xác trên Linux
        root_dir = os.getcwd()
        file_path = os.path.abspath(os.path.join(root_dir, 'FileToUpload', file_name))
        
        if os.path.exists(file_path):
            self.logger.info(f"File exists at: {file_path}")
        else:
            self.logger.error(f"File not exists at: {file_path}")
            assert False, f"File không tồn tại để upload: {file_path}"
            
        self.enter_text(self.FILE_UPLOAD_INP, file_path)
        self.click_element(self.UPLOAD_BTN)
        
        time.sleep(2)
        
        upload_success_title = self.get_text(self.UPLOAD_SUCCESS_HEAD)
        uploaded_file = self.get_text(self.UPLOADED_FILES)
        
        assert upload_success_title == "File Uploaded!", f"Upload success title is not 'File Uploaded!' but got '{upload_success_title}'"
        assert file_name in uploaded_file, f"Uploaded file is not '{file_name}' but got '{uploaded_file}'"
        self.logger.info("Upload file test passed")

    def do_floating_element(self):
        self.open_page(self.domain_floating_menu)
        time.sleep(2)
        assert self.is_element_visible(self.FLOAT_MENU), "Floating menu test failed"
        float_element_js = """
        window.scrollTo(0, document.body.scrollHeight);
        """
        self.execuate_script(float_element_js)
        time.sleep(2)
        assert self.is_element_visible(self.FLOAT_MENU), "Floating menu test failed"
        self.logger.info("Floating menu test passed")

    def do_frame(self):
        self.open_page(self.domain_frame)
        time.sleep(2)
        self.click_element(self.NESTED_FRAME_LINK)
        time.sleep(2)
        self.switch_frame_by_name("frame-top")
        self.switch_frame_by_name("frame-left")
        left_content = self.get_text(self.FRAME_BODY_TEXT)
        assert left_content == "LEFT", f"Left content is not 'LEFT' but got '{left_content}'"
        time.sleep(2)
        self.switch_parent_frame()
        self.switch_frame_by_name("frame-middle")
        middle_content = self.get_text(self.FRAME_CONTENT_TEXT)
        assert middle_content == "MIDDLE", f"Middle content is not 'MIDDLE' but got '{middle_content}'"
        time.sleep(2)
        self.switch_parent_frame()
        self.switch_frame_by_name("frame-right")
        right_content = self.get_text(self.FRAME_BODY_TEXT)
        assert right_content == "RIGHT", f"Right content is not 'RIGHT' but got '{right_content}'"
        time.sleep(2)
        self.switch_default_content()
        self.switch_frame_by_name("frame-bottom")
        bottom_content = self.get_text(self.FRAME_BODY_TEXT)
        assert bottom_content == "BOTTOM", f"Bottom content is not 'BOTTOM' but got '{bottom_content}'"
        time.sleep(2)
        self.switch_parent_frame()
        self.logger.info("Nested Frame test passed")
        self.open_page(self.domain_frame)
        time.sleep(2)
        self.click_element(self.IFRAME_LINK)
        time.sleep(2)
        self.wait_for_visible(self.IFRAME_INP)
        self.switch_frame(self.IFRAME_INP)
        self.wait_for_visible(self.TINY_MCE)
        self.clear_text(self.TINY_MCE)
        test_text = "hello from Selenium"
        self.enter_text(self.TINY_MCE, test_text)
        actual_text = self.get_text(self.TINY_MCE)
        assert actual_text == test_text, f"Iframe content is not '{test_text}' but got '{actual_text}'"
        self.switch_default_content()
        self.logger.info("Iframe test passed")

    




        



    
