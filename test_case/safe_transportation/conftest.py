#作者: taoke
#时间: 2021/5/8 11:43
#编码: -- coding: utf-8 --
#版本: !python3.7
from service.login import *
from config import *
import pytest

@pytest.fixture(scope='module', autouse=True)
def transport_bmy_login():
    """企业端登录获取token"""
    res = BMY().bmy_login(SafeTransportationConfig.test_name_password)
    setattr(SafeTransportationConfig, 'bmy_token', res)


@pytest.fixture(scope='module', autouse=True)
def transport_sso_login():
    """监管端登录获取token"""
    token=Transport_ssoLogin().new_sso_login({"loginName":"taoker","password":"tk123456"},getToken=True)
    setattr(SafeTransportationConfig, 'sso_token', token)


# if __name__ == '__main__':
#     transport_sso_login()
