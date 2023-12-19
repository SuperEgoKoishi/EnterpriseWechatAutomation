from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy


class Operation:
    def open_android_app(self, automation_name="uiautomator2", app_package=None, app_activity=None, no_reset=False):
        """
        实现打开android app
        :param automation_name: appium dirver名称，默认uiautomator2
        :param app_package: app包名称，默认为空，不打开任何app
        :param app_activity: app状态，默认为空，不打开任何app
        :param no_reset: 是否不清空缓存，默认清空缓存
        :return: 无
        """
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": automation_name,
            "appium:appPackage": app_package,
            "appium:appActivity": app_activity,
            "appium:noReset": no_reset
        })
        super.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        super.driver.implicitly_wait(5)

    def inter_address_book(self, driver):
        """
        实现进入通讯录的操作
        :return: 无
        """

    def quit_driver(self):
        """
        实现关闭driver
        :return: 无
        """
        super.driver.quit()
