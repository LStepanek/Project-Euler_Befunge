# compiled with BefunCompile v1.0.4 (c) 2015
# execute with at least Python3
import gzip, base64
_g = ("AR+LCAAAAAAABAC9jz0KAjEQha+SnZhmh5hMhogECbZeYrcR0qZK6dkddxVEEGOzrxjmD977mt9AbQMPynCFTDYNus3Jc/XEFW4XwMA1By5yNoRr4wp4sJ7LSFwwxYjm"
  + "cFRNdWla6k5/rOdJD5VDslQ4VCaHMVYnZjIimWcznvpMVuUFgAUm84uA3whQKRkTWXnpjf9N5/2D4NfXX/HVHUV2dgFeAgAA")
g = base64.b64decode(_g)[1:]
for i in range(base64.b64decode(_g)[0]):
    g = gzip.decompress(g)
g=list(g)
def gr(x,y):
    if(x>=0 and y>=0 and x<101 and y<6):
        return g[y*101 + x];
    return 0;
def gw(x,y,v):
    if(x>=0 and y>=0 and x<101 and y<6):
        g[y*101 + x]=v;
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
    return (3)if(sp()!=0)else(6)
def _1():
    return (8)if(sp()!=0)else(7)
def _2():
    sa(99)
    sa(0)
    return 0
def _3():
    gw(3,3,199)
    sp()
    sa((0)+((gr((tm(gr(3,3),100))+(1),td(gr(3,3),100)))-(48)))
    return 9
def _4():
    sa((gr((tm(gr(3,3),100))+(1),td(gr(3,3),100)))-(48))
    sa(sp()+sp());
    return 9
def _5():
    print(sp(),end="",flush=True)
    return 10
def _6():
    sa(sr())
    gw(0,3,sp())
    gw(1,3,0)
    gw(2,3,199)
    return 7
def _7():
    sa((((gr((tm(gr(2,3),100))+(1),td(gr(2,3),100)))-(48))*(gr(0,3)))+(gr(1,3)))
    gw((tm(gr(2,3),100))+(1),td(gr(2,3),100),(tm((((gr((tm(gr(2,3),100))+(1),td(gr(2,3),100)))-(48))*(gr(0,3)))+(gr(1,3)),10))+(48))
    sa(10)
    v0=sp()
    sa(td(sp(),v0))
    gw(1,3,sp())
    sa((gr(2,3))-(1))
    gw(2,3,(gr(2,3))-(1))
    sa((0)if(sp()!=0)else(1))
    return 1
def _8():
    sa(1)
    v0=sp()
    sa(sp()-v0)
    sa(sr())
    sa((0)if(sp()!=0)else(1))
    return 0
def _9():
    sa(gr(3,3))
    gw(3,3,(gr(3,3))-(1))
    sa((0)if(sp()!=0)else(1))
    return (5)if(sp()!=0)else(4)
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9]
c=2
while c<10:
    c=m[c]()