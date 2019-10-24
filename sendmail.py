import smtplib
from smtplib import SMTP_SSL

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def sendmail():

    my_sender='tyronnlue123@sina.com'   # 发件人邮箱账号
    my_pass = 'adac2c6751b1ed36'            # 发件人邮箱密码
    my_user='18832128399@163.com'    # 收件人邮箱账号，我这边发送给自己
    def mail():
        ret=True
        try:
            msg=MIMEText('填写邮件内容','plain','utf-8')
            msg['From']=formataddr(["FromRunoob",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To']=formataddr(["FK",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject']="first mail"                # 邮件的主题，也可以说是标题
    
            server=smtplib.SMTP_SSL('smtp.sina.com' , 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret=False
        return ret
    
    ret=mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")

    # # 第三方 SMTP 服务
    # mail_host='smtp.sina.com'  #设置服务器
    # mail_user='tyronnlue123@sina.com'   #用户名
    # mail_pass='adac2c6751b1ed36' #口令 
    
    
    # sender = 'tyronnlue123@sina.com' 
    # receivers = ['18832128399@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    
    # message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
    # message['From'] = Header("菜鸟教程", 'utf-8')
    # message['To'] =  Header("测试", 'utf-8')
    
    # subject = 'Python SMTP 邮件测试'
    # message['Subject'] = Header(subject, 'utf-8')
    
    
    # try:
    #     smtpObj = smtplib.SMTP() 
    #     smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    #     smtpObj.login(mail_user,mail_pass)  
    #     smtpObj.sendmail(sender, receivers, message.as_string())
    #     print("邮件发送成功")
    # except smtplib.SMTPException:
    #     print("Error: 无法发送邮件")
    # smtp = smtplib.SMTP() 
    # smtp.connect('smtp.sina.com',25)
    # #smtp=SMTP_SSL('smtp.sina.com') 
    # smtp.login('tyronnlue123@sina.com', 'adac2c6751b1ed36') 
        
    # content='test mail'
    # #输入你的邮件正文
    # msg = MIMEText(content, 'plain', 'utf-8')
    # sender='tyronnlue123@sina.com'
    # receiver='18832128399@163.com'
    # try:
    #     smtp.sendmail(sender, receiver, msg.as_string())
    #     print("邮件发送成功")
    # except smtplib.SMTPException:
    #     print("Error: 无法发送邮件")
    # smtp.quit()

if __name__ == '__main__':
    sendmail()
