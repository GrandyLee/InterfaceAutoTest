import pytest,allure,xlrd,requests,os
from config import *
from common.utils.getExcelData import *
from common.tools import *
from common.db import *
import dict
from service.login import SSOLogin
import json

@allure.epic("角色管理")
@allure.feature("角色管理")
class TestRole():
    workBook=xlrd.open_workbook(f'{SSOConfig.root_path}/test_case_data/sso/sso_testcase_20210513.xlsx')
    @allure.story("角色列表查询")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"大数据平台系统设置","rolelist"))
    def test_rolelist(self,inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url, headers, method, req_data)
        assert res["code"]==expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("角色详情基本信息")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "rolebasic"))
    def test_rolebasic(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = SSOConfig.headers
        headers['token'] = SSOConfig.sso_token
        headers.update({'Referer': 'http://testhdsp.hikcreate.com/'})
        res = requests.get(url=url, headers=headers, params=req_data)
        res=res.json()
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("角色详情资源信息")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "roleresource"))
    def test_roleresource(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = SSOConfig.headers
        headers['token'] = SSOConfig.sso_token
        headers.update({'Referer': 'http://testhdsp.hikcreate.com/'})
        res = requests.get(url=url, headers=headers, params=req_data)
        res=res.json()
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("角色详情应用信息")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "roleapplist"))
    def test_roleapplist(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = SSOConfig.headers
        headers['token'] = SSOConfig.sso_token
        headers.update({'Referer': 'http://testhdsp.hikcreate.com/'})
        res = requests.get(url=url, headers=headers, params=req_data)
        res = res.json()
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)


    @allure.story("角色详情资源列表")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"大数据平台系统设置","roleresourcelist"))
    def test_roleresourcelist(self,inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url, headers, method, req_data)
        assert res["code"]==expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("角色新增")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"大数据平台系统设置","roleadd"))
    def test_roleadd(self,inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        mysql = MYSQL(*BaseConfig.test_mysql)
        if mysql.ExecuQuery("select * from db_sso.sso_role where name ='我的自动化'"):
            mysql.ExecuNonQuery("delete from db_sso.sso_role where name ='我的自动化'")
        res = request_main(url, headers, method, req_data)
        assert res["code"]==expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("角色修改")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "roleupdate"))
    def test_roleupdata(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("角色删除")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "roledelet"))
    def test_roledelet(self, inData):

        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        req_data1={"manageDeptType":0,"appIds":[],"appId":"1","name":"cs","description":"cs","typeCode":"ceshi110","state":1}
        res1=request_main(url="http://testhdsp.hikcreate.com/web/auth/roles/add", headers=headers, method=method, data=req_data1)
        roleId=res1["data"]["roleId"]
        url = f"{SSOConfig().test_host}{inData['url']}{roleId}"
        res = request_main(url, headers, method,req_data)
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_role.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
    # os.system('allure generate ../../report/tmp –o ../../report/tmp1 –-clean')