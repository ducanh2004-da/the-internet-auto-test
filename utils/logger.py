import logging
from config.env_config import EnvConfig

class Logger:
    def __init__(self):
        self.env_config = EnvConfig("dev")
        
        # 1. Đặt tên riêng cho logger để tránh can thiệp toàn cục vào root logger
        self.logger = logging.getLogger("AutomationTest")
        
        # 2. Lấy log_level an toàn: nếu thiếu key "log_level" trong config thì mặc định lấy "INFO"
        raw_level = self.env_config.config.get("log_level", "INFO")
        
        # Chuyển đổi chuỗi (VD: "DEBUG", "INFO") sang hằng số của module logging
        log_level = getattr(logging, str(raw_level).upper(), logging.INFO)
        self.logger.setLevel(log_level)
        
        # 3. Tránh addHandler lặp lại nhiều lần gây nhân đôi dòng log
        if not self.logger.handlers:
            stream_handler = logging.StreamHandler()
            
            # Định dạng log chuyên nghiệp: Thời gian - Cấp độ - Nội dung
            formatter = logging.Formatter(
                fmt="%(asctime)s [%(levelname)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)
    
    def info(self, message):
        self.logger.info(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def debug(self, message):
        self.logger.debug(message)