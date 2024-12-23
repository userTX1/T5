import binascii
"""
s = b'a'
h = binascii.b2a_hex(s)
ac=str(h,encoding='utf-8')
print(ac)
ad=b'31'
d=binascii.a2b_hex(ad)
print(d)
"""

gb5=''
jh=b''
def aa5(as1):
    global gb5
    global jh
    jh+=bytes(as1,'utf-8')
    acd = binascii.a2b_hex(jh)
    print(acd)
def bg5():
    aa5('31323334')
bg5()