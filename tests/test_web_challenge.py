from pages.challenge_eleven_20_page import ChallengeElevenTwentyPage
from pages.challenge_one_ten_page import ChallengeOneTenPage
from pages.challenge_20_30_page import ChallengeTwentyThirtyPage

class TestChallengeOneTen:

    def test_challenge_one_ten(self, setup):
        driver = setup
        challenge_one_ten_page = ChallengeOneTenPage(driver)
        
        challenge_one_ten_page.basic_auth()
        challenge_one_ten_page.broken_image()
        challenge_one_ten_page.do_canvas()
        challenge_one_ten_page.doom_challenge()
        challenge_one_ten_page.do_checkbox()
        challenge_one_ten_page.context_menu()
        challenge_one_ten_page.do_disappear_element()
        challenge_one_ten_page.do_drag_and_drop()
        # challenge_one_ten_page.do_dropdown()
    
    def test_challenge_eleven_20(self, setup):
        driver, download_folder = setup
        challenge_eleven_20_page = ChallengeElevenTwentyPage(driver)
        # challenge_eleven_20_page.do_dropdown()
        # challenge_eleven_20_page.do_dynamic_content()
        # challenge_eleven_20_page.do_entry_ad()
        # challenge_eleven_20_page.do_exit_intent()
        # challenge_eleven_20_page.do_file_downloader(download_folder)
        # challenge_eleven_20_page.do_upload_file("2026-10-22-acme-some-file.txt")
        # challenge_eleven_20_page.do_floating_element()
        challenge_eleven_20_page.do_frame()

    def test_challenge_20_30(self, setup):
        driver, download_folder = setup
        challenge_20_30_page = ChallengeTwentyThirtyPage(driver)
        challenge_20_30_page.do_geolocation()