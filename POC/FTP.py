"""
from ftplib import FTP
cd=FTP()
df=cd.connect('192.168.180.169',21)
print(str(df))
"""
import ftplib

# FTP服务器地址、用户名和密码
host = '192.168.180.169'
username = ''  # 空字符串表示匿名登录
password = ''  # 同样为空字符串表示不需要密码验证
try:
    # 连接到FTP服务器
    ftp = ftplib.FTP(host)
    # 登录
    ftp.login(user=username, passwd=password)
    # 打印当前工作目录
    print('当前工作目录:', ftp.pwd())
    # 列出目录内容
    files = ftp.nlst()
    for file in files:
        print(file)
except Exception as e:
    print("发生错误:", str(e))
