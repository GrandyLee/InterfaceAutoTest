#__author__:hanxiaojuan
#__time__:2021/8/26
import allure
import pytest
import xlrd

from common.tools import request_main
from common.utils.getExcelData import get_excelData
from config import *


@allure.feature("行业隐患监测")
class TestHiddenDanger():
    workBook = xlrd.open_workbook(f"{BaseConfig().root_path}/test_case_data/safe_transportation/jgd_hiddenDanger.xlsx")


    @allure.story("行业信息列表")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/78268")
    @allure.description("/gov/hiddenDanger/industryInfoList")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"行业隐患监测","hiddenDangerIndustry"))
    def test_hiddenDangerIndustry(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("基础设施")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/78270")
    @allure.description("/gov/hiddenDanger/infrastructureList")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"行业隐患监测","hiddenDangerInfrastructure"))
    def test_hiddenDangerInfrastructure(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("围栏")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/83984")
    @allure.description("/gov/hiddenDanger/getEnclosure")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "行业隐患监测", "hiddenDangerEnclosure"))
    def test_hiddenDangerEnclosure(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("关键指标")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/78264")
    @allure.description("/gov/hiddenDanger/keyIndicator")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "行业隐患监测", "hiddenDangerIndicator"))
    def test_hiddenDangerIndicator(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("车辆隐患列表")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/78284")
    @allure.description("/gov/hiddenDanger/hiddenDangerList")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "行业隐患监测", "hiddenDangerList"))
    def test_hiddenDangerList(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("已管理行业")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/88233")
    #@allure.description()
    @pytest.mark.parametrize("inData", get_excelData(workBook, "行业隐患监测", "industryInitConfig"))
    def test_industryInitConfig(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

if __name__ == '__main__':
    for one in os.listdir('../../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../../report/tmp/{one}')
    pytest.main(['test_hiddenDanger.py', '-s', '--alluredir', '../../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../../report/tmp')