/* compiled with BefunCompile v1.0.1 (c) 2015 */
public static class Program 
{
private static readonly long[,] g = {{118,48,49,50,51,52,53,54,55,56,57,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{62,34,100,100,100,34,42,42,49,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{118,112,49,50,57,112,49,49,45,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,32,32,32,32,32,62,118,62,118,32,32,32,32,32,118,32,32,32,32,32,60,32,32,118,32,32,32,32,60,32,32,32,62,32,32,118,32,32,32,62,92,49,45,92,118,118,32,32,32,32,112,49,52,43,49,103,49,52,60},{62,50,49,103,58,49,43,124,62,124,62,50,49,103,48,92,62,58,49,45,58,35,94,95,36,62,42,92,58,35,94,95,36,58,124,32,32,62,51,49,112,32,49,52,49,112,32,62,51,49,103,52,49,103,42,49,49,103,96,33,124},{32,32,32,32,32,32,32,36,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,36,49,94,32,32,32,124,45,34,120,34,32,103,48,58,92,60,92,49,60,103,49,52,32,32,60},{32,32,32,32,32,32,32,64,32,62,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,118,62,32,32,32,32,62,49,43,92,58,124,32,32,49,32,32,32,32,32,32},{94,112,49,50,45,49,103,49,50,112,49,49,45,42,45,49,103,49,52,103,49,51,103,49,49,46,112,48,92,34,120,34,92,45,34,48,34,103,48,58,62,35,45,32,35,49,32,35,36,32,35,60,32,32,94,32,32,32,32,32,32}};
private static long gr(long x,long y){return(x>=0&&y>=0&&x<61&&y<8)?g[y, x]:0;}
private static void gw(long x,long y,long v){if(x>=0&&y>=0&&x<61&&y<8)g[y, x]=v;}
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
        goto _8;
    _0:
        if(sp()!=0)goto _11; else goto _26;
    _1:
        if(sp()!=0)goto _12; else goto _13;
    _2:
        if(sp()!=0)goto _14; else goto _15;
    _3:
        if(sp()!=0)goto _25; else goto _16;
    _4:
        if(sp()!=0)goto _18; else goto _19;
    _5:
        if(sp()!=0)goto _24; else goto _21;
    _6:
        if(sp()!=0)goto _22; else goto _23;
    _7:
        if(((gr(2,1))+(1))!=0)goto _0;else goto _10;
    _8:
        gw(1,1,999999);
        gw(2,1,9);
        goto _9;
    _9:
        sa(gr(2,1));
        goto _7;
    _10:
        sp();
        return;
    _11:
        sa(0);
        sa(gr(2,1));
        sa((gr(2,1))-(1));
        sa((gr(2,1))-(1));
        goto _1;
    _12:
        sa(sr());
        sa(1);
        {long v0=sp();sa(sp()-v0);}
        sa(sr());
        goto _1;
    _13:
        sp();
        goto _14;
    _14:
        sa(sp()*sp());
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(sr());
        goto _2;
    _15:
        sp();
        sa(sr());
        goto _3;
    _16:
        gw(3,1,1);
        gw(4,1,1);
        sp();
        goto _17;
    _17:
        sa(((((gr(3,1))*(gr(4,1)))>(gr(1,1))?1:0)!=0)?0:1);
        goto _4;
    _18:
        gw(4,1,(gr(4,1))+(1));
        goto _17;
    _19:
        sa(gr(4,1));
        goto _20;
    _20:
        sa(1);
        sa((gr(1,0))-(120));
        goto _5;
    _21:
        sa(1);
        sa(sp()+sp());
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(sr());
        goto _6;
    _22:
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(sr());
        sa(0);
        {long v0=sp();sa(gr(sp(),v0));}
        sa(120);
        {long v0=sp();sa(sp()-v0);}
        goto _5;
    _23:
        sp();
        sa(1);
        {long v0=sp();sa(sp()-v0);}
        sa(sr());
        sa(0);
        {long v0=sp();sa(gr(sp(),v0));}
        sa(48);
        {long v0=sp();sa(sp()-v0);}
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(120);
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(0);
        {long v0=sp();long v1=sp();gw(v1,v0,sp());}
        gw(1,1,(gr(1,1))-((gr(3,1))*((gr(4,1))-(1))));
        gw(2,1,(gr(2,1))-(1));
        System.Console.Out.WriteLine((long)(sp()));
        goto _9;
    _24:
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(1);
        {long v0=sp();sa(sp()-v0);}
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        goto _21;
    _25:
        gw(3,1,sp());
        gw(4,1,1);
        goto _17;
    _26:
        sa(1);
        goto _20;
}}