import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from common.db import RedisString, MYSQL
from config import BmyomsConfig
from service.login import BMY


#@allure.epic("斑马企业云oms")
@allure.feature("应用权限")
class TestApplicationPermissions():
    workBook = xlrd.open_workbook(f'{BmyomsConfig.root_path}/test_case_data/bmy/bmy_oms_Application_permissions_20210818.xlsx')

    @allure.story("查询开通了该应用的企业")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/364/interface/api/84796")
    @allure.description("查询应用信息")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '应用权限', 'ApppermissionsSearch'))
    def test_ApppermissionsSearch(self, inData):
        url = f"{BmyomsConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("操作应用")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/364/interface/api/84740")
    @allure.description("禁用某个企业的某个应用")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '应用权限', 'ApppermissionsDisable'))
    def test_ApppermissionsDisable(self, inData):
        url = f"{BmyomsConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        if data['ids'] == ["000"]:
            idlist = []
            idrlist = []
            mysql = MYSQL(host="10.197.236.190", port=3306, user="root", pwd="123456", db="hzcp")
            # mysql = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")
            idlist = mysql.ExecuQuery(
                "SELECT id FROM hzcp.application_open_apply where contact_phone=18888888889 ORDER BY id DESC LIMIT 1;")
            idrlist.append(idlist[0]['id'])
            data['ids'] = idrlist
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("操作记录")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("")
    @allure.description("查询某个企业的某个应用的操作记录")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '应用权限', 'ApppermissionsOperation'))
    def test_ApppermissionsOperation(self, inData):
        url = f"{BmyomsConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        if data['applyId'] == "000":
            idlist = []
            mysql = MYSQL(host="10.197.236.190", port=3306, user="root", pwd="123456", db="hzcp")
            # mysql = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")
            idlist = mysql.ExecuQuery(
                "SELECT id FROM hzcp.application_open_apply where contact_phone=18888888889 ORDER BY id DESC LIMIT 1;")
            data['applyId'] = idlist[0]['id']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

if __name__ == '__main__':

    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_Application_permissions.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')

    # print(1)
