# compiled with BefunCompile v1.0.1 (c) 2015
# execute with at least Python3
from random import randint
g=[[49,58,48,49,48,58,112,112,53,53,53,56,42,42,42,48,52,112,62,49,48,103,49,43,58,58,49,48,112,48,52,103,45,48,48,103,32,92,35,118,95,49,43,58,48,48,112,92,36,49,58,49,48,112,92,58,48,52,103,45,32,35,118,95,36,36,48,51,103,46,64],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,118,32,36,60,32,32,32,32,32,32,32,62,49,35,32,48,35,32,49,35,32,112,35,32,42,35,32,58,35,32,118,35,32,32,60,32,32,32,32,32,32,32,32],[32,32,32,118,95,118,35,45,103,49,45,103,50,48,103,49,48,103,32,49,103,50,48,60,112,50,48,49,60,118,95,94,35,58,47,43,53,53,112,49,48,43,49,103,49,48,112,49,103,49,48,37,43,53,53,58,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,36,32,62,48,50,103,49,43,58,48,50,112,32,48,49,32,103,32,45,32,124,32,32,32,32,32,62,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,62,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,62,58,48,51,103,92,96,35,118,95,48,51,112,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,36,60,32,32,32,48,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32]];
def gr(x,y):
    if(x>=0 and y>=0 and x<71 and y<6):
        return g[y][x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<71 and y<6):
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
    return (8)if(sp()!=0)else(16)
def _1():
    return (9)if(sp()!=0)else(10)
def _2():
    return (5)if(sp()!=0)else(12)
def _3():
    return (14)if(sp()!=0)else(13)
def _4():
    return (8)if(sp()!=0)else(17)
def _5():
    return (15)if((gr(gr(0,2),1))-(gr((gr(0,1))-(gr(0,2)),1)))else(11)
def _6():
    gw(0,0,1)
    gw(1,0,1)
    gw(0,4,1000)
    return 7
def _7():
    sa((gr(1,0))+(1))
    sa((gr(1,0))+(1))
    gw(1,0,(gr(1,0))+(1))
    sa(gr(0,4))
    v0=sp()
    sa(sp()-v0)
    sa(gr(0,0))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    return 0
def _8():
    gw(0,1,1)
    sa(sp()*sp());
    sa(sr())
    return 9
def _9():
    sa(sr())
    sa(10)
    v0=sp()
    sa(tm(sp(),v0))
    gw(gr(0,1),1,sp())
    gw(0,1,(gr(0,1))+(1))
    sa(10)
    v0=sp()
    sa(td(sp(),v0))
    sa(sr())
    return 1
def _10():
    gw(0,2,1)
    sp()
    return 5
def _11():
    sa((gr(0,2))+(1))
    gw(0,2,(gr(0,2))+(1))
    sa(gr(0,1))
    v0=sp()
    sa(sp()-v0)
    return 2
def _12():
    sa(sr())
    sa(gr(0,3))
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa((1)if(sp()>v0)else(0))
    return 3
def _13():
    gw(0,3,sp())
    return 7
def _14():
    sp()
    return 7
def _15():
    sp()
    return 7
def _16():
    sa(1)
    sa(sp()+sp());
    sa(sr())
    gw(0,0,sp())
    gw(1,0,1)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sp()
    sa(1)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    sa(sr())
    sa(gr(0,4))
    v0=sp()
    sa(sp()-v0)
    return 4
def _17():
    sp()
    sp()
    print(gr(0,3),end="",flush=True)
    return 18
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17]
c=6
while c<18:
    c=m[c]()