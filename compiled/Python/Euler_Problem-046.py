# compiled with BefunCompile v1.0.4 (c) 2015
# execute with at least Python3
import gzip, base64
_g = ("AR+LCAAAAAAABADt2k1Lw0AQBuC/st20l4S4k020zVAWL5716CGkRS0LoriI7qk/3lk/oNraFooo8j6wgelMs5uZ5taYJSotY9TF48Pt4vpJnT3fLR5VmeKru8W9ak7U"
  + "H5cBAAAAAAAAAAAAAAAAAAAAAAAA/AO/+V88Z3cUxNViii5GFagtPLW55UDjsvM0TiFPf/Kcn84Risp4qrqRXLjT53qqhvHbb75ZPV17GsIkU9E0HxnHLfliTH4+UEun"
  + "b7TNuaKgrWZLIW8o2JrCrj3eOJJSVR/LZVP2mLwtWLIsO/hRJxdTFV4rXWb9rHdVSvpykMXZesVASlK6K61h6o/G5Mg7TgeXjOMlm0bGY6wMZBoDTfJJnjOnNQlVFSpi"
  + "uc1ek5r12dxT7anZWN7v1YvXJ95d0rteOZmANS2FxkgwlIjzUpoQldOXupZwpRlBYier4EaaMX+/jVQP06fSQhnBWvOWm7Ye7jra3s+51ZaW919+zkqnV2nLvgfO40BT"
  + "9QKcPtfBiCwAAA==")
g = base64.b64decode(_g)[1:]
for i in range(base64.b64decode(_g)[0]):
    g = gzip.decompress(g)
g=list(g)
def gr(x,y):
    if(x>=0 and y>=0 and x<200 and y<57):
        return g[y*200 + x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<200 and y<57):
        g[y*200 + x]=v;
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
    return (6)if(sp()!=0)else(7)
def _1():
    return (19)if(sp()!=0)else(8)
def _2():
    return (11)if(sp()!=0)else(21)
def _3():
    return (17)if(sp()!=0)else(22)
def _4():
    gw(1,0,200)
    gw(2,0,50)
    gw(4,0,10000)
    gw(3,0,2)
    return 5
def _5():
    gw(0,1,32)
    gw(1,1,32)
    gw(8,0,1073741824)
    gw(tm(gr(3,0),gr(1,0)),(td(gr(3,0),gr(1,0)))+(1),88)
    sa((gr(3,0))+(gr(3,0)))
    sa((1)if((gr(4,0))>((gr(3,0))+(gr(3,0))))else(0))
    return 0
def _6():
    sa(sr())
    sa(32)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(sr())
    sa(gr(1,0))
    v0=sp()
    sa(tm(sp(),v0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(gr(1,0))
    v0=sp()
    sa(td(sp(),v0))
    sa(1)
    sa(sp()+sp());
    v0=sp()
    v1=sp()
    gw(v1,v0,sp())
    sa(gr(3,0))
    sa(sp()+sp());
    sa(sr())
    sa(gr(4,0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return 0
def _7():
    sp()
    return 8
def _8():
    sa((gr(3,0))+(1))
    gw(3,0,(gr(3,0))+(1))
    sa(sr())
    sa(gr(1,0))
    v0=sp()
    sa(tm(sp(),v0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(gr(1,0))
    v0=sp()
    sa(td(sp(),v0))
    sa(1)
    sa(sp()+sp());
    v0=sp()
    sa(gr(sp(),v0))
    sa(32)
    v0=sp()
    sa(sp()-v0)
    return 1
def _9():
    gw(3,0,0)
    gw(5,0,3)
    return 20
def _10():
    sp()
    sa(3)
    sa((0)if(((3)-(gr(5,0)))!=0)else(1))
    return 2
def _11():
    print(sp(),end="",flush=True)
    return 26
def _12():
    sa(1)
    sa(sp()+sp());
    sa(sr())
    sa(gr(5,0))
    v0=sp()
    sa(sp()-v0)
    sa((0)if(sp()!=0)else(1))
    return 2
def _13():
    sa(sr())
    sa(gr(5,0))
    gw(9,0,0)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa(sp()-v0)
    sa(2)
    v0=sp()
    sa(td(sp(),v0))
    sa(sr())
    gw(7,0,sp())
    sa(gr(8,0))
    sa((1)if((gr(8,0))>(gr(7,0)))else(0))
    return 3
def _14():
    sa(1)
    sa(sp()+sp());
    sa(sr())
    sa(gr(5,0))
    v0=sp()
    sa(sp()-v0)
    sa((0)if(sp()!=0)else(1))
    return 2
def _15():
    sp()
    return 20
def _16():
    sa(sr())
    sa(gr(9,0))
    sa(sp()+sp());
    sa(gr(7,0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa(sp()-v0)
    gw(7,0,sp())
    sa(sr())
    sa(2)
    sa(sp()*sp());
    sa(gr(9,0))
    sa(sp()+sp());
    gw(9,0,sp())
    gw(9,0,td(gr(9,0),2))
    sa(4)
    v0=sp()
    sa(td(sp(),v0))
    return 22
def _17():
    sa(4)
    v0=sp()
    sa(td(sp(),v0))
    sa(sr())
    sa(gr(7,0))
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return 3
def _18():
    sa(79)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(sr())
    sa(gr(1,0))
    v0=sp()
    sa(tm(sp(),v0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(gr(1,0))
    v0=sp()
    sa(td(sp(),v0))
    sa(1)
    sa(sp()+sp());
    v0=sp()
    v1=sp()
    gw(v1,v0,sp())
    return 20
def _19():
    sa((1)if((gr(4,0))>(gr(3,0)))else(0))
    return (5)if(sp()!=0)else(9)
def _20():
    sa((gr(5,0))+(2))
    gw(5,0,(gr(5,0))+(2))
    sa(sr())
    sa(sr())
    sa(gr(1,0))
    v0=sp()
    sa(tm(sp(),v0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(gr(1,0))
    v0=sp()
    sa(td(sp(),v0))
    sa(1)
    sa(sp()+sp());
    v0=sp()
    sa(gr(sp(),v0))
    sa(32)
    v0=sp()
    sa(sp()-v0)
    return (18)if(sp()!=0)else(10)
def _21():
    sa(sr())
    sa(sr())
    sa(gr(1,0))
    v0=sp()
    sa(tm(sp(),v0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(gr(1,0))
    v0=sp()
    sa(td(sp(),v0))
    sa(1)
    sa(sp()+sp());
    v0=sp()
    sa(gr(sp(),v0))
    sa(32)
    v0=sp()
    sa(sp()-v0)
    sa((0)if(sp()!=0)else(1))
    return (12)if(sp()!=0)else(13)
def _22():
    sa(sr())
    return (24)if(sp()!=0)else(23)
def _23():
    sp()
    sa((gr(9,0))*(gr(9,0)))
    v0=sp()
    sa(sp()-v0)
    return (14)if(sp()!=0)else(15)
def _24():
    sa(sr())
    sa(gr(9,0))
    sa(sp()+sp());
    sa(gr(7,0))
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    sa((0)if(sp()!=0)else(1))
    return (16)if(sp()!=0)else(25)
def _25():
    gw(9,0,td(gr(9,0),2))
    sa(4)
    v0=sp()
    sa(td(sp(),v0))
    sa(sr())
    return (24)if(sp()!=0)else(23)
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17,_18,_19,_20,_21,_22,_23,_24,_25]
c=4
while c<26:
    c=m[c]()