/* compiled with BefunCompile v1.0.1 (c) 2015 */
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#define int64 long long
int64 gr(int64 x,int64 y){if(x>=0&&y>=0&&x<2000&&y<512){return g[y][x];}else{return 0;}}
void gw(int64 x,int64 y,int64 v){if(x>=0&&y>=0&&x<2000&&y<512){g[y][x]=v;}}
int rd(){return rand()%2==0;}
int64 td(int64 a,int64 b){ return (b==0)?0:(a/b); }
int64 tm(int64 a,int64 b){ return (b==0)?0:(a%b); }
int64*s;int q=16384;int y=0;
int64 sp(){if(!y)return 0;return s[--y];}
void sa(int64 v){if(q-y<8)s=(int64*)realloc(s,(q*=2)*sizeof(int64));s[y++]=v;}
int64 sr(){if(!y)return 0;return s[y-1];}
int main(void)
{
    srand(time(NULL));
    s=(int64*)calloc(q,sizeof(int64));
    goto _12;
_0:
    if(sp()!=0)goto _14; else goto _15;
_1:
    if(sp()!=0)goto _17; else goto _16;
_2:
    if(sp()!=0)goto _13; else goto _18;
_3:
    if(sp()!=0)goto _19; else goto _20;
_4:
    if(sp()!=0)goto _19; else goto _21;
_5:
    if(sp()!=0)goto _38; else goto _23;
_6:
    if(sp()!=0)goto _7; else goto _37;
_7:
    if(sp()!=0)goto _26; else goto _27;
_8:
    if(sp()!=0)goto _32; else goto _28;
_9:
    if(sp()!=0)goto _35; else goto _33;
_10:
    if(sp()!=0)goto _29; else goto _36;
_11:
    if(sp()!=0)goto _31; else goto _30;
_12:
    gw(1,0,2000);
    gw(2,0,500);
    gw(0,0,1000000);
    gw(3,0,2);
    gw(0,3,32);
    gw(1,3,32);
    goto _13;
_13:
    gw(tm(gr(3,0),gr(1,0)),(td(gr(3,0),gr(1,0)))+(1),88);
    sa((gr(3,0))+(gr(3,0)));
    sa((gr(0,0))>((gr(3,0))+(gr(3,0)))?1:0);
    goto _0;
_14:
    sa(sr());
    sa(32);
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(sr());
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(1);
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();gw(v1,v0,sp());}
    sa(gr(3,0));
    sa(sp()+sp());
    sa(sr());
    sa(gr(0,0));
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    {int64 v0=sp();sa((sp()>v0)?1:0);}
    goto _0;
_15:
    sp();
    goto _16;
_16:
    sa((gr(3,0))+(1));
    gw(3,0,(gr(3,0))+(1));
    sa(sr());
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(1);
    sa(sp()+sp());
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(32);
    {int64 v0=sp();sa(sp()-v0);}
    goto _1;
_17:
    sa((gr(0,0))>(gr(3,0))?1:0);
    goto _2;
_18:
    gw(4,0,0);
    gw(3,0,0);
    goto _19;
_19:
    sa((gr(3,0))+(1));
    gw(3,0,(gr(3,0))+(1));
    sa(sr());
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(1);
    sa(sp()+sp());
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(88);
    {int64 v0=sp();sa(sp()-v0);}
    goto _3;
_20:
    sa(gr(3,0));
    sa(gr(4,0));
    gw(4,0,(gr(4,0))+(1));
    sa(sr());
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(1);
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();gw(v1,v0,sp());}
    sa((gr(0,0))>(gr(3,0))?1:0);
    goto _4;
_21:
    sa(0);
    sa((gr(4,0))-(1));
    gw(4,0,(gr(4,0))-(1));
    sa(sr());
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(1);
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();gw(v1,v0,sp());}
    gw(6,0,0);
    gw(7,0,-1);
    gw(8,0,0);
    gw(9,0,1);
    goto _22;
_22:
    sa((gr(7,0))+(1));
    gw(7,0,(gr(7,0))+(1));
    sa(sr());
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(gr(1,0));
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(1);
    sa(sp()+sp());
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(gr(8,0));
    sa(sp()+sp());
    sa(sr());
    sa(gr(0,0));
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    {int64 v0=sp();sa((sp()>v0)?1:0);}
    goto _5;
_23:
    gw(7,0,(gr(7,0))-(1));
    sp();
    goto _24;
_24:
    sa(gr(8,0));
    gw(5,0,gr(4,0));
    goto _25;
_25:
    sa(sr());
    sa(gr(5,0));
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(gr(tm(gr(5,0),gr(1,0)),(td(gr(5,0),gr(1,0)))+(1)));
    {int64 v0=sp();sa(sp()-v0);}
    goto _6;
_26:
    gw(5,0,(gr(5,0))-(1));
    goto _25;
_27:
    sp();
    sa((0)>((gr(6,0))+(gr(9,0)))?1:0);
    goto _8;
_28:
    sa((gr(9,0))-(1));
    goto _10;
_29:
    sa(((gr(8,0))+(gr(tm((gr(6,0))-(1),gr(1,0)),(td((gr(6,0))-(1),gr(1,0)))+(1))))-(gr(tm(gr(7,0),gr(1,0)),(td(gr(7,0),gr(1,0)))+(1))));
    sa((((gr(0,0))>(((gr(8,0))+(gr(tm((gr(6,0))-(1),gr(1,0)),(td((gr(6,0))-(1),gr(1,0)))+(1))))-(gr(tm(gr(7,0),gr(1,0)),(td(gr(7,0),gr(1,0)))+(1))))?1:0)!=0)?0:1);
    goto _11;
_30:
    gw(8,0,sp());
    sa(gr(9,0));
    gw(6,0,(gr(9,0))+(gr(6,0)));
    sa(gr(7,0));
    sa(sp()+sp());
    gw(7,0,sp());
    goto _24;
_31:
    sp();
    goto _32;
_32:
    sa((gr(9,0))-(1));
    goto _9;
_33:
    gw(8,0,(gr(8,0))-(gr(tm(gr(6,0),gr(1,0)),(td(gr(6,0),gr(1,0)))+(1))));
    gw(6,0,(gr(6,0))+(1));
    goto _34;
_34:
    gw(9,0,(gr(9,0))*(-1));
    goto _24;
_35:
    gw(8,0,(gr(8,0))-(gr(tm(gr(7,0),gr(1,0)),(td(gr(7,0),gr(1,0)))+(1))));
    gw(7,0,(gr(7,0))-(1));
    goto _34;
_36:
    sa(((gr(8,0))-(gr(tm(gr(6,0),gr(1,0)),(td(gr(6,0),gr(1,0)))+(1))))+(gr(tm((gr(7,0))+(1),gr(1,0)),(td((gr(7,0))+(1),gr(1,0)))+(1))));
    sa((((gr(0,0))>(((gr(8,0))-(gr(tm(gr(6,0),gr(1,0)),(td(gr(6,0),gr(1,0)))+(1))))+(gr(tm((gr(7,0))+(1),gr(1,0)),(td((gr(7,0))+(1),gr(1,0)))+(1))))?1:0)!=0)?0:1);
    goto _11;
_37:
    sp();
    printf("%lld", (int64)(sp()));
    goto __;
_38:
    gw(8,0,sp());
    goto _22;
__:
    return 0;
}