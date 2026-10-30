import pytest
import allure
from selenium import webdriver
import os

# 1. Thêm hook để lấy kết quả (passed/failed) của test case
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# 2. Truyền tham số request vào fixture setup
@pytest.fixture()
def setup(request):
    current_dir = os.getcwd()
    download_folder = os.path.join(current_dir, "download")
    
    # Đảm bảo thư mục tự động được tạo nếu chưa tồn tại
    os.makedirs(download_folder, exist_ok=True)
    
    options = webdriver.ChromeOptions()
    
    # Cấu hình prefs để ép Chrome tải file về đúng thư mục
    prefs = {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.default_content_setting_values.geolocation": 1
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless') # Chạy ẩn giao diện
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    yield driver, download_folder
    
    # 3. Chụp ảnh màn hình nếu test fail và đính kèm vào Allure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Screenshot_Fail_{request.node.name}",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Không thể chụp ảnh: {e}")

    driver.quit()