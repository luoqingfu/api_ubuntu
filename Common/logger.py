import logging
import os
from datetime import datetime
from Common import readConfig

localReadConfig = readConfig.Presendt_path      #获取配置文件的当前路径
class Logger:
    def __init__(self,log):
        global log_path
        config_path = localReadConfig
        result_path = os.path.join(config_path,"Report")    #结果文件的路径
        if not os.path.exists(result_path):     #判断是否存在这样的路径
            os.mkdir(result_path)               #创建此路径的文件夹
        log_path = os.path.join(result_path,str(datetime.now().strftime("%Y%m%d%H%M")))
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        self.logger  =logging.getLogger(log)       #实例化Logger对象
        self.logger.setLevel(logging.DEBUG)      #设定Logger的等级
        #设置log存放的位置
        headler = logging.FileHandler(os.path.join(log_path,"output.log"),encoding= "UTF-8")
        headler.setLevel(logging.INFO)
        #设置logger的显示格式
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        headler.setFormatter(formatter) #为此处存放的logger设置格式

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        self.logger.addHandler(ch)  # 为此logger设置存放地方
        self.logger.addHandler(headler)  # 为此logger设置存放地方

    def get_logger(self):
        """返回一个装配好的logger实例"""
        return self.logger

    def get_path(self):
        return log_path