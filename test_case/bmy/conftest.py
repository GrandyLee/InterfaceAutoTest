#作者: taoke
#时间: 2021/5/8 11:43
#编码: -- coding: utf-8 --
#版本: !python3.7
from service.login import BMY
from config import BmyConfig, BmyomsConfig
import pytest

@pytest.fixture(scope='module', autouse=True)
def bmy_login():
    """BMY登录获取token"""
    res = BMY().bmy_login(BmyConfig.test_name_password)
    setattr(BmyConfig, 'bmy_token', res)

@pytest.fixture(scope='module', autouse=True)
def bmyoms_login():
    """BMYoms登录获取token"""
    res = BMY().bmyoms_login(BmyomsConfig.test_name_password)
    # setattr(object, name, value) object -- 对象。 name -- 字符串，对象属性。value -- 属性值。
    setattr(BmyomsConfig, 'bmy_token', res)  # BmyomsConfig这个类里面的的bmy_token这个变量的值设置为res

    # res= BMY().get_authorization()
    # setattr(BmyConfig, 'bmy_token', res)
