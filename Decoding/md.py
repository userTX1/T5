import hashlib
import base64

w1=''
def mdd(c1):
    global w1
    cd=hashlib.md5()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w1=c3
def m1():
    global w1
    return 'MD5:\n'+str(w1)+'\n'
def m2(aoca):
    url1 = aoca
    mdd(url1)

w2=''
def mdd1(c1):
    global w2
    cd=hashlib.blake2b()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w2=c3
def m3():
    global w2
    return 'Blake2b加密:\n'+str(w2)+'\n'
def m4(aoca):
    url1 = aoca
    mdd1(url1)

w3=''
def mdd2(c1):
    global w3
    cd=hashlib.sha384()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w3=c3
def m5():
    global w3
    return 'Sha384加密:\n'+str(w3)+'\n'
def m6(aoca):
    url1 = aoca
    mdd2(url1)

w4=''
def mdd3(c1):
    global w4
    cd=hashlib.sha256()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w4=c3
def m7():
    global w4
    return 'Sha256加密:\n'+str(w4)+'\n'
def m8(aoca):
    url1 = aoca
    mdd3(url1)

w5=''
def mdd4(c1):
    global w5
    cd=hashlib.sha1()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w5=c3
def m9():
    global w5
    return 'Sha1加密:\n'+str(w5)+'\n'
def m10(aoca):
    url1 = aoca
    mdd4(url1)

w6=''
def mdd5(c1):
    global w6
    cd=hashlib.sha224()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w6=c3
def m11():
    global w6
    return 'Sha224加密:\n'+str(w6)+'\n'
def m12(aoca):
    url1 = aoca
    mdd5(url1)

w7=''
def mdd6(c1):
    global w7
    cd=hashlib.sha512()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w7=c3
def m13():
    global w7
    return 'Sha512加密:\n'+str(w7)+'\n'
def m14(aoca):
    url1 = aoca
    mdd6(url1)

w8=''
def mdd7(c1):
    global w8
    cd=hashlib.blake2s()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w8=c3
def m15():
    global w8
    return 'Blake2s加密:\n'+str(w8)+'\n'
def m16(aoca):
    url1 = aoca
    mdd7(url1)

w9=''
def mdd8(c1):
    global w9
    cd=hashlib.sha3_224()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w9=c3
def m17():
    global w9
    return 'Sha3_224加密:\n'+str(w9)+'\n'
def m18(aoca):
    url1 = aoca
    mdd8(url1)

w10=''
def mdd9(c1):
    global w10
    cd=hashlib.sha3_256()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w10=c3
def m19():
    global w10
    return 'Sha3_256加密:\n'+str(w10)+'\n'
def m20(aoca):
    url1 = aoca
    mdd9(url1)

w11=''
def mdd10(c1):
    global w11
    cd=hashlib.sha3_384()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w11=c3
def m21():
    global w11
    return 'Sha3_384加密:\n'+str(w11)+'\n'
def m22(aoca):
    url1 = aoca
    mdd10(url1)

w12=''
def mdd11(c1):
    global w12
    cd=hashlib.sha3_512()
    cd.update(c1.encode())
    c3=cd.hexdigest()
    w12=c3
def m23():
    global w12
    return 'Sha3_512加密:\n'+str(w12)+'\n'
def m24(aoca):
    url1 = aoca
    mdd11(url1)

w13=''
def mdd12(c1):
    global w13
    encodestr = base64.b64encode(c1.encode('utf-8'))
    c3=str(encodestr, 'utf-8')
    w13=c3
def m25():
    global w13
    return 'Base64编码:\n'+str(w13)+'\n'
def m26(aoca):
    url1 = aoca
    mdd12(url1)

import urllib.parse


w14=''
def mdd13(c1):
    global w14
    url = urllib.parse.quote(c1)
    w14=url
def m27():
    global w14
    return 'URL编码:\n'+str(w14)+'\n'
def m28(aoca):
    url1 = aoca
    mdd13(url1)

w15=''
def mdd14(c1):
    global w15
    url = c1.encode('gb2312')
    w15=url
def m29():
    global w15
    return 'gb2312编码:\n'+str(w15)+'\n'
def m30(aoca):
    url1 = aoca
    mdd14(url1)

hj=''
def a123(jh1):
    import binascii
    global hj
    jh=b''
    jh += bytes(jh1, 'utf-8')
    h = binascii.b2a_hex(jh)
    ac = str(h, encoding='utf-8')
    hj=ac
def s123():
    global hj
    return 'hex编码:\n' + str(hj) + '\n'