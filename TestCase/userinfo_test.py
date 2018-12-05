import unittest

from Common.configHttp import ConfigHttp
from Common.logger import Logger
from TestCase.login.getkey import login
logger = Logger('TestUserInfo').get_logger()
class TestUserInfo(unittest.TestCase):
    def setUp(self):
        self.base_url = '/api/user/getUserInfo'
        self.token = login()
        self.request = ConfigHttp()
        self.request.set_headers(self.token)
        self.data = {'device_type': 'web', 'token': self.token}
        self.AssertionError = []
    def tearDown(self):
        self.assertEqual([], self.AssertionError)
    def test_userinfo(self):
        self.request.set_url(self.base_url)
        self.request.set_data(self.data)
        response = self.request.post()
        json = response.json()
        print(json)