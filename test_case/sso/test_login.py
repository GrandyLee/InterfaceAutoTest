from common.utils.getExcelData import get_excelData
import sys, os
import requests, json
import pytest, allure, xlrd, requests, os
from common.utils.getExcelData import *
from service.login import *
from common.tools import request_main
from common.db import MYSQL

from config import *
from common.db import RedisString, MYSQL


@allure.epic("登录模块")
@allure.feature("登录")
class TestLogin():
    workBook = xlrd.open_workbook(f'{SSOConfig.root_path}/test_case_data/sso/sso_testcase_20210513.xlsx')
    def setup_class(self):  # 每一个类下面所有的方法调用只运行一次
        pass
    @allure.story("登录测试")
    @allure.title("{inData[testPoint]}")
    @allure.link("http://yapi.hikcreate.com/")
    @allure.description("/web/auth/users/login")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '大数据平台系统设置', 'login'))
    def test_login(self, inData):
        # url = f"{SSOConfig().test_host}{inData['url']}"
        # method = inData['method']
        # req_data = inData['reqData']
        expectData = inData['expectData']
        # headers = inData['headers']
        # # print(inData['testPoint'])
        """请求"""
        # print("-----------0000000000000000---",url, headers, method, req_data)
        mysql = MYSQL(*BaseConfig.test_mysql)
        mysql.ExecuNonQuery("update db_sso.sso_user set sso_user.lock_status =0 where login_name ='never1'")
        RedisString(3).delete_key('sso:user:errorPwd:never1')
        res = SSOLogin().new_ssologin(inData, getToken=False)
        # print('5555555555555555555555555555555',res)
        # print(expectData["code"])
        assert res["code"] == expectData["code"]
    """断言"""

    def teardown_class(self):
        """清除"""


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_login.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
    # os.system('allure generate ../../report/tmp –o ../../report/tmp1 –-clean')
