import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from common.db import RedisString, MYSQL
from config import BmyomsConfig
from service.login import BMY


@pytest.fixture(scope='function')
def application_del():  # 删除应用
    # mysql=BaseConfig.test_mysql_215
    # mysql = MYSQL(*mysql)
    mysql = MYSQL(host="10.197.236.190", port=3306, user="root", pwd="123456", db="hzcp")
    # mysql = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")
    mysql.ExecuNonQuery(
        "DELETE FROM hzcp.application_info WHERE name ='卖保险的文子';")  # 删除应用
    # RedisString(0).delete_key("bmc:c1:dl_img:uid") # 清除 Redis缓存
    yield

@pytest.fixture(scope='function')
def applicationa_del():  # 删除应用
    # mysql=BaseConfig.test_mysql_215
    # mysql = MYSQL(*mysql)
    mysql = MYSQL(host="10.197.236.190", port=3306, user="root", pwd="123456", db="hzcp")
    # mysql = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")
    mysql.ExecuNonQuery(
        "DELETE FROM hzcp.application_info WHERE name ='网约车app';")  # 删除应用
    # RedisString(0).delete_key("bmc:c1:dl_img:uid") # 清除 Redis缓存
    yield

@pytest.fixture(scope='function')
def applicationcopy_del():  # 删除应用
    # mysql=BaseConfig.test_mysql_215
    # mysql = MYSQL(*mysql)
    mysql = MYSQL(host="10.197.236.190", port=3306, user="root", pwd="123456", db="hzcp")
    # mysql = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")
    mysql.ExecuNonQuery(
        "DELETE FROM hzcp.application_info WHERE name='复制 卖保险的文子';")  # 删除复制的应用
    yield

#@allure.epic("斑马企业云oms")
@allure.feature("应用管理")
class TestApplicationManagement():
    workBook = xlrd.open_workbook(f'{BmyomsConfig.root_path}/test_case_data/bmy/bmy_oms_ApplicationManagement_20210806.xlsx')

    @allure.story("查询应用")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/364/interface/api/83400")
    @allure.description("查询应用信息")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '应用管理', 'ApplicationSearch'))
    def test_ApplicationSearch(self, inData):
        url = f"{BmyomsConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @pytest.mark.usefixtures("application_del")
    @allure.story("新增应用")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/364/interface/api/82340")
    @allure.description("新增一个政务应用")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '应用管理', 'ApplicationNew'))
    def test_ApplicationNew(self, inData):
        url = f"{BmyomsConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @pytest.mark.usefixtures("applicationa_del")
    @allure.story("新增应用")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/364/interface/api/82340")
    @allure.description("新增一个app付费应用")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '应用管理', 'ApplicationNewa'))
    def test_ApplicationNewa(self, inData):
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
    @allure.testcase("http://yapi.hikcreate.com/project/364/interface/api/82336")
    @allure.description("操作一个应用")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '应用管理', 'ApplicationOperation'))
    def test_ApplicationOperation(self, inData):
        url = f"{BmyomsConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        if data['id'] == '123':
            idlist = []
            mysql = MYSQL(host="10.197.236.190", port=3306, user="root", pwd="123456", db="hzcp")
            # mysql = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")
            idlist = mysql.ExecuQuery(
                "SELECT id FROM hzcp.application_info where name='卖保险的文子';")
            data = idlist[0]
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @pytest.mark.usefixtures("applicationcopy_del")
    @allure.story("复制应用")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/364/interface/api/82332")
    @allure.description("复制一个应用")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '应用管理', 'ApplicationCopy'))
    def test_ApplicationCopy(self, inData):
        url = f"{BmyomsConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        if data['id'] == '123':
            idlist = []
            mysql = MYSQL(host="10.197.236.190", port=3306, user="root", pwd="123456", db="hzcp")
            # mysql = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")
            idlist = mysql.ExecuQuery(
                "SELECT id FROM hzcp.application_info where name='卖保险的文子';")
            data = idlist[0]
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

if __name__ == '__main__':

    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_ApplicationManagement.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')

    # print(1)
