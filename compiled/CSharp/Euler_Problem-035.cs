/* compiled with BefunCompile v1.0 (c) 2015 */
public static class Program 
{
private static long gr(long x,long y){return(x>=0&&y>=0&&x<2000&&y<516)?g[y, x]:0;}
private static void gw(long x,long y,long v){if(x>=0&&y>=0&&x<2000&&y<516)g[y, x]=v;}
private static System.Collections.Generic.Stack<long> s=new System.Collections.Generic.Stack<long>();
private static long sp(){ return (s.Count==0)?0:s.Pop(); }
private static void sa(long v){ s.Push(v); }
private static long sr(){ return (s.Count==0)?0:s.Peek(); }
private static readonly System.Random r = new System.Random();
private static bool rd(){ return r.Next(2)!=0; }
private static long td(long a,long b){ return (b==0)?0:(a/b); }
private static long tm(long a,long b){ return (b==0)?0:(a%b); }
static void Main(string[] args)
{
        goto _11;
    _0:
        if(sp()!=0)goto _13; else goto _14;
    _1:
        if(sp()!=0)goto _16; else goto _15;
    _2:
        if(sp()!=0)goto _12; else goto _17;
    _3:
        if(sp()!=0)goto _31; else goto _19;
    _4:
        if(sp()!=0)goto _24; else goto _18;
    _5:
        if(sp()!=0)goto _27; else goto _20;
    _6:
        if(sp()!=0)goto _29; else goto _22;
    _7:
        if(sp()!=0)goto _28; else goto _30;
    _8:
        if(sp()!=0)goto _21; else goto _25;
    _9:
        if(sp()!=0)goto _21; else goto _26;
    _10:
        if(sp()!=0)goto _20; else goto _27;
    _11:
        gw(1,0,2000);
        gw(2,0,500);
        gw(0,0,1000000);
        gw(3,0,2);
        gw(0,3,32);
        gw(1,3,32);
        goto _12;
    _12:
        gw(tm(gr(3,0),gr(1,0)),((td(gr(3,0),gr(1,0)))+(3)),88);
        sa(((gr(3,0))+(gr(3,0))));
        sa((((gr(0,0))>(((gr(3,0))+(gr(3,0)))))?1:0));
        goto _0;
    _13:
        sa(sr());
        sa(32);
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(sr());
        sa(gr(1,0));
        {long v0=sp();sa((v0==0)?0:(sp()%v0));}
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(gr(1,0));
        {long v0=sp();sa((v0==0)?0:(sp()/v0));}
        sa(3);
        sa(sp()+sp());
        {long v0=sp();long v1=sp();gw(v1,v0,sp());}
        sa(gr(3,0));
        sa(sp()+sp());
        sa(sr());
        sa(gr(0,0));
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        {long v0=sp();sa((sp()>v0)?1:0);}
        goto _0;
    _14:
        sp();
        goto _15;
    _15:
        sa(((gr(3,0))+(1)));
        gw(3,0,((gr(3,0))+(1)));
        sa(sr());
        sa(gr(1,0));
        {long v0=sp();sa((v0==0)?0:(sp()%v0));}
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(gr(1,0));
        {long v0=sp();sa((v0==0)?0:(sp()/v0));}
        sa(3);
        sa(sp()+sp());
        {long v0=sp();sa(gr(sp(),v0));}
        sa(32);
        {long v0=sp();sa(sp()-v0);}
        goto _1;
    _16:
        sa((((gr(0,0))>(gr(3,0)))?1:0));
        goto _2;
    _17:
        gw(9,0,0);
        gw(3,0,2);
        goto _18;
    _18:
        sa(gr(3,0));
        sa(((gr(tm(gr(3,0),gr(1,0)),((td(gr(3,0),gr(1,0)))+(3))))-(88)));
        goto _3;
    _19:
        gw(5,0,1);
        sa(sr());
        sa(1);
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(10);
        {long v0=sp();sa((v0==0)?0:(sp()/v0));}
        sa(sr());
        sa((sp()!=0)?0:1);
        goto _5;
    _20:
        sa(sr());
        sa(2);
        {long v0=sp();sa((v0==0)?0:(sp()%v0));}
        sa((sp()!=0)?0:1);
        goto _8;
    _21:
        sp();
        sp();
        goto _22;
    _22:
        sp();
        goto _23;
    _23:
        sa(((gr(3,0))+(1)));
        gw(3,0,((gr(3,0))+(1)));
        sa(gr(0,0));
        {long v0=sp();sa(sp()-v0);}
        sa((sp()!=0)?0:1);
        goto _4;
    _24:
        sa(gr(9,0));
        sa(61);
        System.Console.Out.WriteLine((char)(32));
        System.Console.Out.WriteLine((char)(sp()));
        System.Console.Out.WriteLine((long)(sp()));
        return;
    _25:
        sa(sr());
        sa(5);
        {long v0=sp();sa((v0==0)?0:(sp()%v0));}
        sa((sp()!=0)?0:1);
        goto _9;
    _26:
        gw(5,0,((gr(5,0))+(1)));
        sa(10);
        {long v0=sp();sa((v0==0)?0:(sp()/v0));}
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(10);
        sa(sp()*sp());
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(sr());
        goto _10;
    _27:
        sp();
        gw(6,0,sp());
        sa(sr());
        gw(7,0,sp());
        goto _28;
    _28:
        sa(sr());
        sa(sr());
        sa(gr(1,0));
        {long v0=sp();sa((v0==0)?0:(sp()%v0));}
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(gr(1,0));
        {long v0=sp();sa((v0==0)?0:(sp()/v0));}
        sa(3);
        sa(sp()+sp());
        {long v0=sp();sa(gr(sp(),v0));}
        sa(32);
        {long v0=sp();sa(sp()-v0);}
        goto _6;
    _29:
        sa(sr());
        sa(10);
        {long v0=sp();sa((v0==0)?0:(sp()/v0));}
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(10);
        {long v0=sp();sa((v0==0)?0:(sp()%v0));}
        sa(gr(6,0));
        sa(sp()*sp());
        sa(sp()+sp());
        sa(((gr(5,0))-(1)));
        gw(5,0,((gr(5,0))-(1)));
        goto _7;
    _30:
        sa(10);
        System.Console.Out.WriteLine((long)(gr(7,0)));
        gw(9,0,((gr(9,0))+(1)));
        System.Console.Out.WriteLine((char)(sp()));
        goto _22;
    _31:
        sp();
        goto _23;
}}