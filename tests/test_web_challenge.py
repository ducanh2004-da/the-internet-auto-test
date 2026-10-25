from pages.challenge_eleven_20_page import ChallengeElevenTwentyPage
from pages.challenge_one_ten_page import ChallengeOneTenPage

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
        challenge_one_ten_page.do_dropdown()
    
    def test_challenge_eleven_20(self, setup):
        driver = setup
        challenge_eleven_20_page = ChallengeElevenTwentyPage(driver)
        # challenge_eleven_20_page.do_dropdown()
        # challenge_eleven_20_page.do_dynamic_content()
        challenge_eleven_20_page.do_entry_ad()