/* compiled with BefunCompile v1.0.1 (c) 2015 */
public static class Program 
{
private static readonly long[,] g = {{118,88,88,88,88,88,88,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{118,88,88,88,88,88,88,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{36,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{62,55,32,32,49,50,112,32,48,62,58,48,92,49,112,58,58,34,49,34,43,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,32,32,32,32,32,32,32,124,45,103,50,49,58,43,49,112,48,92,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{118,32,32,32,112,50,51,49,36,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,51,50,103,49,103,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,32,32,32,32,32,32,62,51,50,103,50,37,124,32,118,112,50,52,60,62,50,103,49,103,49,43,51,50,103,118,32,32,32,32,32,32,32,32},{62,51,50,103,58,49,103,96,124,32,32,32,32,32,62,48,32,32,32,32,94,94,51,112,48,103,50,51,112,48,60,49,32,32,32,32,32,32,32,32},{94,32,32,32,32,32,32,32,62,48,51,50,103,49,112,118,62,52,50,103,48,103,51,50,103,48,103,52,50,103,94,112,32,32,32,32,32,32,32,32},{94,112,50,51,43,49,103,50,51,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,118,112,50,51,48,60,32,32,32,32,32,32,32,32},{32,32,32,32,32,118,54,58,45,49,103,50,54,42,43,32,53,53,60,48,112,50,54,103,50,49,60,32,32,32,32,32,32,32,32,32,32,64,46,60},{32,32,32,32,32,62,50,112,48,103,34,48,34,45,43,54,50,103,124,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,36},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,35,32,32,62,58,62,51,48,50,112,118,32,62,58,48,50,103,50,45,58,42,96,32,33,124},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,36,32,32,32,32,62,33,92,50,37,32,43,124,37,112,50,48,43,49,58,103,50,48,58,60},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,96,50,58,58,60,32,36,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32}};
private static long gr(long x,long y){return(x>=0&&y>=0&&x<40&&y<17)?g[y, x]:0;}
private static void gw(long x,long y,long v){if(x>=0&&y>=0&&x<40&&y<17)g[y, x]=v;}
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
        goto _7;
    _0:
        if(sp()!=0)goto _24; else goto _8;
    _1:
        if(sp()!=0)goto _11; else goto _10;
    _2:
        if(sp()!=0)goto _12; else goto _23;
    _3:
        if(sp()!=0)goto _22; else goto _15;
    _4:
        if(sp()!=0)goto _16; else goto _21;
    _5:
        if(sp()!=0)goto _20; else goto _17;
    _6:
        if(sp()!=0)goto _16; else goto _18;
    _7:
        gw(1,2,7);
        gw(0,1,0);
        gw(0,0,49);
        sp();
        sa(1);
        sa((1)-(gr(1,2)));
        goto _0;
    _8:
        gw(3,2,1);
        sp();
        goto _9;
    _9:
        sa((gr(3,2))>(gr(gr(3,2),1))?1:0);
        goto _1;
    _10:
        gw(gr(3,2),1,0);
        gw(3,2,(gr(3,2))+(1));
        goto _9;
    _11:
        sa(tm(gr(3,2),2));
        goto _2;
    _12:
        gw(4,2,gr(gr(3,2),1));
        goto _13;
    _13:
        sa(gr(gr(4,2),0));
        gw(gr(4,2),0,gr(gr(3,2),0));
        gw(gr(3,2),0,sp());
        gw(gr(3,2),1,(gr(gr(3,2),1))+(1));
        gw(3,2,0);
        gw(6,2,gr(1,2));
        sa(0);
        goto _14;
    _14:
        sa((gr(6,2))-(1));
        gw(6,2,(gr(6,2))-(1));
        sa(0);
        {long v0=sp();sa(gr(sp(),v0));}
        sa(48);
        {long v0=sp();sa(sp()-v0);}
        sa(sp()+sp());
        sa(gr(6,2));
        goto _3;
    _15:
        gw(0,2,3);
        sa(sr());
        sa(sr());
        sa(sr());
        sa(2);
        {long v0=sp();sa((sp()>v0)?1:0);}
        sa((sp()!=0)?0:1);
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(2);
        {long v0=sp();sa((v0==0)?0:(sp()%v0));}
        sa(sp()+sp());
        goto _4;
    _16:
        sa(sr());
        sa(((gr(0,2))-(2))*((gr(0,2))-(2)));
        {long v0=sp();sa((sp()>v0)?1:0);}
        sa((sp()!=0)?0:1);
        goto _5;
    _17:
        sa(sr());
        sa(gr(0,2));
        gw(0,2,(gr(0,2))+(1));
        {long v0=sp();sa((v0==0)?0:(sp()%v0));}
        goto _6;
    _18:
        gw(3,2,(gr(3,2))+(1));
        sp();
        goto _19;
    _19:
        sp();
        goto _9;
    _20:
        sp();
        System.Console.Out.WriteLine((long)(sp()));
        return;
    _21:
        gw(3,2,(gr(3,2))+(1));
        sp();
        goto _19;
    _22:
        sa(10);
        sa(sp()*sp());
        goto _14;
    _23:
        gw(4,2,0);
        goto _13;
    _24:
        sa(sr());
        sa(0);
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(1);
        {long v0=sp();long v1=sp();gw(v1,v0,sp());}
        sa(sr());
        sa(sr());
        sa(49);
        sa(sp()+sp());
        {long v0=sp();long v1=sp();sa(v0);sa(v1);}
        sa(0);
        {long v0=sp();long v1=sp();gw(v1,v0,sp());}
        sa(1);
        sa(sp()+sp());
        sa(sr());
        sa(gr(1,2));
        {long v0=sp();sa(sp()-v0);}
        goto _0;
}}