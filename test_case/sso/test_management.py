import pytest,allure,xlrd,requests,os
from config import *
from common.utils.getExcelData import *
from common.tools import *
from common.db import *
import dict
from service.login import SSOLogin
import json


@allure.epic("组织部门")
@allure.feature("组织部门")
class TestManagement():
    workBook = xlrd.open_workbook(f'{SSOConfig.root_path}/test_case_data/sso/sso_testcase_20210513.xlsx')

    @allure.story("组织部门管理")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "management"))
    def test_management(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("组织部门管理")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "managementadd"))
    def test_managementadd(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        mysql = MYSQL(*BaseConfig.test_mysql)
        if mysql.ExecuQuery("select * from db_sso.sso_organization where name ='新增测试'"):
            mysql.ExecuNonQuery("delete from db_sso.sso_organization where name ='新增测试'")
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("组织部门管理")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "managementadd"))
    def test_managementadd(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        mysql = MYSQL(*BaseConfig.test_mysql)
        if mysql.ExecuQuery("select * from db_sso.sso_organization where name ='新增测试'"):
            mysql.ExecuNonQuery("delete from db_sso.sso_organization where name ='新增测试'")
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)

    @allure.story("组织部门管理")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/roles")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "managementdelete"))
    def test_managementdelete(self, inData):
        url = f"{SSOConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        mysql = MYSQL(*BaseConfig.test_mysql)
        if mysql.ExecuQuery("select * from db_sso.sso_organization where id ='1436253704467849218'"):
            pass
        else:
            mysql.ExecuNonQuery("INSERT INTO db_sso.sso_organization(id, parent_id, code, name, `type`, state, abbr,"
                                " sort, area_code, ref_id, desn, chairman, gmt_create, gmt_modified, latitude,"
                                " longitude)VALUES(1436253704467849218, 1310065723170701313, '123114', '删除测试',"
                                " 1, 1, NULL, 88, 110111, NULL, NULL, NULL, '2021-09-10 17:02:22', "
                                "'2021-09-10 17:02:22', NULL, NULL);")
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
