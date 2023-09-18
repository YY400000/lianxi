# -*- coding: utf-8 -*-
import time
import requests
import pytest
from utils.read_data import read_hero
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.read_data import read_yaml


def test_1():
    name = 'yy'
    assert name == 'yy'


def test_2():
    num = 10
    assert num == 10


class TestCase:
    def test_3(self):
        assert 3 == 3

    def test_4(self):
        assert 4 == 4


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get('https://www.baidu.com/')
    return driver


def test_baidu(driver):
    title = driver.title
    url = driver.current_url
    text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://tieba.baidu.com/"]').text
    button_text = driver.find_element(By.ID, 'su').accessible_name
    assert title == '百度一下，你就知道'
    assert url == 'https://www.baidu.com/'
    assert text == '贴吧'
    assert button_text == '百度一下'


class TestBaidu:

    def test_baidu1(self, driver):
        driver.get('https://www.baidu.com/')
        title = driver.title
        url = driver.current_url
        assert title == '百度一下，你就知道'
        assert url == 'https://www.baidu.com/'

    def test_baidu2(self, driver):
        driver.get('https://www.baidu.com/')
        text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://tieba.baidu.com/"]').text
        button_text = driver.find_element(By.ID, 'su').accessible_name
        assert text == '贴吧'
        assert button_text == '百度一下'


class TestBaiduYY:

    def test_baidu3(self, driver):
        driver.get('https://www.baidu.com/')
        title = driver.title
        url = driver.current_url
        text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://tieba.baidu.com/"]').text
        button_text = driver.find_element(By.ID, 'su').accessible_name
        assert title == '百度一下，你就知道'
        assert url == 'https://www.baidu.com/'
        assert text == '贴吧'
        assert button_text == '百度一下'


# 测试数据未分离时
@pytest.mark.parametrize('key1', ['接口自动化1', 'UI自动化1', '性能测试1'])
@pytest.mark.parametrize('key2', ['接口自动化2', 'UI自动化2', '性能测试2'])
def test_baidu(driver, key1, key2):
    print(key1, key2)
    driver.find_element(By.ID, 'kw').send_keys(key1, key2)
    driver.find_element(By.ID, 'su').click()
    driver.find_element(By.ID, 'kw').clear()
    time.sleep(0.1)


@pytest.mark.parametrize('username,password', [['admin', '123456'], ('test01', '123456')])
def test_login(driver, username, password):
    driver.get('http://sellshop.5istudy.online/sell/user/login_page')
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#login > form > p.login.button > input[type=submit]').click()
    time.sleep(1)


# 测试数据分离
@pytest.mark.parametrize('key',read_yaml()['skill'])
def test_baidu(driver, key):
    driver.get('https://www.baidu.com/')
    driver.find_element(By.ID, 'kw').send_keys(key)
    driver.find_element(By.ID, 'su').click()
    time.sleep(1)


@pytest.mark.parametrize('config_data', read_yaml()['userinfos'])
def test_login(driver, config_data):
    driver.get('http://sellshop.5istudy.online/sell/user/login_page')
    driver.find_element(By.ID, 'username').send_keys(config_data['username'])
    driver.find_element(By.ID, 'password').send_keys(config_data['password'])
    driver.find_element(By.CSS_SELECTOR, '#login > form > p.login.button > input[type=submit]').click()
    time.sleep(1)


@pytest.mark.parametrize('username, password', read_yaml()['userinfo_list'])
def test_login(driver, username, password):
    driver.get('http://sellshop.5istudy.online/sell/user/login_page')
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#login > form > p.login.button > input[type=submit]').click()
    if username == 'admin':
        text = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > div > strong').text
        assert text == '用户不存在'
    time.sleep(1)


# 接口自动化
def test_one():
    expect = 1
    actual = 1
    assert expect == actual


def test_two():
    expect = 1
    actual = 1
    assert expect == actual


def test_mobile():
    url = 'http://sellshop.5istudy.online/sell/shouji/query'
    params = {"shouji": '13456755448', 'appkey': '0c818521d38759e1'}
    r = requests.get(url=url, params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['shouji'] == '13456755448'
    assert result['result']['province'] == '北京'
    assert result['result']['city'] == '北京'
    assert result['result']['company'] == '中国移动'
    assert result['result']['areacode'] == '0571'


def test_mobile_post():
    url = 'http://sellshop.5istudy.online/sell/shouji/query'
    params = {
        "shouji": '13456755448',
        'appkey': '0c818521d38759e1'
    }
    r = requests.post(url=url, params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['shouji'] == '13456755448'
    assert result['result']['province'] == '北京'
    assert result['result']['city'] == '北京'
    assert result['result']['company'] == '中国移动'
    assert result['result']['areacode'] == '0571'


# 前置步骤和后置处理
def setup_function():
    print('函数准备测试数据')


def teardown_function():
    print('函数清理测试数据')


@pytest.fixture(scope='module', autouse=True)
# @pytest.fixture()
def fixture4():
    print('我是前置步骤范围为模块')


class TestMobile:
    @staticmethod
    def setup_class():
        print('class准备测试数据')

    @staticmethod
    def teardown_class():
        print('class清理测试数据')

    def test_mobile(self):
        url = 'http://sellshop.5istudy.online/sell/shouji/query'
        params = {"shouji": '13456755448', 'appkey': '0c818521d38759e1'}
        r = requests.get(url=url, params=params)
        assert r.status_code == 200
        result = r.json()
        assert result['status'] == 0
        assert result['msg'] == 'ok'
        assert result['result']['shouji'] == '13456755448'
        assert result['result']['province'] == '北京'
        assert result['result']['city'] == '北京'
        assert result['result']['company'] == '中国移动'
        assert result['result']['areacode'] == '0571'

    def test_mobile_post(self):
        url = 'http://sellshop.5istudy.online/sell/shouji/query'
        params = {
            "shouji": '13456755448',
            'appkey': '0c818521d38759e1'
        }
        r = requests.post(url=url, params=params)
        assert r.status_code == 200
        result = r.json()
        assert result['status'] == 0
        assert result['msg'] == 'ok'
        assert result['result']['shouji'] == '13456755448'
        assert result['result']['province'] == '北京'
        assert result['result']['city'] == '北京'
        assert result['result']['company'] == '中国移动'
        assert result['result']['areacode'] == '0571'


# 接口测试参数化
@pytest.mark.parametrize('shouji,appkey', read_hero()['mobile_params'])
def test_mobile_post(shouji, appkey):
    print('测试手机归属地post请求')
    url = 'http://sellshop.5istudy.online/sell/shouji/query'
    params = {
        "shouji": shouji,
        'appkey': appkey
    }
    r = requests.post(url=url, params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == 'ok'
    assert result['result']['shouji'] == '13456755448'
    assert result['result']['province'] == '北京'
    assert result['result']['city'] == '北京'
    assert result['result']['company'] == '中国移动'
    assert result['result']['areacode'] == '0571'


if __name__ == '__main__':
    pytest.main()
