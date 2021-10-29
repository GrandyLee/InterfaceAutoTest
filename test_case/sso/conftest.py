#  作者: liangyan
#  时间: 2021/8/25 11:43
#  编码: -- coding: utf-8 --
#  版本: !python3.7

from service.login import SSOLogin
from config import SSOConfig
import pytest


@pytest.fixture(scope='module', autouse=True)
def test_sso_login_fixture():
    """sso登录获取token"""
    url = SSOConfig.sso_url
    headers = SSOConfig.headers
    res = SSOLogin().sso_login(url=url, method='post', headers=headers)
    setattr(SSOConfig, 'sso_token', res)
    headers['token'] = SSOConfig.sso_token



