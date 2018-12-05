from Common import readConfig
from Common.configHttp import ConfigHttp
from Common.logger import Logger

url = '/api/account/login'
target = readConfig.readConfig().get_user('target')
password = readConfig.readConfig().get_user('password')
device_type = 'web'
target_type = '1'
data = {'device_type': device_type, 'target_type': target_type,
        'target': target, 'password': password}
request = ConfigHttp()
log_token = Logger('lonin_token').get_logger()
def login():
    request.set_url(url)
    request.set_data(data)
    response = request.post()
    response = response.json()
    if response['code']==1:
        token = response['data']['token']
        log_token.info("token值：{}".format(token))
        return token
    else:
        log_token.info('登录失败：{}'.format(response))
if __name__ == '__main__':
    token = login()