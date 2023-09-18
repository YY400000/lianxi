# -*- coding: utf-8 -*-


# import time
# import requests
# import pytest
# from utils.read_data import read_hero


# 未学习的内容：代码分层的封装思想（代码不要写在一起），
# 接口层api，把所有的接口请求requests.post()都放到api层。
# 配置中心config，进行域名URL的管理（url=’https://www.baidu.com‘）
# 核心层core，写request的封装，把request不同的请求方式封装到统一的代码里面
# 日志层log，把日志和接口请求进行结合，还有实现日志的打印等
# data.yaml 测试数据分离，定义一些复杂的参数，不同的参数类型等
# 断言

# requests库中的setup/teardown前置和后置步骤
# 方法级 setup_method/teardown_method # 在类中才能使用
# 函数级 setup_function/teardown_function
# 类级 setup_class/teardown_class # 在类中才能使用
# 模块级 setup_module/teardown_module

# Ctrl + Alt + L 可以格式化不规范的书写
# Ctrl + D 复制选定的区域或行到下一行
# Ctrl + Y 删除当前行
# Ctrl + Delete 删除到字符结束
# Ctrl + End/Home 跳转到尾部/头部

# 文件命名规范
# 1、.py测试文件必须以"test_"开头（或"_test"结尾）
# 2、测试方法必须以"test_"开头
# 3、测试类必须以Test开头，并且不能有init方法

# fixture比setup/teardown更灵活，比如5条用例执行前置条件，5条用例不执行前置条件
# fixture夹具，相当于前置步骤，参数scope可以为function、class、module、session 参数autouse为True时每条用例都会自动执行这个前置步骤
# fixture不填参数默认function，每个方法执行一次
# fixture使用时要在函数（）中添加fixture函数的名字
# def test_1():
#     name = 'yy'
#     assert name == 'yy'


# def test_2():
#     num = 10
#     assert num == 10
#
# class TestCase:
#     def test_3(self):
#         assert 3 == 3
#     def test_4(self):
#         assert 4 == 4
#
# import pytest
# if __name__ == '__main__':
#     pytest.main()

# 常见的断言类型
# def test_5():
#     assert 1 == 1
#     assert 1 != 2
#     assert 3 > 1
#     assert 1 < 3
#     assert 3 >= 3
#     assert 3 <= 3
#     assert '百' in '百度一下'
#     assert 'd' not in 'abc'
#     assert True is True
#     assert False is not True

# pytest+selenium实践
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()
# def test_baidu():
#     driver.get('https://www.baidu.com/')
#     title = driver.title
#     url = driver.current_url
#     text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://tieba.baidu.com/"]').text
#     button_text = driver.find_element(By.ID, 'su').accessible_name
#     assert title == '百度一下，你就知道'
#     assert url == 'https://www.baidu.com/'
#     assert text == '贴吧'
#     assert button_text == '百度一下'


# 前置步骤
# @pytest.fixture(scope='function')
# def fixture1():
#     print('我是前置步骤1')
#     return 4
#
# @pytest.fixture(autouse=True)
# def fixture2():
#     print('我是前置步骤2')
#     return 5
#
# def test_fixture1(fixture1,fixture2):
#     assert 1 == 1
#     assert fixture1 == 4
#
# def test_fixture2():
#     assert 2 == 2
#     # assert fixture2 == 5 # 不可用，想要返回值必须在函数参数里面价fixture2
#
# if __name__ == '__main__':
#     pytest.main()


# # 实践
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# @pytest.fixture(scope='module')  # 每个文件（module）只执行一次
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get('https://www.baidu.com/')
#     return driver
#
# class TestBaidu:
#
#     def test_baidu1(self, driver):
#         title = driver.title
#         url = driver.current_url
#         assert title == '百度一下，你就知道'
#         assert url == 'https://www.baidu.com/'
#
#     def test_baidu2(self, driver):
#         text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://tieba.baidu.com/"]').text
#         button_text = driver.find_element(By.ID, 'su').accessible_name
#         assert text == '贴吧'
#         assert button_text == '百度一下'
#
# class TestBaiduYY:
#     def test_baidu3(self, driver):
#         title = driver.title
#         url = driver.current_url
#         text = driver.find_element(By.CSS_SELECTOR, 'a[href="http://tieba.baidu.com/"]').text
#         button_text = driver.find_element(By.ID, 'su').accessible_name
#         assert title == '百度一下，你就知道'
#         assert url == 'https://www.baidu.com/'
#         assert text == '贴吧'
#         assert button_text == '百度一下'
#
# if __name__ == '__main__':
#     pytest.main()


# 测试数据分离
# import pytest
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from utils.read_data import read_yaml
#
#
# @pytest.fixture(scope='module')
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     return driver


# # 测试数据未分离时
# @pytest.mark.parametrize('key1', ['接口自动化1', 'UI自动化1', '性能测试1'])
# @pytest.mark.parametrize('key2', ['接口自动化2', 'UI自动化2', '性能测试2'])
# def test_baidu(driver, key1, key2):
#     print(key1, key2)
#     driver.find_element(By.ID, 'kw').send_keys(key1, key2)
#     driver.find_element(By.ID, 'su').click()
#     driver.find_element(By.ID, 'kw').clear()
#     time.sleep(0.1)

# @pytest.mark.parametrize('username,password', [['admin', '123456'], ('test01', '123456')])
# def test_login(driver, username, password):
#     driver.get('http://sellshop.5istudy.online/sell/user/login_page')
#     driver.find_element(By.ID, 'username').send_keys(username)
#     driver.find_element(By.ID, 'password').send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, '#login > form > p.login.button > input[type=submit]').click()
#     sleep(2)


