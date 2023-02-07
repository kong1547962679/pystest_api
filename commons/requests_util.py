import requests


class RequestUtil:

    sess = requests.session()

    def send_all_rquest(self,**kwargs):
        res = RequestUtil.sess.request(**kwargs)
        # print(res.text)
        return res
