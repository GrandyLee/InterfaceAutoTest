import pytest, allure, xlrd, requests, os
from config import *
from common.utils.getExcelData import *
from common.tools import *
from common.db import *
import dict
from service.login import SSOLogin


class RelayData():
    userId = ''


@allure.epic("账号管理")
@allure.feature("账号管理")
class TestUsersManage():
    workBook = xlrd.open_workbook(f'{SSOConfig.root_path}/test_case_data/sso/sso_testcase_20210513.xlsx')

    @allure.story("账号查询")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "userlist"))
    def test_userlist(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']

        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]

    @allure.story("账号新增")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "useradd"))
    def test_useradd(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        mysql = MYSQL(*BaseConfig.test_mysql)
        if mysql.ExecuQuery("select * from db_sso.sso_user where login_name ='zidonghua' or real_name ='zidonghua' "):
            mysql.ExecuNonQuery("delete from db_sso.sso_user where login_name ='zidonghua'or real_name='zidonghua'")
        res = request_main(url, headers, method, req_data)
        if res["message"] == '添加用户成功':
            a = res["data"]["userId"]
            setattr(RelayData, 'userId', a)
            print(RelayData.userId)
        assert res["code"] == expectData["code"]

    @allure.story("账号编辑")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "userupdate"))
    def test_userupdate(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]

    @allure.story("查看账号详情")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "userview"))
    def test_userview(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = SSOConfig.headers
        headers['token'] = SSOConfig.sso_token
        headers.update({'Referer': 'http://testhdsp.hikcreate.com/'})
        res = requests.get(url=url, params=req_data, headers=headers)
        res = res.json()
        assert res["code"] == expectData["code"]

    @allure.story("账号删除")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "userdelet"))
    def test_userdelet(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        mysql = MYSQL(*BaseConfig.test_mysql)
        if mysql.ExecuQuery("select * from db_sso.sso_user where login_name ='csyihao' and deleted =1"):
            mysql.ExecuNonQuery("update  db_sso.sso_user set deleted =0 where login_name ='csyihao' ")
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]

    @allure.story("批量应用授权")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "userauthorization"))
    def test_userauthorization(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]

    @allure.story("登录安全设置")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "userexpiration"))
    def test_userexpiration(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]

    @allure.story("批量禁用")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "userchangestate"))
    def test_userchangestate(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url, headers, method, req_data)
        assert res["code"] == expectData["code"]

    @allure.story("账号解锁")
    @allure.title("{inData[testPoint]}")
    @allure.description("/web/auth/users/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "大数据平台系统设置", "userunlock"))
    def test_userunlock(self, inData):
        url = f"{SSOConfig.test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        # req_data=json.dumps(req_data)
        expectData = inData['expectData']
        headers = SSOConfig.headers
        headers['token'] = SSOConfig.sso_token
        headers.update({'Referer': 'http://testhdsp.hikcreate.com/'})
        headers1 = {'Referer': 'http://testhdsp.hikcreate.com/', 'Content-Type': 'application/json'}
        encrypted_password = SSOLogin()._sso_pwd_encrypted('a+b=C1234')
        user = {"loginName": "ziguanli", "password": f"{encrypted_password}"}
        user = json.dumps(user)
        for i in range(5):
            res1 = requests.post(url='http://testhdsp.hikcreate.com/web/auth/users/login', data=user, headers=headers1)
        res = requests.post(url=url, headers=headers, data=req_data)
        res = res.json()
        print(res)
        assert res["code"] == expectData["code"]


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_user.py', '-s', '--alluredir', '../../report/tmp'])
