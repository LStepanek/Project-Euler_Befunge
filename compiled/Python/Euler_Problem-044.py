# compiled with BefunCompile v1.0.4 (c) 2015
# execute with at least Python3
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
x0=37
x1=37
x2=37
x3=37
x4=37
x5=37
x6=37
def _0():
    return (6)if(sp()!=0)else(5)
def _1():
    return (7)if(sp()!=0)else(16)
def _2():
    return (10)if(sp()!=0)else(19)
def _3():
    global x0
    global x1
    global x5
    x0=1073741824
    x1=2
    x5=5
    sa(2)
    sa(5)
    return 4
def _4():
    sa((x1)-(1))
    sa((x1)-(1))
    return 0
def _5():
    global x1
    global x5
    sp()
    sp()
    sa(sp()+(1));
    sa(sr())
    sa(sr())
    x1=sp()
    sa(sr())
    sa(sp()*(3));
    sa(sp()-(1));
    sa(sp()*sp());
    sa(td(sp(),2))
    sa(sr())
    x5=sp()
    return 4
def _6():
    global x2
    global x3
    global x6
    global x4
    global x0
    sa(sr())
    x2=sp()
    sa(sr())
    sa(sp()*(3));
    sa(sp()-(1));
    sa(sp()*sp());
    sa(td(sp(),2))
    sa(sr())
    x3=sp()
    x6=0
    v0=sp()
    sa(sp()-v0)
    sa(sp()*(24));
    sa(sp()+(1));
    sa(sr())
    x4=sp()
    sa(x0)
    sa((1)if((x0)>(x4))else(0))
    return 1
def _7():
    global x4
    sa(td(sp(),4))
    sa(sr())
    sa((1)if(sp()>(x4))else(0))
    return 1
def _8():
    global x5
    sa(x5)
    sa((x2)-(1))
    sa((x2)-(1))
    return 0
def _9():
    global x6
    global x4
    global x0
    sa((((x3)+(x5))*(24))+(1))
    sa((((x3)+(x5))*(24))+(1))
    x6=0
    x4=sp()
    sa(x0)
    sa((1)if((x0)>(x4))else(0))
    return 2
def _10():
    global x4
    sa(td(sp(),4))
    sa(sr())
    sa((1)if(sp()>(x4))else(0))
    return 2
def _11():
    sp()
    print((x5)-(x3),end="",flush=True)
    return 26
def _12():
    sp()
    return 8
def _13():
    global x6
    global x4
    global x4
    global x6
    global x6
    global x6
    sa(sr())
    sa(sp()+(x6));
    sa(x4)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa(sp()-v0)
    x4=sp()
    sa(sr())
    sa(sp()*(2));
    sa(sp()+(x6));
    x6=sp()
    x6=td(x6,2)
    sa(td(sp(),4))
    return 19
def _14():
    sp()
    return 8
def _15():
    global x6
    global x4
    global x4
    global x6
    global x6
    global x6
    sa(sr())
    sa(sp()+(x6));
    sa(x4)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    v0=sp()
    sa(sp()-v0)
    x4=sp()
    sa(sr())
    sa(sp()*(2));
    sa(sp()+(x6));
    x6=sp()
    x6=td(x6,2)
    sa(td(sp(),4))
    return 16
def _16():
    sa(sr())
    return (24)if(sp()!=0)else(17)
def _17():
    global x6
    sp()
    sa(sp()-((x6)*(x6)));
    sa(x6)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    return (14)if(sp()!=0)else(18)
def _18():
    sa(tm(sp(),6))
    sa(sp()-(5));
    sa((0)if(sp()!=0)else(1))
    return (9)if(sp()!=0)else(8)
def _19():
    sa(sr())
    return (22)if(sp()!=0)else(20)
def _20():
    global x6
    sp()
    sa(sp()-((x6)*(x6)));
    sa(x6)
    v0=sp()
    v1=sp()
    sa(v0)
    sa(v1)
    return (12)if(sp()!=0)else(21)
def _21():
    sa(tm(sp(),6))
    sa(sp()-(5));
    return (8)if(sp()!=0)else(11)
def _22():
    global x6
    global x4
    sa(sr())
    sa(sp()+(x6));
    sa((1)if(sp()>(x4))else(0))
    sa((0)if(sp()!=0)else(1))
    return (13)if(sp()!=0)else(23)
def _23():
    global x6
    x6=td(x6,2)
    sa(td(sp(),4))
    sa(sr())
    return (22)if(sp()!=0)else(20)
def _24():
    global x6
    global x4
    sa(sr())
    sa(sp()+(x6));
    sa((1)if(sp()>(x4))else(0))
    sa((0)if(sp()!=0)else(1))
    return (15)if(sp()!=0)else(25)
def _25():
    global x6
    x6=td(x6,2)
    sa(td(sp(),4))
    sa(sr())
    return (24)if(sp()!=0)else(17)
m=[_0,_1,_2,_3,_4,_5,_6,_7,_8,_9,_10,_11,_12,_13,_14,_15,_16,_17,_18,_19,_20,_21,_22,_23,_24,_25]
c=3
while c<26:
    c=m[c]()