#coding:utf-8
import os

class BaseConfig():
    """基础配置类"""
    # 请求头
    headers = {'Content-Type': 'application/json'}
    # 当前运行的产品名 #auto
    current_name = "sso"
    test_case_dir = "test_case/"

    secs = 0.1                    # 测试用例间隔运行时间
    test_redis = {"host": "10.197.236.197", "port": 6379, "password": "123456"}
    root_path = os.path.abspath(os.path.dirname(__file__))          # 项目根目录

    # 钉钉相关
    webhook = ''
    # 斑马信用钉钉群
    bmc_group = [{"secret": "SECd10e7eaf4ae5e4a9b15cb059951519c0d8537721fd588e38b861c411ce6442d3",
                  "webhook": "https://oapi.dingtalk.com/robot/send?access_token=9755709d67e98f6adfa09c884b2b62480b5315ffb65acde5309094206374e3a1",
                  "group": "斑马信用测试"},
                 {"secret": "SEC7714672a0be0239dbff12083d6beca3961490f1f5384c616ea259015d7e71cd1",
                  "webhook": "https://oapi.dingtalk.com/robot/send?access_token=10baf66992f12849793666ee882569bf50d313e9c070ab1afbff25cb9ffcd567",
                  "group": "测试序列"}
                 ]
    # 交委钉钉群
    bmy_group =[{"secret":"SEC40a1be4bbd9214e16ba288208fd608b2b590e82e853fa9b24c1850a506c6185b",
                "webhook":"https://oapi.dingtalk.com/robot/send?access_token=e830b05eeee88da31972099e403a74d05ec55719360707dc44e532c0d0b49cb6",
                "group":"自动化测试组 - 技术和思路分享"},
                {"secret": "SEC7714672a0be0239dbff12083d6beca3961490f1f5384c616ea259015d7e71cd1",
                 "webhook": "https://oapi.dingtalk.com/robot/send?access_token=10baf66992f12849793666ee882569bf50d313e9c070ab1afbff25cb9ffcd567",
                 "group": "测试序列"}
                ]

    # 日志相关
    log_path = r''  # 日志路径

    # 数据库
    test_mysql_215 = ("10.197.236.215", 3306, "root", "DataCenter@!hik", "")
    # edl_private 、edl_public 、hik_trade 、 db_base_service
    test_mysql = ("10.197.236.190", 3306, "root", "123456", "")
    test_mysql_232 = ("10.197.236.190", 3306, "root", "123456", "")


class BMCConfig(BaseConfig):
    """斑马信用app的配置类"""
    # 测试用例目录
    name = "bmc"
    test_case_dir = "test_case/bmc/"
    test_case_data_dir = "test_case_data/bmc/"
    bmcphone = "17822000000"  # 已激活已有车
    Registerphone = "17822220000"   # 未注册用户
    NoactivePhone = "17811000000 "  # 未激活用户
    encodedGesture = "67e6d10010533eed4bbe9659863bf6ee"
    bmc_login_url = "http://testbmcapp.hikcreate.com/v1/user/login/gesture"
    bmc_token = ""  # 公网加密token
    bmc_pvt_token = ""  # 专网token
    host = "http://testbmcapp.hikcreate.com"  # bmc业务所有URL的host
    pvthost = "http://testbmcpvtapp.hikcreate.com"
    # bmc除登录外所有的header
    headers = {
        'City-Code': "520100",
        'Device-Brand': "vivo",
        'Device-Code': "000000001e167ed7000000001e167ed7",
        'Device-Model': "vivo vivo X20",
        'Device-Name': "vivo+X20",
        'Device-Type': "Android",
        'Mac': "38:6E:A2:A0:0E:AF",
        'mimeType': "application/json",
        'Net': "wifi",
        'OS-Type': "Android",
        'OS-Version': "27",
        'Pvt-Token': f"{bmc_pvt_token}",
        'Resolution': "2034x1080",
        'Token': f"{bmc_token}",
        'Version': "2.2.6"
    }
    # 注册和注销专用账号
    loginheader = {
        'City-Code': "520100",
        'Device-Brand': "vivo",
        'Device-Code': "000000001e167ed7000000001e167ed7",
        'Device-Model': "vivo vivo X20",
        'Device-Name': "vivo+X20",
        'Device-Type': "Android",
        'Mac': "38:6E:A2:A0:0E:AF",
        'mimeType': "application/json",
        'Net': "wifi",
        'OS-Type': "Android",
        'OS-Version': "27",
        'Resolution': "2034x1080",
        'Version': "2.2.6"
    }
    logoutheader = {
        'City-Code': "520100",
        'Device-Brand': "vivo",
        'Device-Code': "000000001e167ed7000000001e167ed7",
        'Device-Model': "vivo vivo X20",
        'Device-Name': "vivo+X20",
        'Device-Type': "Android",
        'Mac': "38:6E:A2:A0:0E:AF",
        'mimeType': "application/json",
        'Net': "wifi",
        'OS-Type': "Android",
        'OS-Version': "27",
        'Resolution': "2034x1080",
        'Token': bmc_token,
        'Version': "2.2.6"
    }


