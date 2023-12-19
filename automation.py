from operation import Operation


class TestAutomation:
    def setup(self):
        self.operation = Operation()
        # 打开app并且不清空用户信息
        self.operation.open_android_app(app_package="com.tencent.wework", app_activity=".launch.LaunchSplashActivity",
                                        no_reset=True)

    def teardown(self):
        self.operation.quit_driver()

    def test_add_user(self):
        self.operation.inter_address_book()
        self.operation.add_a_member_manually("test member", "15804404801")
