# compiled with BefunCompile v1.0.1 (c) 2015
# execute with at least Python3
from random import randint
g=[[36,36,62,53,51,42,32,48,48,112,48,48,103,49,45,50,48,112,48,49,48,112,62,49,48,103,51,42,58,50,48,103,49,43,103,34,48,34,45,53,53,43,42,92,49,43,50,48,103,49,43,103,34,48,34,45,43,49,48,103,50,48,103,49,43,112,49,48,103,49,43,58,49,48,112,50,48,103,45,49,45,35,118,95,50,48,103,58,49,45,50,48,112,48,49,48,112,35,118,95,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[55,53,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[57,53,32,54,52,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[49,55,32,52,55,32,56,50,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,32,36,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[49,56,32,51,53,32,56,55,32,49,48,32,32,32,32,32,32,32,32,32,32,32,62,48,48,103,50,45,58,49,48,112,50,48,112,62,49,48,103,50,48,103,49,43,103,49,48,103,50,48,103,50,43,103,58,49,48,103,49,43,50,48,103,50,43,103,32,45,58,48,96,62,35,94,95,45,62,43,49,48,103,50,48,103,49,43,112,49,48,103,58,49,45,49,48,112,35,118,95,50,48,103,58,49,45,58,50,48,112,49,48,112,35,118,95,48,49,103,46,64],[50,48,32,48,52,32,56,50,32,52,55,32,54,53,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32],[49,57,32,48,49,32,50,51,32,55,53,32,48,51,32,51,52,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[56,56,32,48,50,32,55,55,32,55,51,32,48,55,32,54,51,32,54,55,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[57,57,32,54,53,32,48,52,32,50,56,32,48,54,32,49,54,32,55,48,32,57,50,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[52,49,32,52,49,32,50,54,32,53,54,32,56,51,32,52,48,32,56,48,32,55,48,32,51,51,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[52,49,32,52,56,32,55,50,32,51,51,32,52,55,32,51,50,32,51,55,32,49,54,32,57,52,32,50,57,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[53,51,32,55,49,32,52,52,32,54,53,32,50,53,32,52,51,32,57,49,32,53,50,32,57,55,32,53,49,32,49,52,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[55,48,32,49,49,32,51,51,32,50,56,32,55,55,32,55,51,32,49,55,32,55,56,32,51,57,32,54,56,32,49,55,32,53,55,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[57,49,32,55,49,32,53,50,32,51,56,32,49,55,32,49,52,32,57,49,32,52,51,32,53,56,32,53,48,32,50,55,32,50,57,32,52,56,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[54,51,32,54,54,32,48,52,32,54,56,32,56,57,32,53,51,32,54,55,32,51,48,32,55,51,32,49,54,32,54,57,32,56,55,32,52,48,32,51,49,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32],[48,52,32,54,50,32,57,56,32,50,55,32,50,51,32,48,57,32,55,48,32,57,56,32,55,51,32,57,51,32,51,56,32,53,51,32,54,48,32,48,52,32,50,51,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32]];
def gr(x,y):
    if(x>=0 and y>=0 and x<120 and y<16):
        return g[y][x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<120 and y<16):
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
    return (16)if(sp()!=0)else(7)
def _1():
    return (15)if(sp()!=0)else(8)
def _2():
    return (9)if(sp()!=0)else(12)
def _3():
    return (9)if(sp()!=0)else(13)
def _4():
    return (14)if((1)if(((gr(gr(1,0),(gr(2,0))+(2)))-(gr((gr(1,0))+(1),(gr(2,0))+(2))))>(0))else(0))else(10)
def _5():
    gw(0,0,15)
    gw(2,0,(gr(0,0))-(1))
    gw(1,0,0)
    gw(gr(1,0),(gr(2,0))+(1),(((gr((gr(1,0))*(3),(gr(2,0))+(1)))-(48))*(10))+((gr(((gr(1,0))*(3))+(1),(gr(2,0))+(1)))-(48)))
    sp()
    sp()
    return 6
def _6():
    sa((gr(1,0))+(1))
    gw(1,0,(gr(1,0))+(1))
    sa(gr(2,0))
    v0=sp()
    sa(sp()-v0)
    sa(1)
    v0=sp()
    sa(sp()-v0)
    return 0
def _7():
    sa(gr(2,0))
    gw(2,0,(gr(2,0))-(1))
    gw(1,0,0)
    return 1
def _8():
    sa((gr(0,0))-(2))
    gw(1,0,(gr(0,0))-(2))
    gw(2,0,sp())
    return 9
def _9():
    sa(gr(gr(1,0),(gr(2,0))+(1)))
    sa(gr(gr(1,0),(gr(2,0))+(2)))
    sa((gr(gr(1,0),(gr(2,0))+(2)))-(gr((gr(1,0))+(1),(gr(2,0))+(2))))
    return 4
def _10():
    v0=sp()
    sa(sp()-v0)
    return 11
def _11():
    sa(sp()+sp());
    gw(gr(1,0),(gr(2,0))+(1),sp())
    sa(gr(1,0))
    gw(1,0,(gr(1,0))-(1))
    return 2
def _12():
    sa(gr(2,0))
    sa((gr(2,0))-(1))
    gw(2,0,(gr(2,0))-(1))
    gw(1,0,sp())
    return 3
def _13():
    print(gr(0,1),end="",flush=True)
    return 17
def _14():
    sp()
    return 11
def _15():
    gw(gr(1,0),(gr(2,0))+(1),(((gr((gr(1,0))*(3),(gr(2,0))+(1)))-(48))*(10))+((gr(((gr(1,0))*(3))+(1),(gr(2,0))+(1)))-(48)))
    return 6
def _16():
    gw(gr(1,0),(gr(2,0))+(1),(((gr((gr(1,0))*(3),(gr(2,0))+(1)))-(48))*(10))+((gr(((gr(1,0))*(3))+(1),(gr(2,0))+(1)))-(48)))
    return 6
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16]
c=5
while c<17:
    c=m[c]()