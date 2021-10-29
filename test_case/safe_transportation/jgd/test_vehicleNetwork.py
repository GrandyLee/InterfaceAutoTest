#__author__:hanxiaojuan
#__time__:2021/8/26
import allure
import pytest
import xlrd

from common.tools import request_main
from common.utils.getExcelData import get_excelData
from config import *


@allure.feature("车辆风险监测")
class TestHiddenDanger():
    workBook = xlrd.open_workbook(f"{BaseConfig().root_path}/test_case_data/safe_transportation/jgd_vehicleNetwork.xlsx")


    @allure.story("高发风险车辆排名")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/78216")
    @allure.description("/vehicle/network/overview/highRiskRank")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"车辆风险监测","vehicleNetworkRisk"))
    def test_vehicleNetworkRisk(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("城市在线车辆数")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/74926")
    @allure.description("/vehicle/network/overview/onlineNumOfCity")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "车辆风险监测", "vehicleNetworkOnlineNumOfCity"))
    def test_vehicleNetworkOnlineNumOfCity(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("车辆分布信息")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/71596")
    @allure.description("/vehicle/network/info/vehicleMap")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "车辆风险监测", "vehicleNetworkMap"))
    def test_vehicleNetworkMap(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("车辆在线指标")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/78212")
    @allure.description("/vehicle/network/overview/onlineState")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "车辆风险监测", "vehicleNetworkOnlineState"))
    def test_vehicleNetworkOnlineState(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("车辆状态指标")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/78214")
    @allure.description("/vehicle/network/overview/riskState")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "车辆风险监测", "vehicleNetworkRiskState"))
    def test_vehicleNetworkRiskState(self, inData):
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
    pytest.main(['test_vehicleNetwork.py', '-s', '--alluredir', '../../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../../report/tmp')