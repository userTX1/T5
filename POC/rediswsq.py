import socket
import sys
import re
import os

PASSWORD_DIC=['redis','root','oracle','password','p@aaw0rd','abc123!','123456','admin']
a='redis_version'
b='Authentication'
c='+OK'
g=''
def check(ip, port, timeout):
    global a,b,c
    global PASSWORD_DIC
    global g
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.send("INFO\r\n".encode())
        result = s.recv(1024)
        g="[+]链接成功"
        if a.encode() in result:
            g="[+]漏洞存在\n"+str(a.encode())
        elif b.encode() in result:
            for pass_ in PASSWORD_DIC:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, int(port)))
                s.send("AUTH %s\r\n" %(pass_))
                result = s.recv(1024)
                if c.encode() in result:
                    g=u"[+]存在弱口令，密码：%s" % (pass_)
                    print(g)
                else:
                    g = "[-]不在弱口令"
        else:
            g="[-]漏洞不存在"
    except Exception as aa:
        g="[-]端口未开启"+str(aa)
def jg11():
    global g
    return '--------------------------------------------------\n[ Redis未授权+弱口令 ]\n\n' + str(g) + '\n'
def u11(aoca):
    global g
    ip = re.search(r'//([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}):(.*?)/', aoca)
    try:
        if ip.group()!=None:
            check(ip.group(1),ip.group(2), timeout=6)
    except:
        g='格式：http://10.0.0.1:端口'