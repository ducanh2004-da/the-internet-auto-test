import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    download_folder = r"D:\Auto_Test\Selenium_Python\download"
    
    options = webdriver.ChromeOptions()
    
    # Cấu hình prefs để ép Chrome tải file về đúng thư mục
    prefs = {
        "download.default_directory": download_folder, # Thay đổi thư mục đích
        "download.prompt_for_download": False,         # Tắt hộp thoại "Save As"
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,                   # Bỏ qua cảnh báo bảo mật khi tải file
        # 1: Tự động Allow, 2: Tự động Block, 0: Hỏi lại (Mặc định)
        "profile.default_content_setting_values.geolocation": 1
    }
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver, download_folder
    driver.quit()