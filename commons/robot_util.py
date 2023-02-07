# 封装企业微信机器人
import datetime
import requests

headers = {'Content-Type':'application/json'}
# 机器人的webhook地址
key = ''
urlw = 'https://qyapi.weixin.qq.com/com/cgi-bin/webhook/send?key={}'.format(key)
def robot_send_message(projname,total,passed,failed,skipped,adress):
    time = datetime.datetime.now()
    data = {
        'msgtype':'markdown',
        'markdown':{
            'content':'''
                <font color=\"warning\">提醒！自动人测试反馈\n请求相关同事注意，及时跟进！\n
                > 用例执行完毕时间：<font color=\"info\">{}</font>\n
                > 项目名称：<font color=\"comment\">{}</font>\n
                > 用例总数：<font color=\"comment\">{}</font>\n
                > 通过用例数：<font color=\"info\">{}</font>\n
                > 失败用例数：<font color=\"warning\">{}</font>\n
                > 跳过用例数：<font color=\"warning\">{}</font>\n
                > 报告链接：{}
            '''.format(time,projname,total,passed,failed,skipped,adress)
        }
    }
    print(data)
    # requests.post(url=urlw,headers=headers,json=data)
    print('发消息了')

robot_send_message(11,22,33,44,55,66)