class BmyConfig(BaseConfig):
    """企业云的配置类"""
    name = "bmy"
    test_case_dir = "test_case/bmy/"
    test_case_data_dir = "test_case_data/bmy/"
    # 获取token和密码加密原始密钥
    key = "Jv+h&c0A"
    # 获取token 原始token
    defaultToken = "Basic aHpjcF93ZWI6MTIzNDU2"
    # 测试环境host
    test_host = "http://testyun.banmago.com/api"
    # 登录账号
    test_name_password = {"username": "15151500000", "password": "bmy123456", "Register-Origin": "yun"}
    # 企业云接口的Authorization
    bmy_token = ''
    headers = {"Content-Type": "application/json"}


class BmyomsConfig(BaseConfig):
    """企业云oms的配置类"""
    name = "bmyoms"
    test_case_dir = "test_case/bmy/"
    test_case_data_dir = "test_case_data/bmy/"
    # 获取token和密码加密原始密钥
    key = "Jv+h&c0A"
    # 获取token 原始token
    defaultToken = "Basic aHpjcF93ZWI6MTIzNDU2"
    # 测试环境host
    test_host = "http://testoms.banmago.com/api"
    # 登录账号
    test_name_password = {"username": "888888", "password": "bmy123456", "grant_type": "intranet"}
    # 企业云接口的Authorization
    bmy_token = ''

    headers = {"Content-Type": "application/json",
               "Authorization": bmy_token}


class SSOConfig(BaseConfig):
    """SSO配置类"""
    name = "sso"
    test_case_dir = "test_case/sso/"
    test_case_data_dir = "test_case_data/sso/"
    sso_username = 'never1'  # SSO登录名
    sso_password = 'ly123456'  # sso密码
    test_host = "http://testhdsp.hikcreate.com"
    sso_url = "http://testhdsp.hikcreate.com/web/auth/users/login"  # sso登录地址
    sso_salt = 'hikcreate_xj'  # SSO盐值
    sso_token = ''
    headers = {'Content-Type': 'application/json'}


class SafeTransportationConfig(BaseConfig):
    """交委安全运输配置类"""
    name = "sTransport"
    test_case_dir = "test_case/safe_transportation/"
    test_case_data_dir = "test_case_data/safe_transportation/"
    # 企业云
    key = "Jv+h&c0A"
    defaultToken = "Basic aHpjcF93ZWI6MTIzNDU2"
    test_host = "http://testyun.banmago.com/api"
    test_name_password = {"username": "15150000000", "password": "A123456", "Register-Origin": "yun"}
    bmy_token = ''
    # headers = {"Content-Type": "application/json",
    #                "Authorization":bmy_token}
    # sso
    sso_username = 'robot_fanxun'  # SSO登录名
    sso_password = 'fx123456'  # sso密码
    sso_url = r'http://testtbdzj.hikcreate.com/web/auth/users/login'  # sso登录地址
    SSO_url =  r'http://testtbdzj.hikcreate.com/web'  #监管端sso
    sso_salt = 'hikcreate_xj'  # SSO盐值
    sso_token = ''
    headers = {'Content-Type': 'application/json',
                 "appCode": "1422744796822036481"}         # 应用code
