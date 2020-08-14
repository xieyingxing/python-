from selenium import webdriver


class DriverUtil:

    driver = None

    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver


    @classmethod
    def close_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
