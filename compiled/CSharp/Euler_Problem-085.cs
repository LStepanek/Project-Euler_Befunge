/* transpiled with BefunCompile v1.1.0 (c) 2015 */
public static class Program
{
private static System.Collections.Generic.Stack<long> s=new System.Collections.Generic.Stack<long>();
private static long sp(){ return (s.Count==0)?0:s.Pop(); }
private static void sa(long v){ s.Push(v); }
private static long sr(){ return (s.Count==0)?0:s.Peek(); }
private static long td(long a,long b){ return (b==0)?0:(a/b); }
private static long tm(long a,long b){ return (b==0)?0:(a%b); }
static void Main(string[]args)
{
        long t0;
        long x0=2000000;
        long x1=2000000;
        long x2=0;
        long x3=89;
        long x4=0;
        long x5=89;
        long x6=89;
    _1:
        if(x0>x4)goto _3;else goto _2;
    _2:
        System.Console.Out.Write(x3);
        return;
    _3:
        x5=1;
        x6=x4;
    _4:
        if(((x2>x5?1:0)*(x0>x6?1L:0L))!=0)goto _5;else goto _12;
    _5:
        sa(x0-x6);

        if((x0-x6)<0)goto _11;else goto _6;
    _6:
        sa(sp()-0L);
    _7:
        if(sr()>x1)goto _8;else goto _10;
    _8:
        sp();
    _9:
        t0=x5+1;
        x5++;
        t0*=x4;
        t0+=x6;
        x6=t0;
        goto _4;
    _10:
        x1=sp();
        x3=x5*x2;
        goto _9;
    _11:
        t0=0;
        sa(t0);
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        {long v0=sp();sa(sp()-v0);}
        goto _7;
    _12:
        t0=x2+1;
        x2++;
        t0+=x4;
        x4=t0;
        goto _1;
}
}
