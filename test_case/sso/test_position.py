from common.utils.getExcelData import get_excelData
import sys,os
import requests,json
import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  *
from service.login import SSOLogin
from common.tools import request_main
from config import *
from common.db import RedisString,MYSQL

class RelayData():
    positionId=''




@allure.epic("岗位管理")
@allure.feature("岗位列表")
class TestPosition():
    workBook = xlrd.open_workbook(f'{SSOConfig.root_path}/test_case_data/sso/sso_testcase_20210513.xlsx')
    def setup_class(self):  # 每一个类下面所有的方法调用只运行一次
        pass
    @allure.story("岗位管理获取列表")
    @allure.title("{inData[testPoint]}")
    @allure.link("http://yapi.hikcreate.com/")
    @allure.description("/web/auth/position/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'大数据平台系统设置', 'position'))
    def test_position_list(self,inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # print(inData['testPoint'])
        """请求"""
        # print("--------------",url, headers, method, req_data)
        res = request_main(url, headers, method, req_data)
        print(res)
        assert res["code"]==expectData["code"]



    @allure.story("岗位管理新增岗位")
    @allure.title("{inData[testPoint]}")
    @allure.link("http://yapi.hikcreate.com/")
    @allure.description("/web/auth/position/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '大数据平台系统设置', 'positionadd'))
    def test_position_add(self,inData):
        # mysql = MYSQL(*BaseConfig.test_mysql)
        # mysql.ExecuNonQuery("DELETE FROM db_sso.sso_position WHERE code='cs001';")  # 删除岗位code为cs001的数据
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # print(inData['testPoint'])
        # print("--------------",url, headers, method, req_data)
        res = request_main(url, headers, method, req_data)
        assert res["code"]==expectData["code"]
        if res["code"]=='200':
            a=res["data"]["positionId"]
            setattr(RelayData, 'positionId', a)
            print(RelayData.positionId)

    @allure.story("岗位管理删除岗位")
    @allure.title("{inData[testPoint]}")
    @allure.link("http://yapi.hikcreate.com/")
    @allure.description("/web/auth/position/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '大数据平台系统设置', 'positiondel'))
    def test_position_del(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']+RelayData.positionId}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        print(RelayData.positionId)
        # print(inData['testPoint'])
        """请求"""
        # print("--------------",url, headers, method, req_data)
        res = request_main(url,headers,method,req_data)
        assert res["code"] == expectData["code"]
    """断言"""

    def teardown_class(self):
        """清除"""


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_position.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
    # os.system('allure generate ../../report/tmp –o ../../report/tmp1 –-clean')