# 测试数据分离
# @pytest.mark.parametrize('key',read_yaml()['skill'])
# def test_baidu(driver, key):
#     driver.get('https://www.baidu.com/')
#     driver.find_element(By.ID, 'kw').send_keys(key)
#     driver.find_element(By.ID, 'su').click()
#     time.sleep(2)
#
#
# @pytest.mark.parametrize('config_data', read_yaml()['userinfos'])
# def test_login(driver, config_data):
#     driver.get('http://sellshop.5istudy.online/sell/user/login_page')
#     driver.find_element(By.ID, 'username').send_keys(config_data['username'])
#     driver.find_element(By.ID, 'password').send_keys(config_data['password'])
#     driver.find_element(By.CSS_SELECTOR, '#login > form > p.login.button > input[type=submit]').click()
#     sleep(2)
#
#
# @pytest.mark.parametrize('username, password', read_yaml()['userinfo_list'])
# def test_login(driver, username, password):
#     driver.get('http://sellshop.5istudy.online/sell/user/login_page')
#     driver.find_element(By.ID, 'username').send_keys(username)
#     driver.find_element(By.ID, 'password').send_keys(password)
#     driver.find_element(By.CSS_SELECTOR, '#login > form > p.login.button > input[type=submit]').click()
#     if username == 'admin':
#         text = driver.find_element(By.CSS_SELECTOR, 'body > div > div > div > div > strong').text
#         assert text == '用户不存在'
#     sleep(2)


# 接口自动化
# def test_one():
#     expect = 1
#     actual = 1
#     assert expect == actual

# def test_two():
#     expect = 1
#     actual = 2
#     assert expect == actual

# def test_mobile():
#     url = 'http://sellshop.5istudy.online/sell/shouji/query'
#     params = {"shouji": '13456755448', 'appkey': '0c818521d38759e1'}
#     r = requests.get(url=url, params=params)
#     assert r.status_code == 200
#     result = r.json()
#     assert result['status'] == 0
#     assert result['msg'] == 'ok'
#     assert result['result']['shouji'] == '13456755448'
#     assert result['result']['province'] == '北京'
#     assert result['result']['city'] == '北京'
#     assert result['result']['company'] == '中国移动'
#     assert result['result']['areacode'] == '0571'
#
#
# def test_mobile_post():
#     url = 'http://sellshop.5istudy.online/sell/shouji/query'
#     params = {
#         "shouji": '13456755448',
#         'appkey': '0c818521d38759e1'
#     }
#     r = requests.post(url=url, params=params)
#     assert r.status_code == 200
#     result = r.json()
#     assert result['status'] == 0
#     assert result['msg'] == 'ok'
#     assert result['result']['shouji'] == '13456755448'
#     assert result['result']['province'] == '北京'
#     assert result['result']['city'] == '北京'
#     assert result['result']['company'] == '中国移动'
#     assert result['result']['areacode'] == '0571'
#
#
# 前置步骤和后置处理
# def setup_function():
#     print('准备测试数据')
#
#
# def teardown_function():
#     print('清理测试数据')


# @pytest.fixture(scope='module', autouse=True)
# # @pytest.fixture()
# def fixture4():
#     print('我是前置步骤1234')


# class TestMobile:
#     @staticmethod
#     def setup_class():
#         print('准备测试数据')
#
#     @staticmethod
#     def teardown_class():
#         print('清理测试数据')
#
#     def test_mobile(self):
#         url = 'http://sellshop.5istudy.online/sell/shouji/query'
#         params = {"shouji": '13456755448', 'appkey': '0c818521d38759e1'}
#         r = requests.get(url=url, params=params)
#         assert r.status_code == 200
#         result = r.json()
#         assert result['status'] == 0
#         assert result['msg'] == 'ok'
#         assert result['result']['shouji'] == '13456755448'
#         assert result['result']['province'] == '北京'
#         assert result['result']['city'] == '北京'
#         assert result['result']['company'] == '中国移动'
#         assert result['result']['areacode'] == '0571'
#
#     def test_mobile_post(self):
#         url = 'http://sellshop.5istudy.online/sell/shouji/query'
#         params = {
#             "shouji": '13456755448',
#             'appkey': '0c818521d38759e1'
#         }
#         r = requests.post(url=url, params=params)
#         assert r.status_code == 200
#         result = r.json()
#         assert result['status'] == 0
#         assert result['msg'] == 'ok'
#         assert result['result']['shouji'] == '13456755448'
#         assert result['result']['province'] == '北京'
#         assert result['result']['city'] == '北京'
#         assert result['result']['company'] == '中国移动'
#         assert result['result']['areacode'] == '0571'


# 接口测试参数化

# @pytest.mark.parametrize('shouji,appkey', read_hero()['mobile_params'])
# def test_mobile_post(shouji, appkey):
#     print('测试手机归属地post请求')
#     url = 'http://sellshop.5istudy.online/sell/shouji/query'
#     params = {
#         "shouji": shouji,
#         'appkey': appkey
#     }
#     r = requests.post(url=url, params=params)
#     assert r.status_code == 200
#     result = r.json()
#     assert result['status'] == 0
#     assert result['msg'] == 'ok'
#     assert result['result']['shouji'] == '13456755448'
#     assert result['result']['province'] == '北京'
#     assert result['result']['city'] == '北京'
#     assert result['result']['company'] == '中国移动'
#     assert result['result']['areacode'] == '0571'
