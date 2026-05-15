import requests
class ApiRequest:
    @staticmethod
    def send_request( method,url,params=None,data=None,headers=None,cookies=None,files=None,
                      auth=None,timeout=None,allow_redirects=True,proxies=None,hooks=None,
                      stream=None,verify=None,cert=None,json=None):
        """
        if method == 'get':
            res = requests.get(url,params=params)
        elif method == 'post':
            res = requests.post(url,data=data,json=json)
        elif method == 'put':
            res = requests.put(url,data=data,json=json)
        elif method == 'delete':
            res = requests.delete(url,params=params)
        else:
            print('请输入正确的请求方式')
        """
        responses = requests.request(method, url, headers=headers, cookies=cookies, files=files,
                                     auth=auth, timeout=timeout, allow_redirects=allow_redirects,
                                     proxies=proxies, hooks=hooks, stream=stream, verify=verify,
                                     cert=cert, params=params, data=data, json=json)
        return responses