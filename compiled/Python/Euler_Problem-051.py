# compiled with BefunCompile v1.0.5 (c) 2015
# execute with at least Python3
import gzip, base64
_g = ("AR+LCAAAAAAABACNVMuO6yAM/RUmJJsibsHNqwh55g/6A1E60l2wzYpV7r9fmzTNoxl1rKhKiX045hyT/c0MDGIXUaCBYJVz/BGKDxnvVfq9WBjQpm/0Bs1J86oBGCKK"
  + "KDcxo6Eco9SnNvuXBTCeVvLVXv1+cy/QSjMKcbvdRHputCqX/C9JkPM/yQVT2VH4/t5LbzGKY26/C4TUMXV50R89ULW1xhgrP1MsaPgbtH3HXlhjj9AYr49QiiGAVU2n"
  + "MpMVqqoClA6ld1MOC0CKTREUcSOsQzQGDFWlziWJuKM0agIPtI8T2voBSpKqZnKp0R/QlvoVwwDgHmJIlDla7RpFlokhCGHsrlNsIbR65OyvtwdX+9F1iajwGTDartPJ"
  + "WNhA+LM5ZcxfwTCXng7jRAeqopnQ1p3GAa7UywCtJeB7lOL7DAEqR44qOnrxIvJqASSEjwln+vGZJjRu9ZXbI9xCjYmSn3vJkl6KpCROYPGZkST9EQ1BVxA6mtD+XivX"
  + "u2aA6j7PBm9Ao+qWCUmSLmh4ZXtfaYYf31NfM1OmVQL7pqCTV11DmaFUQwkP1+0ma9R0bFfaDGu6RNhqVmi6LUKgclL6xf5ktjO7+nCCMeWnmpwTYp2v8tARlw2rHXpc"
  + "68ZibYTzOLmTSyNG8S7aDXQisBLOidmdSnhVvUUDov8ULu6FU2Tap6P692hIErbzVb71e8/Pyp/q+K5cx3+VQY0mGAYAAA==")
g = base64.b64decode(_g)[1:]
for i in range(base64.b64decode(_g)[0]):
    g = gzip.decompress(g)
g=list(g)
def gr(x,y):
    if(x>=0 and y>=0 and x<78 and y<20):
        return g[y*78 + x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<78 and y<20):
        g[y*78 + x]=v;
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
    gw(0,2,99)
    return 1
def _1():
    return (2)if(gr(0,2)-1000)else(48)
def _2():
    sa(gr(0,2)+1)
    sa(gr(0,2)+1)
    gw(0,2,gr(0,2)+1)
    sa(2)
    v0=sp()
    sa(tm(sp(),v0))
    sa((0)if(sp()!=0)else(1))
    return (47)if(sp()!=0)else(3)
def _3():
    sa(5)
    v0=sp()
    sa(tm(sp(),v0))
    sa((0)if(sp()!=0)else(1))
    return (1)if(sp()!=0)else(4)
def _4():
    gw(1,2,3)
    return 5
def _5():
    sa(gr(1,2)+1)
    gw(1,2,gr(1,2)+1)
    sa(14)
    v0=sp()
    sa(sp()-v0)
    sa((0)if(sp()!=0)else(1))
    return (1)if(sp()!=0)else(6)
def _6():
    gw(2,2,0)
    return (8)if((gr(0,gr(1,2))-48)+gr(2,2))else(7)
def _7():
    sa(gr(2,2)+1)
    gw(2,2,gr(2,2)+1)
    sa(3)
    v0=sp()
    sa(sp()-v0)
    sa((0)if(sp()!=0)else(1))
    return (5)if(sp()!=0)else(8)
def _8():
    gw(4,2,gr(0,2))
    sa(5)
    sa(gr(5,gr(1,2))-48)
    return 9
def _9():
    return (10)if(sp()!=0)else(46)
def _10():
    sa(sr())
    sa((tm(gr(4,2),10))+48)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(7)
    sa(sp()+sp());
    sa(gr(1,2))
    v0=sp()
    v1=sp()
    gw(v1,v0,sp())
    gw(4,2,td(gr(4,2),10))
    return 11
def _11():
    sa(sr())
    sa((0)if(sp()!=0)else(1))
    return (12)if(sp()!=0)else(45)
def _12():
    sp()
    sa(gr(12,gr(1,2))-48)
    sa(5)
    sa(5)
    return 13
def _13():
    return (44)if(sp()!=0)else(14)
def _14():
    sp()
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(sr())
    gw(7,2,sp())
    sa(sr())
    sa(2)
    v0=sp()
    sa(tm(sp(),v0))
    return (15)if(sp()!=0)else(21)
def _15():
    sa(sr())
    sa(3)
    v0=sp()
    sa(tm(sp(),v0))
    return (16)if(sp()!=0)else(21)
