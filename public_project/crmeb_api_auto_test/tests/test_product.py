
import pytest
import requests
import json
import logging
import allure
from jsonpath import jsonpath
from base.method import ApiRequest
from tools.data_loader import LoadData
from tools.excel_variable import ExcelVariable
log = logging.getLogger()
# test_cases = LoadData.loader_from_excel("product_api_test_cases.xlsx")
@pytest.mark.parametrize('case', LoadData.loader_from_excel("product_api_test_cases.xlsx"))
def test_product_api(get_token, case):
    with allure.step('获取uri和服务配置文件组装url并做特殊化处理'):
        log.info(f'当前用例编号为{case[ExcelVariable.case_id]}')
        log.info(f'当前用例名称为{case[ExcelVariable.case_title]}')
        protocol = LoadData.loader_from_ini('server_info', 'Protocol')
        host = LoadData.loader_from_ini('server_info', 'Host')
        port = LoadData.loader_from_ini('server_info', 'Port')
        uri = case[ExcelVariable.case_uri]
        address_param = case[ExcelVariable.case_address_param]
        if address_param:
            try:
                address_param = json.loads(address_param)
            except (json.JSONDecodeError, TypeError) as e:
                log.error(f'address_param JSON解析失败: {e}, 原始值: {address_param}')
                address_param = None
        if address_param:
            for key, value in address_param.items():
                uri = uri.replace(f'{{{key}}}', str(value))
        param_address = case[ExcelVariable.case_address_param]
        url = f"{protocol}://{host}:{port}{uri}"
        log.info(f'当前用例url为{url}')
    with allure.step('获取请求方法'):
        method = case[ExcelVariable.case_method]
        log.info(f'当前用例请求方法为{method}')
    with allure.step('获取请求头信息'):
        header = case[ExcelVariable.case_headers]
        if header:
            try:
                header = json.loads(header)
            except (json.JSONDecodeError, TypeError) as e:
                log.error(f'headers JSON解析失败: {e}, 原始值: {header}')
                header = None
            else:
                header["Authori-zation"] = f"Bearer {get_token}"
        else:
            header = None
        log.info(f'当前用例请求头为{header}')
    # 参数不一定是字典
    # 需要进行判断
    with allure.step('获取请求参数'):
        query_params = case[ExcelVariable.case_params]
        if query_params:
            try:
                query_params = json.loads(query_params)
            except (json.JSONDecodeError, TypeError) as e:
                log.error(f'query_params JSON解析失败: {e}, 原始值: {query_params}')
                query_params = None
        else:
            query_params = None
    def case_assert(r):
        assert r.status_code == int(case[ExcelVariable.case_code])
        try:
            act_value = r.json()
        except Exception as e:
            log.error(f'响应JSON解析失败: {e}')
            pytest.fail(f'响应体不是有效JSON: {r.text[:200]}')
        act_message = jsonpath(act_value, '$..message')
        if act_message:
            act_message = act_message[0]
        else:
            act_message = ''
        log.info(f'当前用例实际结果为{act_message}')
        assert act_message == case[ExcelVariable.case_expected]
    response = ApiRequest.send_request(method,url, headers=header, params=query_params)
    case_assert(response)
    # print(response.json())
    # assert response.status_code == 200









