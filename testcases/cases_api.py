import pytest
import logging

from commons.requests_util import RequestUtil
from commons.yaml_util import write_yaml, read_yaml, read_yaml_testcase, yaml_path
from commons.validate_util import equals, contains

class CasesApi:

    logger = logging.getLogger(__name__)
    # @pytest.mark.parametrize('cassesinfo',[k for i in yaml_path() for k in read_yaml_testcase(i)])
    @pytest.mark.parametrize('cassesinfo',read_yaml_testcase('/test_api.yaml'))
    def test_cases_api(self,cassesinfo):
        data_list = ['method','url','params','data','headers','cookies','files','auth','timeout','allow_redirects','proxies','hoooks','stream','verify','cert','json']
        send_res = ''
        try:
            self.logger.warning('{}'.format('-' * 100))
            self.logger.warning('{}{}{}'.format('-'*30,cassesinfo['name'],'-'*30))
            # self.logger.info('cassesinfo：{}'.format(cassesinfo))
            self.logger.info('url：{}'.format(cassesinfo['url']))
            self.logger.info('method：{}'.format(cassesinfo['method']))
            if 'params' in cassesinfo.keys():
                self.logger.info('params：{}'.format(cassesinfo['params']))
            if 'data' in cassesinfo.keys():
                self.logger.info('data：{}'.format(cassesinfo['data']))
            if 'files' in cassesinfo.keys():
                self.logger.info('files：{}'.format(cassesinfo['files']))
            self.logger.info('validate：{}'.format(cassesinfo['validate']))
            for i in set(cassesinfo.keys()) & set(data_list):
                send_res += '{}=cassesinfo["{}"],'.format(i,i)
            if 'token' in cassesinfo['name']:
                res = eval("RequestUtil().send_all_rquest({})".format(send_res.strip(',')))
                write_yaml({cassesinfo['name']: res.json()[cassesinfo['name']]})
            else:
                for i in cassesinfo['params'].keys():
                    if 'token' in i:
                        cassesinfo['params'][i] = read_yaml()[i]
                        break
                if 'files' in send_res:
                    res = eval("RequestUtil().send_all_rquest({})".format(send_res.replace('=cassesinfo["files"]',"={'media': open(cassesinfo['files'], 'rb')}").strip(',')))
                else:
                    res = eval("RequestUtil().send_all_rquest({})".format(send_res.strip(',')))
            self.logger.info('msg：{}'.format(res.text))
        except Exception as e:
            self.logger.exception(e)

        try:
            for i in cassesinfo['validate']:
                for k,v in i.items():
                    flas = ''
                    if k == 'eq':
                        flas = eval("res.{}".format(i[k][0]))
                        equals(flas,i[k][1])
                        self.logger.info('{} -----> {} == {}'.format(k,i[k][1],flas))
                    elif k == 'con':
                        flas = eval("res.{}".format(i[k][0]))
                        contains(str(i[k][1]),str(flas))
                        self.logger.info('{} -----> {} in {}'.format(k, i[k][1],flas))
        except AssertionError as e:
            self.logger.error(e)
            raise
        except Exception as e:
            self.logger.exception(e)
            raise