def _16():
    gw(5,2,sp())
    sa(7)
    sa(tm(gr(5,2),7))
    return 17
def _17():
    return (18)if(sp()!=0)else(21)
def _18():
    sa(sr())
    sa(td(gr(5,2),2))
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return (22)if(sp()!=0)else(19)
def _19():
    sa(sr())
    sa(2)
    v0=sp()
    sa(sp()-v0)
    sa(gr(5,2))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa(tm(sp(),v0))
    sa((0)if(sp()!=0)else(1))
    return (21)if(sp()!=0)else(20)
def _20():
    sa(6)
    sa(sp()+sp());
    sa(sr())
    sa(gr(5,2))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa(tm(sp(),v0))
    return 17
def _21():
    sp()
    return 7
def _22():
    gw(8,2,1)
    gw(9,2,gr(2,2))
    gw(9,2,gr(9,2)+1)
    gw(4,2,gr(0,2))
    sp()
    return 23
def _23():
    sa(5)
    sa(gr(5,gr(1,2))-48)
    return 24
def _24():
    return (25)if(sp()!=0)else(43)
def _25():
    sa(sr())
    sa((tm(gr(4,2),10))+48)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(7)
    sa(sp()+sp());
    sa(gr(9,2)+4)
    v0=sp()
    v1=sp()
    gw(v1,v0,sp())
    gw(4,2,td(gr(4,2),10))
    return 26
def _26():
    sa(sr())
    return (42)if(sp()!=0)else(27)
def _27():
    sp()
    sa(gr(12,gr(9,2)+4)-48)
    sa(5)
    sa(5)
    return 28
def _28():
    return (41)if(sp()!=0)else(29)
def _29():
    sp()
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(10)
    sa(sp()*sp());
    sa(sp()+sp());
    sa(sr())
    sa(2)
    v0=sp()
    sa(tm(sp(),v0))
    return (34)if(sp()!=0)else(30)
def _30():
    sp()
    sa(gr(9,2)-9)
    return (33)if(sp()!=0)else(31)
def _31():
    sa(gr(8,2)-8)
    return (7)if(sp()!=0)else(32)
def _32():
    print(gr(7,2),end="",flush=True)
    return 49
def _33():
    gw(9,2,gr(9,2)+1)
    gw(4,2,gr(0,2))
    return 23
def _34():
    sa(sr())
    sa(3)
    v0=sp()
    sa(tm(sp(),v0))
    return (35)if(sp()!=0)else(30)
def _35():
    gw(5,2,sp())
    sa(7)
    sa(tm(gr(5,2),7))
    return 36
def _36():
    return (37)if(sp()!=0)else(30)
def _37():
    sa(sr())
    sa(td(gr(5,2),2))
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return (40)if(sp()!=0)else(38)
def _38():
    sa(sr())
    sa(2)
    v0=sp()
    sa(sp()-v0)
    sa(gr(5,2))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa(tm(sp(),v0))
    sa((0)if(sp()!=0)else(1))
    return (30)if(sp()!=0)else(39)
def _39():
    sa(6)
    sa(sp()+sp());
    sa(sr())
    sa(gr(5,2))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa(tm(sp(),v0))
    return 36
def _40():
    gw(8,2,gr(8,2)+1)
    return 30
def _41():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    sa(7)
    sa(sp()+sp());
    sa(gr(9,2)+4)
    v0=sp()
    sa(gr(sp(),v0))
    sa(48)
    v0=sp()
    sa(sp()-v0)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(sr())
    return 28
def _42():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    sa(gr(1,2))
    v0=sp()
    sa(gr(sp(),v0))
    sa(48)
    v0=sp()
    sa(sp()-v0)
    return 24
def _43():
    sa(sr())
    sa(gr(9,2)+48)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(7)
    sa(sp()+sp());
    sa(gr(9,2)+4)
    v0=sp()
    v1=sp()
    gw(v1,v0,sp())
    return 26
def _44():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    sa(7)
    sa(sp()+sp());
    sa(gr(1,2))
    v0=sp()
    sa(gr(sp(),v0))
    sa(48)
    v0=sp()
    sa(sp()-v0)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(sr())
    return 13
def _45():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    sa(gr(1,2))
    v0=sp()
    sa(gr(sp(),v0))
    sa(48)
    v0=sp()
    sa(sp()-v0)
    return 9
def _46():
    sa(sr())
    sa(gr(2,2)+48)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(7)
    sa(sp()+sp());
    sa(gr(1,2))
    v0=sp()
    v1=sp()
    gw(v1,v0,sp())
    return 11
def _47():
    sp()
    return 1
def _48():
    return 49
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17,_18,_19,_20,_21,_22,_23,_24,_25,_26,_27,_28,_29,_30,_31,_32,_33,_34,_35,_36,_37,_38,_39,_40,_41,_42,_43,_44,_45,_46,_47,_48]
c=0
while c<49:
    c=m[c]()