# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :send_email.py
# @Date     :2020/11/10 22:30
# @Author   :刘旭
-------------------------------------------------
"""

# 实现对邮件进行发送
import smtplib
# 邮件头部包
from email.header import Header
# 邮件文本包
from email.mime.text import MIMEText
# 邮件附件包
from email.mime.multipart import MIMEMultipart
from logger.logger import LoggerInfo


log = LoggerInfo().logger()
class sendEmail:
    def send(self):
        massage = MIMEMultipart()
        # 邮件：_text正文内容，_subtype文本格式，编码格式
        massage.attach(MIMEText(_text='自动化用例测试结束，请查看下方测试报告！', _subtype='plain', _charset='utf-8'))
        # 读取附件文件
        att1 = MIMEText(open('./report/html/index.html', 'rb').read(), 'base64', 'utf-8')
        # 文件类型是二进制流数据
        att1['Content-Type'] = 'application/octet-stream'
        # 设置附件文件的名称、后缀
        att1['Content-Disposition'] = 'attachment; filename="index.html"'
        # 邮件内容添加附件
        massage.attach(att1)
        # 设置邮件发送人名称，邮件接收人名称，邮件标题
        massage['From'] = Header('刘旭<529166299@qq.com>', 'utf-8')
        massage['To'] = Header('发送给谁dsadsadsad     dsadsadas dasd sad  dsadsad', 'utf-8')
        massage['Subject'] = Header('python邮件附件发送', 'utf-8')
        try:
            # 实例化smtplib
            smtpeml = smtplib.SMTP()
            # 连接smtp服务器，host：qq的smpt服务器地址，port：端口号
            smtpeml.connect(host='smtp.qq.com', port='587')
            # 用户登录smtp服务器，用户名和授权码登录
            user = '529166299@qq.com'
            pwd = 'ohwsfdphqahcbhed'
            smtpeml.login(user=user, password=pwd)
            # 发送邮件的邮箱
            sender = '529166299@qq.com'
            # 可以发送多人接受
            receiver = ['529166299@qq.com']
            # 发送邮件
            smtpeml.sendmail(sender, receiver, massage.as_string())
            log.info('邮件发送中......')
        except smtplib.SMTPException:
            log.error('邮件发送失败')


if __name__ == '__main__':
    sendEmail().send()
