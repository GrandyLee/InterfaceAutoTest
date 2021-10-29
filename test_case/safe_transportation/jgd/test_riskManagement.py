# autor: taoke
# time : 2021/8/23 13:46
from config import *
import requests,pytest,allure,xlrd
from common.tools import request_main
from common.utils.getExcelData import get_excelData
from common.db import MYSQL
# class Test_Model():
#     def test_qyd(self):
#         print("测试")
#         """直接拿token"""
#         # bmy_token=SafeTransportationConfig.bmy_token
#         # bmy_headers = {"Content-Type": "application/json",
#         #                "Authorization": bmy_token,
#         #                "appCode": "1422744796822036481"}
#         # res=requests.post("http://testyun.banmago.com/api/tbd/web/baseData/intoVehicle/list",
#         #                   json={"appCode":"1422744796822036481","pageNum":1,"pageSize":10,"useNaturePropertyIds":[]},
#         #                   headers=bmy_headers)
#         # print(res.json())
#
#         """使用公共方法"""
#         res=request_main("http://testyun.banmago.com/api/tbd/web/baseData/intoVehicle/list",
#                          "",
#                          "POST",
#                          {"appCode":"1422744796822036481","pageNum":1,"pageSize":10,"useNaturePropertyIds":[]})
#         print(res)
#
#     def test_jgd(self):
#         print("测试")
#         # """直接拿token"""
#         # sso_token=SafeTransportationConfig.sso_token
#         # headers = {"Content-Type": "application/json",
#         #                "token": sso_token}
#         # res=requests.post("http://testtbdzj.hikcreate.com/web/warnPoint/pageList",
#         #                   json={"pageNum":1,"pageSize":10},
#         #                   headers=headers)
#         # print(res.json())
#
#         """使用公共方法"""
#         res=request_main("http://testtbdzj.hikcreate.com/web/warnPoint/pageList",
#                          "",
#                          "POST",
#                          {"pageNum":1,"pageSize":10})
#         print(res)


@pytest.fixture(scope="class")
def riskPointdelete():
    """删除测试数据"""
    yield
    mysql = MYSQL(*BaseConfig.test_mysql)
    mysql.ExecuNonQuery("delete from db_tbd_base1.risk_info where risk_name like '自动化新增%'")
    mysql.ExecuNonQuery("delete from db_tbd_base1.risk_info_comment where content like '自动化测试%'")


@allure.feature("风险配置")
@allure.description("author:taoke")
@pytest.mark.usefixtures("riskPointdelete")
class TestRiskMan():
    workBook = xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/safe_transportation/jgd_riskCase.xlsx')

    # @pytest.mark.run(order=661)
    @allure.story("风险规则配置")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/73931")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskSave"))
    def test_1riskpointsave(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @pytest.fixture()
    def riskPointID(self):
        """返回新增的测试数据的id"""
        mysql = MYSQL(*BaseConfig.test_mysql)
        info=mysql.ExecuQuery("select id from db_tbd_base1.risk_info where risk_name like '自动化新增%';")
        return info[0]['id']

    @allure.story("风险规则配置") # 编辑
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/73931")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskupdateSave"))
    def test_riskupdateSave(self, inData,riskPointID):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        # 修改请求参数中的风险id
        data["riskPointRequest"]["riskId"] = riskPointID
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("风险规则配置")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/73931")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskList"))
    def test_riskList(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        # 如果通过关键字查询则多个判断
        if inData['frontCondition']=='关键字：自动化':
            assert res['data']['list'][0]['riskName'].__contains__("自动化")
        else:
            assert res['code'] == expectData['code']

    # @pytest.mark.pppp
    @allure.story("风险时间配置")
    @allure.title("{inData[testPoint]}")
    # @allure.testcase("")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskTime"))
    def test_riskTime(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    # @pytest.mark.pppp
    @allure.story("风险基础查询")
    @allure.title("{inData[testPoint]}")
    # @allure.testcase("")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskBase"))
    def test_riskBase(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    # @pytest.mark.pppp
    @allure.story("风险备注配置")
    @allure.title("{inData[testPoint]}")
    # @allure.testcase("")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskComments"))
    def test_riskComments(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("风险备注配置")
    @allure.title("{inData[testPoint]}")
    # @allure.testcase("")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskcommentCreate"))
    def test_riskcommentCreate(self, inData,riskPointID):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        # 请求的风险id修改为新增的风险
        data["parentRiskId"] = riskPointID
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("风险相关")
    @allure.title("{inData[testPoint]}")
    # @allure.testcase("")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskTogeter"))
    def test_riskTogeter(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


@allure.feature("风险结果")
@allure.description("author:taoke")
@pytest.mark.usefixtures("riskPointdelete")
class TestRiskRsu():
    workBook = xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/safe_transportation/jgd_riskCase.xlsx')

    @pytest.mark.pppp
    @allure.story("风险数据分析")
    @allure.title("{inData[testPoint]}")
    # @allure.testcase("")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "风险管理中心", "riskAnalysis"))
    def test_riskAnalysis(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


if __name__ == '__main__':
    for one in os.listdir('../../../report/tmp'):
        if 'json' or 'txt' in one:
            os.remove(f'../../../report/tmp/{one}')
    pytest.main(['test_riskManagement.py', '-s', '--alluredir','../../../report/tmp'])
    # 启动默认浏览器打开报告
    os.system('allure serve ../../../report/tmp')
