import base64
import re
from urllib.parse import quote
import urllib
import binascii
#------------------------------------------------------------------------------------------base64
df=''
def a1(as1):
    global df
    b = base64.b64decode(as1)
    df = str(b, 'utf-8')
def s1():
    global df
    return df
def ss1():
    global df
    df=''
#------------------------------------------------------------------------------------------unicode
df1=''
def a2(as1):
    global df1
    ass1=as1
    aa12 = re.findall('\\\[a-z,A-Z]', as1)
    for i in aa12:
        ass1 = ass1.replace(i, '\\u')
    cda = ass1.encode('utf-8').decode('unicode_escape')
    df1 = cda
def s2():
    global df1
    return df1
def ss2():
    global df1
    df1=''
#------------------------------------------------------------------------------------------url
df3=''
def a3(as1):
    global df3
    acd = urllib.parse.unquote(as1)
    df3 = acd
def s3():
    global df3
    return df3
def ss3():
    global df3
    df3=''
#------------------------------------------------------------------------------------------GBK
gb3=''
def aa3(as1):
    global gb3
    acd=urllib.parse.unquote(as1,encoding='gb2312')
    gb3 = acd
def bg3():
    global gb3
    return gb3
#------------------------------------------------------------------------------------------hex
gb5=''
jh=b''
def aa5(as1):
    global gb5,jh
    try:
        jh += bytes(as1, 'utf-8')
        acd = binascii.a2b_hex(jh)
        ac = str(acd, encoding='utf-8')
        gb5 = ac
    except:
        pass
def bg5():
    global gb5
    return gb5
def k():
    global jh,gb5
    gb5=''
    jh=b''
#------------------------------------------------------------------------------------------字节流
df4=[]
dff4=''
def a4(as1):
    global df4
    global dff4
    if len(as1)%8==0:
        ca = len(as1) / 8
        s = as1
        g = 0
        b = 8
        asd = 0 #等于ca停止循环
        while True:
            asd += 1
            dg = s[g:b]
            if dg[0:4] == '0000':
                sd = dg.replace('0000', '\\u')
                cda = sd.encode('utf-8').decode('unicode_escape')
                df4.append(str(cda))
                g += 8
                b += 8
            else:
                dff4 = 'Unicode字节流解码失败 密文不完整或拆分为8的倍数 ×'
            if asd == ca:
                break
    else:
        dff4='Unicode字节流解码失败 密文不完整或拆分为8的倍数 ×'
def s4():
    global df4
    global dff4
    if dff4!='':
        return dff4
    else:
        return '尝试解码Unicode字节流：'+str(df4)
def ss4():
    global dff4
    df4.clear()
    dff4=''
