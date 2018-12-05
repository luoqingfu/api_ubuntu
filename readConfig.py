import os
from configparser import ConfigParser

Presendt_path = os.path.split(os.path.realpath(__file__))[0]        #***获取当前文件所在路径**
config_path = os.path.join(Presendt_path, "config.ini")            #***获取config.ini文件所在路径**
class readConfig:
    """读取配置文件config.ini"""
    def __init__(self):
        # open_config = open(config_path)  #打开配置文件文件
        # config_data = open_config.read() #读取配置文件
        # open_config.close()              #关闭配置文件
        self.parser = ConfigParser()     #实例化配置文件解析器
        self.parser.read(config_path)    #读取配置文件的的数据

    def get_http(self, name):
        """获取http配置文件中的字段值"""
        return self.parser.get("HTTP", name)

    def get_database(self, name):
        """获取database配置文件中的字段值"""
        return self.parser.get("DATABASE", name)

    def get_user(self, name):
        """获取database配置文件中的字段值"""
        return self.parser.get("USER", name)

    def get_config(self, name):
        return self.parser.get('CONFIG', name)

