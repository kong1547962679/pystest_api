import pytest
import logging


from commons.requests_util import RequestUtil
from commons.yaml_util import yaml_path
from commons.yaml_util import write_yaml, read_yaml, read_yaml_testcase, csv_data

class CasesApi:

    logger = logging.getLogger(__name__)

    @pytest.mark.parametrize('cassesinfo', read_yaml_testcase('/test_api.yaml'))
    def test_cases_api(self, cassesinfo):
        print(cassesinfo)
        lis = ['method', 'url', 'params', 'data', 'headers', 'cookies', 'files', 'auth', 'timeout', 'allow_redirects',
               'proxies', 'hoooks', 'stream', 'verify', 'cert', 'json']
        data = {}
        for i in set(cassesinfo.keys()) & set(lis):
            data.update({i:cassesinfo[i]})

        RequestUtil().send_all_rquest({})



