# # 创建这个文件，解决问题
# # ModuleNotFoundError: No module named 'utils'
import pytest
#这是目录级别的前置和后置条件


@pytest.fixture(scope='package', autouse=True)
def st_emptyEnv():
    print(f'\n#### 前置初始化-目录甲')
    yield

    print(f'\n#### 后置清除-目录甲')
