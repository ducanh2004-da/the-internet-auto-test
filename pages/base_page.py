from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common import actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import Logger
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = Logger()
    
    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)
    
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.logger.info("Clicking on element")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self.logger.info("Element clicked")

    def is_element_present(self, locator):
        elements = self.find_elements(locator)
        return len(elements) > 0

    def enter_text(self, locator, text):
        self.logger.info("Entering text")
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def clear_text(self, locator):
        self.logger.info("Clearing text")
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        self.logger.info("Text cleared")

    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.logger.info(f"Getting text: {element.text}")
        return element.text

    def is_element_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()
    
    def is_element_invisible(self, locator):
        try:
            # invisibility_of_element_located tự động trả về True nếu element ẩn hoặc không tồn tại trong DOM
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element.is_enabled()

    def click_at_coordinate(self, locator, x, y):
        self.logger.info("Clicking at coordinate")
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element_with_offset(element, x, y).click().perform()
        self.logger.info("Element clicked at coordinate")

    def right_click(self, locator):
        self.logger.info("Right clicking on element")
        element = self.wait.until(EC.presence_of_element_located(locator))
        action = ActionChains(self.driver)
        action.context_click(element).perform()
        self.logger.info("Element right clicked")
    
    def accept_alert(self):
        self.logger.info("Accepting alert")
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        self.logger.info("Alert accepted")

    def dismiss_alert(self):
        self.logger.info("Dismissing alert")
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()
        self.logger.info("Alert dismissed")

    def get_alert_text(self):
        self.logger.info("Getting alert text")
        alert = self.wait.until(EC.alert_is_present())
        self.logger.info(f"Alert text: {alert.text}")
        return alert.text
    
    def enter_text_alert(self, text):
        self.logger.info("Entering text to alert")
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)
        self.logger.info("Text entered to alert")

    def click_and_type(self, locator, text):
        self.logger.info("Clicking and typing")
        element = self.wait.until(EC.presence_of_element_located(locator))
        action = ActionChains(self.driver)
        action.click(element).send_keys(text).send_keys(Keys.ENTER).perform()
        self.logger.info("Element clicked and typed")
    
    def drag_and_drop(self, source_locator, target_locator):
        self.logger.info("Dragging and dropping element")
        source = self.wait.until(EC.presence_of_element_located(source_locator))
        target = self.wait.until(EC.presence_of_element_located(target_locator))
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
        self.logger.info("Element dragged and dropped")

    def execuate_script(self, script):
        self.logger.info("Executing script")
        self.driver.execute_script(script)
        self.logger.info("Script executed")

    def switch_frame(self, frame_locator):
        self.logger.info("Switching to frame")
        frame = self.find_element(frame_locator)
        self.driver.switch_to.frame(frame)
        self.logger.info("Frame switched")

    def switch_frame_by_name(self, frame_name):
        self.logger.info("Switching to frame by name")
        self.driver.switch_to.frame(frame_name)
        self.logger.info("Frame switched by name")

    def switch_frame_by_index(self, frame_index):
        self.logger.info("Switching to frame by index")
        self.driver.switch_to.frame(frame_index)
        self.logger.info("Frame switched by index")

    def switch_parent_frame(self):
        self.logger.info("Switching to parent frame")
        self.driver.switch_to.parent_frame()
        self.logger.info("Parent frame switched")
    
    def switch_default_content(self):
        self.logger.info("Switch to default content")
        self.driver.switch_to.default_content()

    def switch_new_window(self):
        self.logger.info("Switching to new window")
        all_windows = self.driver.window_handles
        new_window = all_windows[-1]
        self.driver.switch_to.window(new_window)
        self.logger.info("Switched to new window")

    def back_to_origin_window(self):
        self.logger.info("Back to origin window")
        all_windows = self.driver.window_handles
        origin_window = all_windows[0]
        self.driver.switch_to.window(origin_window)
        self.logger.info("Back to origin window")
    
    def get_location(self, locator):
        element = self.find_element(locator)
        return element.location
    
    def get_size(self, locator):
        element = self.find_element(locator)
        return element.size
