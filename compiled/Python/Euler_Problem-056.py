# compiled with BefunCompile v1.0.4 (c) 2015
# execute with at least Python3
import gzip, base64
_g = ("AR+LCAAAAAAABACtkbEKwyAQhl9FNC6RNKdBSI8gnQrtE2QQU+jg6uQU8uzV0rRTBou3nAf63fdjnOeZsCpFKqJyVUTVKbMf6JNGQpaY4Y/2rHEqRUVBbxudbCJ9HxvU"
  + "WvC12Ep2CBbplfK4zyt2kpBiqxVDnzhWaDJdTl42TDXFkI9VI8exVQEUBAnBwACBbncqsh6+bbWwqfVegm8VeJHj9/GIp2RIH5Czud3pp8tTQxtgEB4G5ELrtPjI3KU7"
  + "i2MPLw0jjqk0/pHyBanoFos5AwAA")
g = base64.b64decode(_g)[1:]
for i in range(base64.b64decode(_g)[0]):
    g = gzip.decompress(g)
g=list(g)
def gr(x,y):
    if(x>=0 and y>=0 and x<75 and y<11):
        return g[y*75 + x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<75 and y<11):
        g[y*75 + x]=v;
def td(a,b):
    return bool(random.getrandbits(1))
def td(a,b):
    return ((0)if(b==0)else(a//b))
def tm(a,b):
    return ((0)if(b==0)else(a%b))
s=[]
def sp():
    global s
    if (len(s) == 0):
        return 0
    return s.pop()
def sa(v):
    global s
    s.append(v)
def sr():
    global s
    if (len(s) == 0):
        return 0
    return s[-1]
def _0():
    gw(63,2,0)
    sa(99)
    sa(99)
    sa(99)
    return 1
def _1():
    sa(198)
    sa(198)
    return 2
def _2():
    return (3)if(sp()!=0)else(4)
def _3():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    sa(0)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(sr())
    sa(70)
    v0=sp()
    sa(tm(sp(),v0))
    sa(5)
    sa(sp()+sp());
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(70)
    v0=sp()
    sa(td(sp(),v0))
    v0=sp()
    v1=sp()
    gw(v1,v0,sp())
    sa(sr())
    return 2
def _4():
    gw(64,2,1)
    gw(2,0,0)
    sp()
    gw(1,0,sp())
    return 5
def _5():
    gw(3,0,0)
    sa(199)
    sa(199)
    sa(((gr(64,2))*(gr(1,0)))+(gr(2,0)))
    gw(2,0,td(((gr(64,2))*(gr(1,0)))+(gr(2,0)),10))
    return 6
def _6():
    sa(10)
    v0=sp()
    sa(tm(sp(),v0))
    sa(sr())
    sa(gr(3,0))
    sa(sp()+sp());
    gw(3,0,sp())
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(sr())
    sa(70)
    v0=sp()
    sa(tm(sp(),v0))
    sa(5)
    sa(sp()+sp());
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(70)
    v0=sp()
    sa(td(sp(),v0))
    v0=sp()
    v1=sp()
    gw(v1,v0,sp())
    sa(sr())
    return (17)if(sp()!=0)else(7)
def _7():
    sp()
    sa((1)if((gr(3,0))>(gr(2,1)))else(0))
    return (16)if(sp()!=0)else(8)
def _8():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    return (5)if(sp()!=0)else(9)
def _9():
    sp()
    return 10
def _10():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    return (11)if(sp()!=0)else(13)
def _11():
    sa(sr())
    sa(10)
    v0=sp()
    sa(tm(sp(),v0))
    return (14)if(sp()!=0)else(12)
def _12():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    return (11)if(sp()!=0)else(13)
def _13():
    sp()
    print(gr(2,1),end="",flush=True)
    return 18
def _14():
    sa(sr())
    sa(45)
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return (15)if(sp()!=0)else(10)
def _15():
    gw(63,2,0)
    sa(sr())
    sa(99)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    return 1
def _16():
    gw(2,1,gr(3,0))
    return 8
def _17():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    sa(sr())
    sa(sr())
    sa(70)
    v0=sp()
    sa(tm(sp(),v0))
    sa(5)
    sa(sp()+sp());
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(70)
    v0=sp()
    sa(td(sp(),v0))
    v0=sp()
    sa(gr(sp(),v0))
    sa(gr(1,0))
    sa(sp()*sp());
    sa(gr(2,0))
    sa(sp()+sp());
    sa(sr())
    sa(10)
    v0=sp()
    sa(td(sp(),v0))
    gw(2,0,sp())
    return 6
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17]
c=0
while c<18:
    c=m[c]()