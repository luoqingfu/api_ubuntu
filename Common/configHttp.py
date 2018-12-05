

import requests
import readConfig
from Common.logger import Logger

logger  = Logger("ConfigHttp").get_logger()
localReadConfig = readConfig.readConfig()  #读取配置文件的路径
class ConfigHttp:
    """对HTTP请求的的配置与调用"""
    def __init__(self):
        global scheme ,host ,prot ,timeout
        scheme = localReadConfig.get_http("scheme")
        host = localReadConfig.get_http("baseurl")
        prot = localReadConfig.get_http("prot")
        timeout = localReadConfig.get_http("timeout")
        self.headers = {}
        self.data = {}
        self.url = None
        self.params = {}
    #给请求传入URL参数
    def set_url(self,url):
        self.url = scheme +"://"+ host + url
        logger.info("请求URL：{}".format(self.url))

    # 给请求传入headers参数
    def set_headers(self,headers):
        self.headers.setdefault("Authorization","JWT "+headers)
        logger.info("请求headers：{}".format(self.headers))

    ##给post请求传入数据参数
    def set_data(self,data):
        self.data = data
        logger.info("请求data：{}".format(self.data))

    #给get请求传入数据参数
    def set_params(self,params):
        self.params = params
        logger.info("请求params：{}".format(self.params))

    #调用get请求
    def get(self):
        logger.info("请求类型为：get")
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            return response
        except TimeoutError:
            logger.error("Time out!")
            return None

    #调用post请求
    def post(self):
        logger.info("请求类型为：post")
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data,
                                     timeout=float(timeout))
            return response
        except TimeoutError:
            logger.error("Time out!")
            return None

    # 调用put请求
    def put(self):
        logger.info("请求类型为：put")
        try:
            response = requests.put(self.url, headers=self.headers,  json=self.data,
                                    timeout=float(timeout))
            return response
        except TimeoutError:
            logger.error("Time out!")
            return None

    # 调用deleter请求
    def deleter(self):
        try:
            logger.info("请求类型为：deleter")
            response = requests.delete(self.url, headers=self.headers, json=self.data,
                                    timeout=float(timeout))
            return response
        except TimeoutError:
            logger.error("Time out!")
            return None

    # 调用patch请求
    def patch(self):
        try:
            logger.info("请求类型为：patch")
            response = requests.patch(self.url, headers=self.headers, data=self.data,
                                    timeout=float(timeout))
            return response
        except TimeoutError:
            logger.error("Time out!")
            return None

    #调用请求，传入不同的参数获取不同的请求调用
    def request(self,type):
        if type == "get":
            return  self.get()
        elif   type == "post":
            return  self.post()
        elif   type == "put":
            return  self.put()
        elif   type == "deleter":
            return  self.deleter()
        elif   type == "patch":
            return  self.patch()
        else:
            logger.error("request的类型参数不正确！")
