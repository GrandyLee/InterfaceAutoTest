import pytest,allure,xlrd,requests,os
from config import BmyConfig
from  common.utils.getExcelData import  get_excelData
from common.tools import request_main

# @allure.epic("控制台111")
@allure.feature("控制台")
class Test_console:
    #引用测试用例表单
    workBook = xlrd.open_workbook(f'{BmyConfig.root_path}/test_case_data/bmy/bmy_case.xlsx')

    """接口1"""

    @allure.story("我的应用")       # 接口
    @allure.title("{inData[testPoint]}")       # 测试点
    @pytest.mark.parametrize("inData", get_excelData(workBook, '控制台', 'UserApplication')) #[{},{},{}]
    def test_application(self,inData):
        url=f"{BmyConfig().test_host}{inData['url']}"
        headers=inData['headers']
        method=inData['method']
        data=inData['reqData']
        expectData=inData['expectData']

        res=request_main(url,headers,method,data)
        # print("-------------------",res)
        assert res['code']==expectData['code']

    """接口2"""

    @allure.story("应用中心")  # 接口
    @allure.title("查看应用中心")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '控制台', 'ApplicationCenter'))  # [{},{},{}]
    def test_applicationcenter(self, inData):
        url = f"{BmyConfig().test_host}{inData['url']}"
        headers = inData['headers']
        method = inData['method']
        data = inData['reqData']
        expectData = inData['expectData']

        res = request_main(url, headers, method, data)
        assert res['code'] == expectData['code']


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_console.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')



