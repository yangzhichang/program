import smtplib
from email.mime.text import MIMEText
msg_from='2500372180@qq.com'n'g
passwd='zoycvzwfbbajddgb'
msg_to='57820048@qq.com'

subject="2018144130杨志昌的第一次作业"
content="内网手机wifi：192.168.137.1  外网手机wifi:10.28.87.208  内网手机流量：172.69.33.98  外网手机流量：106.61.134.39"
msg=MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,passwd)
    s.sendmail(msg_from,msg_to,msg.as_string())
    print("发送成功")
except(s.SMTPException,e):
    print("发送失败")
finally:
    s.quit()
