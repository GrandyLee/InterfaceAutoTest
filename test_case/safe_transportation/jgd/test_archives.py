# __author__: hanxiaojuan
# __time__: 2021/8/25

import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import *
from service.login import BMY



@allure.feature("全息档案")
class TestEnterpriseArchives():
    workBook = xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/safe_transportation/jgd_archives.xlsx')

    @allure.story("企业档案列表")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/69879")
    @allure.description("/enterprise-archives/query")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '全息档案', 'enterpriseArchives'))
    def test_enterpriseArchives(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("企业档案详情")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/83952")
    @allure.description("/enterprise-archives/enterpriseArchiveDetail")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","enterpriseArchiveDetail"))
    def test_enterpriseArchiveDetail(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("企业档案运政详情")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/83948")
    @allure.description("/enterprise-archives/yzEnterpriseArchiveDetail")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","enterpriseArchiveDetailYz"))
    def test_enterpriseArchiveDetailYz(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    # @allure.story("企业关联车辆")
    # @allure.title("{inData[testPoint]}")
    # @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/83920")
    # @allure.description("/enterprise-archives/vehicle")
    # @pytest.mark.parametrize("inData", get_excelData(workBook,"全息档案","enterpriseArchivesVehicle"))
    # def test_enterpriseArchivesVehicle(self,inData):
    #     url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
    #     headers = inData['headers']
    #     method = inData['method']
    #     data = inData['reqData']
    #     expectData = inData['expectData']
    #     res = request_main(url, headers, method, data)
    #     allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
    #     assert res['code'] == expectData['code']

    @allure.story("企业关联驾驶人")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/83924")
    @allure.description("/enterprise-archives/driver")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "全息档案", "enterpriseArchivesDriver"))
    def test_enterpriseArchivesDriver(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("关键指标风险明细")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85272")
    @allure.description("/enterprise-archives/keyIndicatorsRiskDetail")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","enterpriseArchiveIndicatorsRisk"))
    def test_enterpriseArchiveIndicatorsRisk(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("关键指标信息")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85321")
    @allure.description("/enterprise-archives/safeProductionStat")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","enterpriseArchiveIndicators"))
    def test_enterpriseArchiveIndicators(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("关键指标变化趋势")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85335")
    @allure.description("/enterprise-archives/keyIndicatorsTimeTrend")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","enterpriseArchiveIndicatorsTrend"))
    def test_enterpriseArchiveIndicatorsTrend(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("关键指标统计报表")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85328")
    @allure.description("/enterprise-archives/keyIndicatorsReport")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","enterpriseArchiveIndicatorsReport"))
    def test_enterpriseArchiveIndicatorsReport(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("关键指标风险详情")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85342")
    @allure.description("/enterprise-archives/riskDetail")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","enterpriseArchiveRisk"))
    def test_enterpriseArchiveRisk(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("获取风险类型")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/67617")
    @allure.description("/dic/getRisk?fromStatPage=true")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","enterpriseArchiveGetRisk"))
    def test_enterpriseArchiveGetRisk(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("驾驶人档案列表")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/69873")
    @allure.description("/driver-archives/query")
    @pytest.mark.parametrize("inData",get_excelData(workBook,"全息档案","driverArchivesQuery"))
    def test_driverArchivesQuery(self,inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}","响应结果",allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("驾驶人档案详情")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85384")
    @allure.description("/drivers/page")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "全息档案", "driverArchivesDrivers"))
    def test_driverArchivesDrivers(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("驾驶人特征")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85307")
    @allure.description("/driver-archives/driverFeatureStat")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "全息档案", "driverArchivesFeature"))
    def test_driverArchivesFeature(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("驾驶人关联车辆")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85314")
    @allure.description("/driver-archives/associatedVehicle")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "全息档案", "driverArchivesAssociatedVehicle"))
    def test_driverArchivesAssociatedVehicle(self, inData):
        url = f"{SafeTransportationConfig().SSO_url}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("驾驶人关联企业")
    @allure.title("inData[testPoint]")
    @allure.testcase("http://yapi.hikcreate.com/project/336/interface/api/85293")
    @allure.description("/vehicle-archives/driverAssociatedEnterprise")
    @pytest.mark.parametrize("inData", get_excelData(workBook, "全息档案", "driverArchivesAssociatedEnterprise"))
    def test_driverArchivesAssociatedEnterprise(self, inData):
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
    pytest.main(['test_archives.py', '-s', '--alluredir', '../../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../../report/tmp')