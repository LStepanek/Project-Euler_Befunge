/* compiled with BefunCompile v1.0.5 (c) 2015 */
public static class Program 
{
private static System.Collections.Generic.Stack<long> s=new System.Collections.Generic.Stack<long>();
private static long sp(){ return (s.Count==0)?0:s.Pop(); }
private static void sa(long v){ s.Push(v); }
private static long sr(){ return (s.Count==0)?0:s.Peek(); }
private static long td(long a,long b){ return (b==0)?0:(a/b); }
private static long tm(long a,long b){ return (b==0)?0:(a%b); }
static void Main(string[] args)
{
        long x0=0;
        long x1=0;
        long x2=32;
        long x3=6;
        long x4=1000;
        long x5=0;
        x2=td(x3,3);
    _1:
        sa(x2);
        if((x2-2)!=0)goto _2;else goto _4;
    _2:
        sa(sp()-1);
        x2=sp();
        if((tm(x3*(x3-(2*x2)),(x3-x2)*2))!=0)goto _1;else goto _3;
    _3:
        x5=x5+1;
        goto _1;
    _4:
        sp();
        sa(x5);
        if(((x5)>(x0)?1:0)!=0)goto _9;else goto _5;
    _5:
        sp();
    _6:
        sa(x3);
        if((x3-x4)!=0)goto _8;else goto _7;
    _7:
        sp();
        System.Console.Out.Write((long)(x1));
        return;
    _8:
        sa(sp()+2);
        x3=sp();
        x5=0;
        x2=td(x3,3);
        goto _1;
    _9:
        x0=sp();
        x1=x3;
        goto _6;
}}