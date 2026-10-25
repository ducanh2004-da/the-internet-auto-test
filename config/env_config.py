class EnvConfig:
    def __init__(self, env):
        self.env = env
        self.config = self.load_config()

    def load_config(self):
        if self.env == "dev":
            return{
                "base_url": "https://the-internet.herokuapp.com",
                "endpoints": {
                    "basic_auth": "/basic_auth",
                    "broken_image": "/broken_images",
                    "canvas": "/canvas",
                    "challenge_DOM": "/challenging_dom",
                    "check_boxes": "/checkboxes",
                    "context_menu": "/context_menu",
                    "disappear_elements": "/disappearing_elements",
                    "drag_drop": "/drag_and_drop",
                    "dropdown": "/dropdown",
                    "dynamic_content": "/dynamic_content",
                    "dynamic_controls": "/dynamic_controls",
                    "dynamic_loading": "/dynamic_loading",
                    "entry_ad": "/entry_ad",
                    "entry_exit": "/entry_exit",
                    "file_download": "/download",
                    "file_upload": "/upload",
                    "floating_menu": "/floating_menu",
                    "i_frame": "/frames",
                    "horizontal_slider": "/horizontal_slider"
                }
            }

        if self.env == "qa":
            return {
                "base_url": "https://the-internet.herokuapp.com/",
                "endpoints": {
                    "basic_auth": "basic_auth",
                    "broken_image": "broken_images",
                    "canvas": "canvas",
                    "challenge_DOM": "challenging_dom",
                    "check_boxes": "checkboxes",
                    "context_menu": "context_menu",
                    "disappear_elements": "disappearing_elements",
                    "drag_drop": "drag_and_drop",
                    "dynamic_content": "dynamic_content",
                    "dynamic_controls": "dynamic_controls",
                    "dynamic_loading": "dynamic_loading",
                    "entry_exit": "entry_exit",
                    "file_download": "download",
                    "file_upload": "upload",
                    "floating_menu": "floating_menu",
                    "i_frame": "frames",
                    "horizontal_slider": "horizontal_slider"
                }
            }