from config import BASE_URL
from tools.get_log import GetLog
import smtplib  # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText  # email 用于构建邮件内容
from email.header import Header  # Header 用来构建邮件头
from email.mime.multipart import MIMEMultipart  # 用于实例化附件（处理多种形态的邮件主体我们需要 MIMEMultipart 类）

log = GetLog.get_logger()


class Tools:
    # 提取token
    @classmethod
    def get_token(cls, response):
        # 提取token
        token = response.json().get("data").get("token")
        log.info("正在提取token:{}".format(token))
        # 将token追加到 api.headers
        # api.headers['Authorization'] = "Bearer " + token

    # 断言
    @classmethod
    def official_assert_common(cls, response, msg="OK", status=200):
        try:
            log.info("正在断言msg:{}".format(response.json().get("msg")))
            # 断言响应信息
            assert msg == response.json().get("msg")
            # 断言状态码
            assert status == response.status_code


        except Exception as e:
            log.error(e)
            raise

    @classmethod
    def send_mail(cls):
        from_addr = 'shisantjgg@163.com'
        password = "ziji521"

        # 收信方邮箱（因为是发送给多个人，所以我们可以用列表进行储存）
        to_addrs = ['942369647@qq.com', 'jing.tian6@pactera.com']

        # 发信服务器
        smtp_server = 'smtp.163.com'

        # 创建一个带附件的邮件实例
        message = MIMEMultipart()

        # 邮箱正文内容，第一个参数为内容，第二个参数为格式（plain 为纯文本），第三个参数为编码
        text = '接口日常监控'  # 若邮件正文较长，可以这样设置一个变量
        mail_inside = MIMEText(text, 'plain', 'utf-8')  # 传入文本，文本类型（plain）、文本编码

        # 设置邮件头信息
        message['From'] = Header(from_addr)
        message['TO'] = Header(",".join(to_addrs))  # 因为是多个邮件，所以需要用join,不信你可以试试不用join看下会报什么错呢
        message['Subject'] = Header('接口检测结果')
        message.attach(mail_inside)  # 传入邮件正文的内容

        # 构造附件附件1
        attr1 = MIMEText(open(BASE_URL + '/log/wiwj.log', 'rb').read(), 'base64', 'utf-8')
        attr1["content_Type"] = 'application/octet-stream'
        attr1["Content-Disposition"] = 'attachment; filename="log.txt"'  # 表示这是附件，名字是啥
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

        # 用于捕捉错误
        try:
            # 开启发信服务，这里使用的是加密传输加ssl是加密的
            server = smtplib.SMTP(smtp_server, 25)
            # 登录发信邮箱
            server.login(from_addr, password)
            # 发送邮件
            server.sendmail(from_addr, to_addrs, message.as_string())
            # 关闭服务器
            server.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print('error', e)  # 打印错误
