/* transpiled with BefunCompile v1.1.0 (c) 2015 */
class Program{
private long td(long a,long b){return(b==0)?0:(a/b);}
private long tm(long a,long b){return(b==0)?0:(a%b);}
private final static java.util.Stack<Long> s=new java.util.Stack<Long>();
private long sp(){return(s.size()==0)?0:s.pop();}
private void sa(long v){s.push(v);}
private long sr(){return(s.size()==0)?0:s.peek();}
long t0,t1;
long x0=10000;
long x1=35;
long x2=35;
long x3=9;
long x4=35;
long x5=35;
long x6=0;
long x7=1;
private int _0(){
    sa(0);
    sa(10000);
    sa(0);
    return 1;
}
private int _1(){
    sa(x0);
    x4=0;
    x1=sr();
    return 2;
}
private int _2(){
    x2=sr();
    sa(sr());
    t0=x1;
    sa(t0);
    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    {long v0=sp();sa(td(sp(),v0));}

    t1=sp();
    sa(sp()+t1);

    sa(td(sp(),2));


    if(sr()!=x2)return 15;else return 3;
}
private int _3(){
    sp();
    sa(x2);

    if((x2*x2)!=x0)return 12;else return 4;
}
private int _4(){
    sa(0);
    return 5;
}
private int _5(){
    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    sa(sr());

    if(sp()!=0)return 11;else return 6;
}
private int _6(){
    sp();
    sa(tm(sp(),2));


    if(sp()!=0)return 8;else return 7;
}
private int _7(){
    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    sa(sp()+1L);

    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    return 8;
}
private int _8(){
    if(sr()!=2)return 10;else return 9;
}
private int _9(){
    sp();
    System.out.print(String.valueOf((long)(sp())));
    return 17;
}
private int _10(){
    x3=9;
    sa(sp()-1L);

    sa(sr());
    sa(0);
    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    x0=sp();
    x6=0;
    x7=1;
    return 1;
}
private int _11(){
    sp();
    sa(sp()+1L);
    return 5;
}
private int _12(){
    x5=sr();
    sa(sp()+x6);

    sa(td(sp(),x7));

    t0=(sr()*x7)-x6;
    x6=t0;
    return 13;
}
private int _13(){
    if(((x7-1)+x3)!=0)return 14;else return 4;
}
private int _14(){
    x7=td(x0-(x6*x6),x7);
    x3=0;
    sa(td(x5+x6,x7));
    x6=((td(x5+x6,x7))*x7)-x6;
    return 13;
}
private int _15(){
    if(sr()!=x4)return 16;else return 3;
}
private int _16(){
    x4=x2;
    return 2;
}

public void main(){
    int c=0;
    while(c<17){
    switch(c){
    case 0:c=_0();break;
    case 1:c=_1();break;
    case 2:c=_2();break;
    case 3:c=_3();break;
    case 4:c=_4();break;
    case 5:c=_5();break;
    case 6:c=_6();break;
    case 7:c=_7();break;
    case 8:c=_8();break;
    case 9:c=_9();break;
    case 10:c=_10();break;
    case 11:c=_11();break;
    case 12:c=_12();break;
    case 13:c=_13();break;
    case 14:c=_14();break;
    case 15:c=_15();break;
    case 16:c=_16();break;
}
}
}
public static void main(String[]a){new Program().main();}
}
