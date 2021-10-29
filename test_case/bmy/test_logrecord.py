import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BmyomsConfig
from service.login import BMY


#@allure.epic("斑马企业云oms")
@allure.feature("日志模块")
class TestLogRecord():
    workBook = xlrd.open_workbook(f'{BmyomsConfig.root_path}/test_case_data/bmy/bmy_oms_logging_20210803.xlsx')

    @allure.story("查询日志")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/project/364/interface/api/cat_17412")
    @allure.description("查询日记记录")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '日志', 'logging'))
    def test_logrecord(self, inData):
        url = f"{BmyomsConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url, headers, method, data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']




if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_logrecord.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')


