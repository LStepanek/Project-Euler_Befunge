/* transpiled with BefunCompile v1.1.0 (c) 2015 */
class Program{
private java.io.BufferedReader ib=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));
private long td(long a,long b){return(b==0)?0:(a/b);}
private long tm(long a,long b){return(b==0)?0:(a%b);}
private final static java.util.Stack<Long> s=new java.util.Stack<Long>();
private long sp(){return(s.size()==0)?0:s.pop();}
private void sa(long v){s.push(v);}
private long sr(){return(s.size()==0)?0:s.peek();}
long t0,t1;
long x0=32;
long x1=32;
long x2=1;
private int _0(){
    sa(0);
    sa(1);
    sa(10);
    sa(100);
    sa(1000);
    sa(10000);
    sa(100000);
    sa(1000000);
    return 1;
}
private int _1(){
    x0=1;
    x1=1;
    return 2;
}
private int _2(){
    if(sr()<=(x0*9*x1))return 3;else return 9;
}
private int _3(){
    sa(sp()-1L);

    t0=(td(sr(),x0))+x1;
    sa(tm(sp(),x0));

    t1=x0;
    sa(t1);
    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    {long v0=sp();sa(sp()-v0);}

    sa(sp()-1L);

    sa(sr());

    if(sp()!=0)return 8;else return 4;
}
private int _4(){
    sa(sr());
    return 5;
}
private int _5(){
    if(sp()!=0)return 8;else return 6;
}
private int _6(){
    sp();
    t0%=10;
    t0*=x2;
    x2=t0;
    sa(sr());

    if(sp()!=0)return 1;else return 7;
}
private int _7()throws java.io.IOException{
    System.out.print(String.valueOf(x2));
    sp();
    return 10;
}
private int _8(){
    t0/=10;
    sa(sp()-1L);

    sa(sr());
    return 5;
}
private int _9(){
    t0=x0*9*x1;
    x0++;
    x1*=10;
    sa(sp()-t0);
    return 2;
}

public void main()throws java.io.IOException{
    int c=0;
    while(c<10){
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
}
}
}
public static void main(String[]a){try{new Program().main();}catch(java.io.IOException e){}}
}
