# compiled with BefunCompile v1.0.1 (c) 2015
# execute with at least Python3
from random import randint
def gr(x,y):
    if(x>=0 and y>=0 and x<109 and y<5164):
        return g[y][x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<109 and y<5164):
        g[y][x]=v;
def rd():
    return bool(random.getrandbits(1))
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
    return (29)if(sp()!=0)else(11)
def _1():
    return (28)if(sp()!=0)else(13)
def _2():
    return (14)if(sp()!=0)else(10)
def _3():
    return (17)if(sp()!=0)else(21)
def _4():
    return (19)if(sp()!=0)else(20)
def _5():
    return (16)if(sp()!=0)else(22)
def _6():
    return (15)if(sp()!=0)else(23)
def _7():
    return (27)if(sp()!=0)else(25)
def _8():
    return (24)if(sp()!=0)else(26)
def _9():
    gw(2,0,5163)
    gw(0,0,5163)
    return 10
def _10():
    gw(1,0,0)
    sa(0)
    sa((gr(0,gr(0,0)))-(64))
    sa((1)if(((gr(0,gr(0,0)))-(64))>(0))else(0))
    return 0
def _11():
    gw(1,0,(0)+((gr(1,0))*(28)))
    sp()
    return 12
def _12():
    sa(1)
    sa(sp()+sp());
    sa(sr())
    sa(12)
    v0=sp()
    sa(sp()-v0)
    return 1
def _13():
    gw(0,gr(0,0),gr(1,0))
    sp()
    sa((gr(0,0))-(1))
    gw(0,0,(gr(0,0))-(1))
    sa((0)if(sp()!=0)else(1))
    return 2
def _14():
    gw(3,0,gr(2,0))
    return 15
def _15():
    gw(4,0,0)
    return 16
def _16():
    sa((1)if((gr(0,(gr(4,0))+(1)))>(gr(0,(gr(4,0))+(2))))else(0))
    return 3
def _17():
    sa(gr(4,0))
    gw(6,0,(gr(4,0))+(1))
    gw(7,0,sp())
    gw(8,0,12)
    sa(gr(12,(gr(6,0))+(1)))
    gw(gr(8,0),(gr(6,0))+(1),gr(12,(gr(7,0))+(1)))
    return 18
def _18():
    gw(gr(8,0),(gr(7,0))+(1),sp())
    sa(gr(8,0))
    sa((gr(8,0))-(1))
    gw(8,0,(gr(8,0))-(1))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    return 4
def _19():
    sa(sr())
    sa((gr(6,0))+(1))
    v0=sp()
    sa(gr(sp(),v0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa((gr(7,0))+(1))
    v0=sp()
    sa(gr(sp(),v0))
    gw(gr(8,0),(gr(6,0))+(1),sp())
    return 18
def _20():
    sp()
    return 21
def _21():
    sa((gr(4,0))+(1))
    gw(4,0,(gr(4,0))+(1))
    sa((gr(3,0))-(1))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return 5
def _22():
    sa(gr(3,0))
    gw(3,0,(gr(3,0))-(1))
    sa(2)
    v0=sp()
    sa(sp()-v0)
    return 6
def _23():
    gw(9,0,0)
    gw(5,0,gr(2,0))
    return 24
def _24():
    sa(1)
    sa(gr(1,gr(5,0)))
    sa((gr(1,gr(5,0)))-(32))
    return 7
def _25():
    sp()
    sp()
    sp()
    sa((gr(5,0))-(1))
    gw(5,0,(gr(5,0))-(1))
    return 8
def _26():
    print(gr(9,0),end="",flush=True)
    return 30
def _27():
    sa(64)
    v0=sp()
    sa(sp()-v0)
    sa(gr(5,0))
    sa(sp()*sp());
    sa(gr(9,0))
    sa(sp()+sp());
    gw(9,0,sp())
    sa(1)
    sa(sp()+sp());
    sa(sr())
    sa(gr(5,0))
    v0=sp()
    sa(gr(sp(),v0))
    sa(sr())
    sa(32)
    v0=sp()
    sa(sp()-v0)
    return 7
def _28():
    sa(sr())
    sa(gr(0,0))
    v0=sp()
    sa(gr(sp(),v0))
    sa(64)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    sa(0)
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return 0
def _29():
    sa((gr(1,0))*(28))
    sa(sp()+sp());
    gw(1,0,sp())
    return 12
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17,_18,_19,_20,_21,_22,_23,_24,_25,_26,_27,_28,_29]
c=9
while c<30:
    c=m[c]()