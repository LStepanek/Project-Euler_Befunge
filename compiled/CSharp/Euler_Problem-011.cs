/* compiled with BefunCompile v1.0.4 (c) 2015 */
public static class Program 
{
private static readonly string _g = "AR+LCAAAAAAABADlmM1uIzcQhF+lIWcvGjjmP4eCoAR5DsPOba466bQPv1+1tJtdIM5KCJhLiLFEzlBgTXV1NemLfd8u9kg7PjT7oXbalV16OezjcwhnO1kIYTuY37RP"+
                                    "u992y+tt8BIXO5vp8XWuPb29X5YP2zzId7T/G6ywWkiWko1uebVYiZOVoM9Ov1jgs1tfrSaLySr3u42oH34WrKe/af8eVhm6xhCU2G2NFkHQrQVbu+5wf6xWsjXmrAJa"+
                                    "m7Uk3BNhgQNYOVrPVqv1YbFYAmi2HoWpdavZ1tUyFGZNjtkyyOpMWISmw0e1lMUEJEXQJHGTGK7iJkTLSR2A5q6gA4s4ToSFqqAq+pI1ipsGN8Qr2vDla9Gc4oJLq7Vm"+
                                    "OYuwdWoQoaR0kQFPKExhquKjFEkeBEQQvYNvBV+wXCW4q/YnwgIQikZhYqIolBAWIaYpMW/aGuKMWEMVCZF9Zp8Ki1VBAA3NnaK5CyRXG9EcxfJQJzhE9AQyZS4vMFdb"+
                                    "RQlYV/kTS5KPhBKgw92B8HENIpiVocrHIuUBtKepsKJ0ozQc7p+4ZZOwIAyRSUlFN1uUzmS5RSmi/lSDgIzozoS2yDjJ3PMRuydSwTNOxpGUrYI4NBmzGFPZYjHUQwTx"+
                                    "KoKVHRa5eY0sUUvOlqAX9UXtsLWqEsx0+eaGGVRYwIR7IR2KoIAWXfhncZsl3ADF28AnlFNrYhwKEwbRXPXDbUwWv7r8kztn8zrdVaSDSx4uy1SDUOlNyv/1quiqTCSy"+
                                    "EMawutMyTH5RMRF76rI60nZmEN3BoWp1EM1Ni+SX3XudQf50oAc/UzHIquLVNxRz2SrOByHDvlNVBlCtUTcBBR+2Li91pWcvjkDHRPJUtuTvQ2tQmwHB7iXlm22yPAHl"+
                                    "6ZpuJYgE7EVvwvw4G5Z4qiJDJZmNQ9BOprttUme061ql+tU3GoCunqfk48wgRhVdVeIo1V/zv7nqtbHJwoTFsztVZrh9kLwS3EyDuJxDeI77w55KQzvHZYm1hnPw78i4"+
                                    "1ueosY+G9+GTqSGG44NHjBO/vussetLBr5b9p7yPyyudl7Jsu7B7rmm//+tZ+uHZ8vXB4+fE0y+nKx3/DOvzPdjVnNXDxsF1KS9w+7rs/tg9ytbb+9vTn1uIh+MH2L4e"+
                                    "1E+89O1MfUpJH2EbyyFsOZzjVojYjRgCK74aX2ED0dLCBnlVM7eFpxrTY8LppzMupnU4nrPi0+X921Gdg3oM26/2+/evwh9vcy99H7Yjem3LFsoW2jlUenkLdVs0FsUM"+
                                    "jm/i5UpWmPivjB/az9na7/dv/xGYb+3uBY8f8/QFUdxTbEkSAAA=";
private static readonly long[]  g = System.Array.ConvertAll(zd(System.Convert.FromBase64String(_g)),b=>(long)b);
private static byte[]zd(byte[]o){byte[]d=System.Linq.Enumerable.ToArray(System.Linq.Enumerable.Skip(o, 1));for(int i=0;i<o[0];i++)d=zs(d);return d;}
private static byte[]zs(byte[]o){using(var c=new System.IO.MemoryStream(o))
                                 using(var z=new System.IO.Compression.GZipStream(c,System.IO.Compression.CompressionMode.Decompress))
                                 using(var r=new System.IO.MemoryStream()){z.CopyTo(r);return r.ToArray();}}
private static long gr(long x,long y){return(x>=0&&y>=0&&x<151&&y<31)?g[y*151+x]:0;}
private static void gw(long x,long y,long v){if(x>=0&&y>=0&&x<151&&y<31)g[y*151+x]=v;}
private static System.Collections.Generic.Stack<long> s=new System.Collections.Generic.Stack<long>();
private static long sp(){ return (s.Count==0)?0:s.Pop(); }
private static void sa(long v){ s.Push(v); }
private static long sr(){ return (s.Count==0)?0:s.Peek(); }
private static long td(long a,long b){ return (b==0)?0:(a/b); }
private static long tm(long a,long b){ return (b==0)?0:(a%b); }
static void Main(string[] args)
{
        goto _3;
    _0:
        if(sp()!=0)goto _4; else goto _5;
    _1:
        if(sp()!=0)goto _6; else goto _7;
    _2:
        if(sp()!=0)goto _8; else goto _14;
    _3:
        gw(0,0,675);
        goto _4;
    _4:
        gw((tm(gr(0,0),26))+(63),(td(gr(0,0),26))+(1),0);
        sa(gr(0,0));
        gw(0,0,(gr(0,0))-(1));
        goto _0;
    _5:
        gw(1,0,0);
        gw(9,0,0);
        gw(9,1,-1);
        gw(10,0,1);
        gw(10,1,-1);
        gw(11,0,1);
        gw(11,1,0);
        gw(0,0,399);
        goto _6;
    _6:
        gw((tm(gr(0,0),20))+(66),(td(gr(0,0),20))+(4),(((gr(((tm(gr(0,0),20))*(3))+(1),(td(gr(0,0),20))+(4)))-(48))*(10))+((gr(((tm(gr(0,0),20))*(3))+(2),(td(gr(0,0),20))+(4)))-(48)));
        sa(gr(0,0));
        gw(0,0,(gr(0,0))-(1));
        goto _1;
    _7:
        gw(0,0,399);
        goto _8;
    _8:
        gw(2,0,2);
        goto _14;
    _9:
        gw(1,0,sp());
        goto _15;
    _10:
        System.Console.Out.Write((long)(gr(1,0)));
        return;
    _11:
        sa(1);
        goto _2;
    _12:
        sa(0);
        goto _2;
    _13:
        sp();
        goto _15;
    _14:
        sa((gr(2,0))+(9));
        gw(3,0,gr((gr(2,0))+(9),0));
        sa(1);
        {long v0=sp();sa(gr(sp(),v0));}
        gw(4,0,sp());
        sa(gr(0,0));
        gw(5,0,tm(gr(0,0),20));
        sa(20);
        {long v0=sp();sa((v0==0)?0:(sp()/v0));}
        gw(6,0,sp());
        sa(gr((gr(5,0))+(66),(gr(6,0))+(4)));
        gw(5,0,(gr(5,0))+(gr(3,0)));
        gw(6,0,(gr(6,0))+(gr(4,0)));
        sa(gr((gr(5,0))+(66),(gr(6,0))+(4)));
        gw(5,0,(gr(5,0))+(gr(3,0)));
        gw(6,0,(gr(6,0))+(gr(4,0)));
        sa(gr((gr(5,0))+(66),(gr(6,0))+(4)));
        gw(5,0,(gr(5,0))+(gr(3,0)));
        gw(6,0,(gr(6,0))+(gr(4,0)));
        sa(gr((gr(5,0))+(66),(gr(6,0))+(4)));
        gw(5,0,(gr(5,0))+(gr(3,0)));
        gw(6,0,(gr(6,0))+(gr(4,0)));
        sa(sp()*sp());
        sa(sp()*sp());
        sa(sp()*sp());
        sa(sr());
        sa(gr(1,0));
        {long v0=sp();sa((sp()>v0)?1:0);}
        if(sp()!=0)goto _9; else goto _13;
    _15:
        sa(gr(2,0));
        gw(2,0,(gr(2,0))-(1));
        if(sp()!=0)goto _12; else goto _16;
    _16:
        sa(gr(0,0));
        gw(0,0,(gr(0,0))-(1));
        if(sp()!=0)goto _11; else goto _10;
}}