from operation import Operation


class TestAutomation:
    def setup(self):
        self.operation = Operation()
        # 打开app并且不清空用户信息
        self.operation.open_android_app(app_package="com.tencent.wework", app_activity=".launch.LaunchSplashActivity",
                                        no_reset=True)

    def teardown(self):
        self.driver.quit()

    def add_user(self):
        pass
