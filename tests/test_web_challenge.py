import pytest
import allure
from pages.challenge_eleven_20_page import ChallengeElevenTwentyPage
from pages.challenge_one_ten_page import ChallengeOneTenPage
from pages.challenge_20_30_page import ChallengeTwentyThirtyPage

@allure.epic("The Internet Herokuapp")
@allure.feature("Giải quyết các bài toán Automation Challenges")
class TestChallengeOneTen:

    @allure.story("Challenges từ 1 đến 10")
    @allure.title("Thực thi các action cơ bản: Auth, Canvas, Checkbox...")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_challenge_one_ten(self, setup):
        driver, download_folder = setup
        challenge_one_ten_page = ChallengeOneTenPage(driver)
        
        with allure.step("Xử lý Basic Auth"):
            challenge_one_ten_page.basic_auth()
            
        with allure.step("Kiểm tra Broken Image"):
            challenge_one_ten_page.broken_image()
            
        with allure.step("Tương tác Canvas"):
            challenge_one_ten_page.do_canvas()
            
        with allure.step("Giải quyết Doom Challenge"):
            challenge_one_ten_page.doom_challenge()
            
        with allure.step("Tương tác Checkbox"):
            challenge_one_ten_page.do_checkbox()
            
        with allure.step("Xử lý Context Menu"):
            challenge_one_ten_page.context_menu()
            
        with allure.step("Kiểm tra Disappear Element"):
            challenge_one_ten_page.do_disappear_element()
            
        with allure.step("Thực hiện Drag and Drop"):
            challenge_one_ten_page.do_drag_and_drop()

    @allure.story("Challenges từ 11 đến 20")
    @allure.title("Thực thi các action trung cấp: Upload/Download file, Iframe, Dynamic Content...")
    @allure.severity(allure.severity_level.NORMAL)
    def test_challenge_eleven_20(self, setup):
        driver, download_folder = setup
        challenge_eleven_20_page = ChallengeElevenTwentyPage(driver)
        
        with allure.step("Tương tác Dropdown"):
            challenge_eleven_20_page.do_dropdown()

        with allure.step("Kiểm tra Dynamic Content"):
            challenge_eleven_20_page.do_dynamic_content()

        with allure.step("Xử lý Entry Ad (Modal Window)"):
            challenge_eleven_20_page.do_entry_ad()

        with allure.step("Xử lý Exit Intent Modal"):
            challenge_eleven_20_page.do_exit_intent()
        
        with allure.step(f"Download file về thư mục {download_folder}"):
            challenge_eleven_20_page.do_file_downloader(download_folder)
            
        with allure.step("Upload file text"):
            challenge_eleven_20_page.do_upload_file("2026-10-22-acme-some-file.txt")
            
        with allure.step("Kiểm tra Floating Menu"):
            challenge_eleven_20_page.do_floating_element()

        with allure.step("Xử lý Nested Frames và iFrame"):
            challenge_eleven_20_page.do_frame()

    @allure.story("Challenges từ 20 đến 30")
    @allure.title("Thực thi các action nâng cao: Geolocation, Slider, Alerts, Windows...")
    @allure.severity(allure.severity_level.NORMAL)
    def test_challenge_20_30(self, setup):
        driver, download_folder = setup
        challenge_20_30_page = ChallengeTwentyThirtyPage(driver)
        
        with allure.step("Lấy tọa độ Geolocation"):
            challenge_20_30_page.do_geolocation()

        with allure.step("Tương tác Horizontal Slider"):
            challenge_20_30_page.do_horizontal_slider()

        with allure.step("Xử lý JavaScript Alerts"):
            challenge_20_30_page.do_javascript_alerts()

        with allure.step("Chuyển đổi qua lại giữa các cửa sổ (Switch Window)"):
            challenge_20_30_page.do_switch_window()

        with allure.step("Kiểm tra Shifting Content"):
            challenge_20_30_page.do_shifting_content()
