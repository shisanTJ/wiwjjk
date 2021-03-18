from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
#
# import smtplib, datetime
#
# # 创建一个带附件的实例
#
#
# msg = MIMEMultipart()
#
# # 构造附件
# att = MIMEText(open("C:/Users/Pactera/Pictures/IU/微信图片_202010261451312.jpg", 'rb').read(), 'base64','gb2312')
# att["Content-Type"] = 'application/octet-stream'
# att["Content-Disposition"] = 'attachment; filename="test.jpg"'
# msg.attach(att)
#
# # 加邮件头
# # 收件人
# tomail =['942369647@qq.com','jing.tian6@pactera.com']
# # 发件人
# frommail ="shisantjgg@163.com"
# password ="ziji521"
# msg['from'] =Header(frommail)
# msg['to'] =Header(",".join(tomail))
#
# msg['subject'] = Header('日常接口测试结果 (' + str(datetime.date.today()) + ')', 'utf-8')
# # 发送邮件
# try:
#     server = smtplib.SMTP('smtp.163.com',25)
#     server.login(frommail,password)
#     server.sendmail(msg['from'], msg['to'], msg.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print('邮件发送失败')






# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
#
# sender = 'shisantjgg@163.com'  # 发送邮件的人
# receivers = ['942369647@qq.com']  # 接收邮件人
#
# # 第三方SMTP服务
# mail_host = 'smtp.163.com'  # 设置发送服务器
# mail_user = 'shisantjgg@163.com'  # 登录邮箱名
# mail_pass = 'ziji521'  # 口令（授权码）
#
# # 创建一个带附件的实例
# message = MIMEMultipart()
# message['From'] = Header(sender, 'utf-8')  # 发送者
# message['To'] = Header("942369647@qq.com", 'utf-8')  # 接收者
# subject = '日常接口巡检'  # 发送邮件标题
# message['Subject'] = Header(subject, 'utf-8')
#
# # 邮件正文内容
# mail_msg = '日常接口巡检,附件为测试结果,请查收'  # 发送邮件内容
# # 三个参数：第一个是文本内容，第二个plain设置文本格式，第三个utf-8设置编码
# message.attach(MIMEText(mail_msg, 'plain', 'utf-8'))  # 发送邮件正文(纯文本)
#
# # 构造附件1，传送当前目录下的文件
# att1 = MIMEText(open('../log/wiwj.log', 'rb').read(), 'base64', 'utf-8')
# att1['Content-Type'] = 'application/octet-stream'
# # 这里的filename是指邮件中显示的附件名称
# # att1['Content-Disposition'] = 'attachment;filename = "星测试附件.txt"'
# att1.add_header('Content-Disposition', 'attachment', filename='测试附件.txt')
# message.attach(att1)
#
# # # 构造附件1，传送当前目录下的文件
# # att2 = MIMEText(open('冒泡排序.py', 'rb').read(), 'base64', 'utf-8')
# # att2['Content-Type'] = 'application/octet-stream'
# # # 这里的filename是指邮件中显示的附件名称
# # att2.add_header('Content-Disposition', 'attachment', filename='冒泡排序.py')
# # message.attach(att2)
#
# try:
#     smtpObj = smtplib.SMTP(mail_host, 25)  # 发送服务器的端口号
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print('邮件发送成功')
# except smtplib.SMTPException:
#     print('邮件发送失败')

import smtplib                           #smtplib 用于邮件的发信动作
from email.mime.text import MIMEText         # email 用于构建邮件内容
from email.header import Header                #Header 用来构建邮件头
from email.mime.multipart import MIMEMultipart        #用于实例化附件（处理多种形态的邮件主体我们需要 MIMEMultipart 类）

def sendmail():
#发信方的信息：发信邮箱，邮箱授权码
    from_addr = 'shisantjgg@163.com'
    password = "ziji521"

    #收信方邮箱（因为是发送给多个人，所以我们可以用列表进行储存）
    to_addrs =[ '942369647@qq.com','jing.tian6@pactera.com']

    #发信服务器
    smtp_server = 'smtp.163.com'

    # 创建一个带附件的邮件实例
    message=MIMEMultipart()

    #邮箱正文内容，第一个参数为内容，第二个参数为格式（plain 为纯文本），第三个参数为编码
    text = '接口日常监控'      #若邮件正文较长，可以这样设置一个变量
    mail_inside = MIMEText(text,'plain','utf-8')             #传入文本，文本类型（plain）、文本编码

    #设置邮件头信息
    message['From'] = Header(from_addr)
    message['TO'] = Header(",".join(to_addrs))    #因为是多个邮件，所以需要用join,不信你可以试试不用join看下会报什么错呢
    message['Subject'] = Header('接口检测结果')
    message.attach(mail_inside)                   #传入邮件正文的内容

    #构造附件附件1
    attr1=MIMEText(open(r'../log/wiwj.log','rb').read(),'base64','utf-8')
    attr1["content_Type"]='application/octet-stream'
    attr1["Content-Disposition"] = 'attachment; filename="log.log"'  # 表示这是附件，名字是啥
    message.attach(attr1)

    # # 构造图片附件2
    # att2 = MIMEText(open(r'F:\猫看见\猫看见\Python代码\timg.jpg','rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="timg.jpg"'
    # message.attach(att2)

    # #构造html附件
    # att3 = MIMEText(open(r'F:\猫看见\猫看见\Python代码\boke.html', 'rb').read(), 'base64', 'utf-8')
    # att3["Content-Type"] = 'application/octet-stream'
    # att3["Content-Disposition"] = 'attachment; filename="boke.html"'
    # message.attach(att3)

    #用于捕捉错误
    try:
        #开启发信服务，这里使用的是加密传输加ssl是加密的
        server = smtplib.SMTP(smtp_server,25)
        #登录发信邮箱
        server.login(from_addr,password)
        #发送邮件
        server.sendmail(from_addr,to_addrs,message.as_string())
        #关闭服务器
        server.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误


