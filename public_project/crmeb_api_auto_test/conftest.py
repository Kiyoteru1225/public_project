

import subprocess
import json
import pytest
import requests
from config.settings import BASE_URL,LOGIN_ACCOUNT,LOGIN_PASSWORD

def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

@pytest.fixture(scope='module', autouse=True)
def get_token():
    url = f'{BASE_URL}/api/front/login'
    json_data = {
        'account': LOGIN_ACCOUNT,
        'password': LOGIN_PASSWORD
    }
    try:
        response = requests.request(method='post', url=url, json=json_data, timeout=10)
        token = response.json()['data']['token']
        if not token:
            pytest.fail('登录成功但token为空')
        return token
    except requests.exceptions.RequestException as e:
        pytest.fail(f'登录请求失败: {e}')
    except (KeyError, json.JSONDecodeError) as e:
        pytest.fail(f'登录响应解析失败: {e}')


# session结束的时候执行,
def pytest_sessionfinish(session, exitstatus):
    subprocess.run("allure generate ./report/temps -o ./report/html --clean", shell=True)