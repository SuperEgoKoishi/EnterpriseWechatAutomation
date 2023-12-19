"""
实现企业微信的各种操作
"""
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
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.driver.implicitly_wait(5)

    def inter_address_book(self):
        """
        实现进入通讯录的操作
        :return: 无
        """
        address_book_tab = self.driver.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@resource-id="com.tencent.wework:id/gvq" and @text="Contacts"]')
        address_book_tab.click()

    def add_a_member_manually(self, name, mobile):
        """
        实现手动添加一个成员
        :param name: 成员名字
        :param mobile: 成员的手机号码
        :return: 无
        """
        add_bottom = self.driver.find_element(by=AppiumBy.XPATH,
                                              value='//android.widget.TextView[@resource-id="com.tencent.wework:id/mid1Txt" and @text="Add Member"]')
        add_bottom.click()
        add_manually_bottom = self.driver.find_element(by=AppiumBy.XPATH,
                                                       value='//android.widget.TextView[@text="Add Manually"]')
        add_manually_bottom.click()
        name_box = self.driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.EditText[@resource-id="com.tencent.wework:id/c68"]')
        name_box.send_keys(name)
        mobile_box = self.driver.find_element(by=AppiumBy.XPATH,
                                              value='//android.widget.EditText[@resource-id="com.tencent.wework:id/inm"]')
        mobile_box.send_keys(mobile)
        save_bottom = self.driver.find_element(by=AppiumBy.XPATH,
                                               value='//android.widget.TextView[@resource-id="com.tencent.wework:id/b45"]')
        save_bottom.click()

    def assert_information(self):
        try:
            self.driver.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.LinearLayout[@resource-id="com.tencent.wework:id/csy"]')
        except Exception:
            return
        note = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="com.tencent.wework:id/ct4"]')
        assert "mobile number" in note.text
        assert "name" in note.text

    def quit_driver(self):
            """
            实现关闭driver
            :return: 无
            """
            self.driver.quit()
