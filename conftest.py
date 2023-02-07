import pytest
from commons.yaml_util import clear_yaml, read_yaml_testcase

# fixture固件
@pytest.fixture(scope='session',autouse=True)
def clear_session():
    # print('清空yaml参数')
    clear_yaml()
    yield
    # print('yaml参数清空完毕')

# fixture固件
@pytest.fixture(scope='function',autouse=True)
def cases():
    print('-'*10,'用例开始执行','-'*10)
    yield
    print('-'*10,'用例执行完毕!','-'*10)

@pytest.fixture(scope="function")
def demo_fixture():
    print("用例前置操作->do something .....")
    yield
    print("用例后置操作，do something .....")