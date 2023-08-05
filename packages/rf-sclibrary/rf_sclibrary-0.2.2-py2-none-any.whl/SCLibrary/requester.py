# -*- coding:utf-8 -*-

from fork_requests import RequestsKeywords
from base import keyword
from json import dumps
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from robot.libraries.BuiltIn import BuiltIn
from zk import ZookeeperRegistry

class RequesterKeywords(RequestsKeywords):

    def __init__(self):
        super(RequesterKeywords, self).__init__()
        self.response = None
        self.zk = None

    @keyword("HTTP Create Session")
    def http_create_session(self, alias, url, headers={}, cookies={},
                            auth=None, timeout=None, proxies=None,
                            verify=False, debug=0, max_retries=3, backoff_factor=0.10, disable_warnings=0):
        if(not headers.has_key('Content-Type')):
            headers['Content-Type'] = 'application/json'
        if(not headers.has_key('charset')):
            headers['charset'] = 'utf-8'
        if(not headers.has_key('Accept-Encoding')):
            headers['Accept-Encoding'] = 'gzip'
        if(not headers.has_key('Accept-Language')):
            headers['Accept-Language'] = 'zh-CN'
        return super(RequesterKeywords, self).create_session(alias,
                                                             url,
                                                             headers,
                                                             cookies,
                                                             auth,
                                                             timeout,
                                                             proxies,
                                                             verify,
                                                             debug,
                                                             max_retries,
                                                             backoff_factor,
                                                             disable_warnings)

    @keyword("HTTP Post")
    def http_post(self,
                  alias,
                  uri,
                  params=None,
                  headers=None,
                  data=None,
                  json=None,
                  files=None,
                  allow_redirects=None,
                  timeout=None):
        return self.http_post_request(alias,
                                      uri,
                                      params,
                                      headers,
                                      data,
                                      json,
                                      files,
                                      allow_redirects,
                                      timeout)

    @keyword("HTTP Post Request")
    def http_post_request(self,
                  alias,
                  uri,
                  params=None,
                  headers=None,
                  data=None,
                  json=None,
                  files=None,
                  allow_redirects=None,
                  timeout=None):
        self.response = None
        self.response = super(RequesterKeywords, self).post_request(alias,
                                                                    uri,
                                                                    data,
                                                                    json,
                                                                    params,
                                                                    headers,
                                                                    files,
                                                                    allow_redirects,
                                                                    timeout)
        return self.response.json()

    @keyword("HTTP Get")
    def http_get(self,
                 alias,
                 uri,
                 params=None,
                 headers=None,
                 json=None,
                 allow_redirects=None,
                 timeout=None):
        return self.http_get_request(alias,
                                     uri,
                                     params,
                                     headers,
                                     json,
                                     allow_redirects,
                                     timeout)

    @keyword("HTTP Get Request")
    def http_get_request(self,
                         alias,
                         uri,
                         params=None,
                         headers=None,
                         json=None,
                         allow_redirects=None,
                         timeout=None):
        self.response = None
        self.response = super(RequesterKeywords, self).get_request(alias,
                                                                   uri,
                                                                   headers,
                                                                   json,
                                                                   params,
                                                                   allow_redirects,
                                                                   timeout)
        return self.response.json()

    @keyword("HTTP Delete All Sessions")
    def http_delete_all_session(self):
        super(RequesterKeywords, self).delete_all_sessions()

    @keyword("HTTP Update Session")
    def http_update_session(self, alias, headers=None, cookies=None):
        super(RequesterKeywords, self).update_session(alias, headers, cookies)

    @keyword("HTTP Code Should Be")
    def http_code_should_be(self, code):
        resp_code = self.get_response_value(
            'code', '该关键词 仅适用于类似 {code: xxx} 返回结构')
        if(resp_code != code):
            raise AssertionError("%s != %s" % (code, resp_code))

    @keyword("HTTP Check if Success")
    def http_check_if_success(self):
        success = self.get_response_value(
            'success', '该关键词 仅适用于类似 {success: boolean} 返回结构')
        if(success == False):
            raise AssertionError("期望请求成功，但是现在是失败!".decode('utf-8'))

    @keyword("HTTP Check if Failure")
    def http_check_if_failure(self):
        success = self.get_response_value(
            'success', '该关键词 仅适用于类似 {success: boolean} 返回结构')
        if(success == True):
            raise AssertionError("期望请求失败，但是现在是成功!".decode('utf-8'))

    @keyword("DUBBO Request")
    def dubbo_post(self, interface, method, token='souche_http_token', type='form', params=None, headers=None):
        if self.zk is None:
            built_in = BuiltIn()
            rf_zk = built_in.get_variable_value("${RF_ZK}")
            self.zk = ZookeeperRegistry(rf_zk)

        url = self.zk.subscribe(interface)[0]

        session_headers = {}
        if type == 'form':
            # type=json时， Content-Type默认为application/json
            session_headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.http_create_session(alias='dubbo', url='http://%s' % url, headers=session_headers)
        headers = {'_method_name': method, '_dubbo_token': token}
        return self.http_post(alias='dubbo', uri='/%s' % interface, data=params, headers=headers)


    @keyword("To Json")
    def http_to_json(self, content, pretty_print=False):
        return super(RequesterKeywords, self).to_json(alias, headers, cookies)

    @keyword("To String")
    def http_to_string(self, list_or_dict):
        return dumps(list_or_dict, ensure_ascii=False)

    def get_response_value(self, key, exception):
        json = self.response.json()
        if(not json.has_key(key)):
            raise AssertionError(exception.decode('utf-8'))
        return json[key]
