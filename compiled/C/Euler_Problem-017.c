/* compiled with BefunCompile v1.0 (c) 2015 */
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#define int64 long long
int64 g[0x15][0x48]={{118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{48,51,51,53,52,52,51,53,53,52,51,54,54,56,56,55,55,57,56,56,54,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{48,51,54,54,53,53,53,55,54,54,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{36,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{36,32,32,32,118,45,49,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,118,45,49,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32},{62,53,52,42,62,58,58,58,49,103,34,48,34,45,92,49,112,35,94,95,53,52,42,62,58,58,58,50,103,34,48,34,45,92,50,112,124,32,32,32,32,32,32,32,32,32,32,32},{118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,42,42,50,53,34,100,34,32,48,32,36,36,60,32,32,32,32,32,32,32,32,32,32,32},{118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60},{32,32,32,118,32,32,32,32,32,32,32,32,32,32,32,32,36,60,32,32,32,62,58,53,53,43,47,50,103,92,53,53,43,37,32,32,32,32,32,32,32,32,32,32,32,118,32,32},{58,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,58,53,52,42,96,124,32,32,32,32,32,32,32,32,32,62,34,100,34,47,49,103,55,48,32,32,32,32,32,118,32,32},{62,48,92,62,58,33,35,118,95,58,34,100,34,92,96,124,32,94,48,103,49,60,32,32,62,58,34,100,34,37,33,124,32,32,32,32,32,32,32,32,118,32,32,32,32,60,32,32},{118,32,32,32,32,32,32,60,32,32,32,32,32,32,32,62,58,34,125,34,56,42,45,35,94,95,36,51,56,48,118,62,58,34,100,34,47,49,103,92,32,34,100,34,37,118,32,32},{32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,60,92,51,92,55,60,32,32},{62,43,35,32,92,58,35,32,95,43,32,32,32,32,32,32,32,32,32,32,92,32,49,45,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,58,124},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,64,46,43,95,32,35,33,32,35,58,92,32,35,43,60}};
int64 gr(int64 x,int64 y){if(x>=0&&y>=0&&x<48&&y<15){return g[y][x];}else{return 0;}}
void gw(int64 x,int64 y,int64 v){if(x>=0&&y>=0&&x<48&&y<15){g[y][x]=v;}}
int random(){return rand()%2==0;}
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
    goto _10;
_0:
    if(sp()!=0)goto _30; else goto _11;
_1:
    if(sp()!=0)goto _29; else goto _12;
_2:
    if(sp()!=0)goto _13; else goto _20;
_3:
    if(sp()!=0)goto _14; else goto _15;
_4:
    if(sp()!=0)goto _16; else goto _17;
_5:
    if(sp()!=0)goto _19; else goto _18;
_6:
    if(sp()!=0)goto _26; else goto _21;
_7:
    if(sp()!=0)goto _28; else goto _27;
_8:
    if(sp()!=0)goto _22; else goto _25;
_9:
    if(sp()!=0)goto _24; else goto _23;
_10:
    gw(20,1,((gr(20,1))-(48)));
    sa(20);
    sa(20);
    goto _0;
_11:
    gw(20,2,((gr(20,2))-(48)));
    sa(20);
    sa(20);
    goto _1;
_12:
    sp();
    sp();
    sa(0);
    sa(1000);
    sa(0);
    sa(1000);
    sa(0);
    goto _2;
_13:
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(sr());
    goto _3;
_14:
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    goto _13;
_15:
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(1);
    {int64 v0=sp();sa(sp()-v0);}
    sa(sr());
    goto _4;
_16:
    sa(sr());
    sa(0);
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(sr());
    sa((sp()!=0)?0:1);
    goto _2;
_17:
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(sr());
    sa((sp()!=0)?0:1);
    goto _5;
_18:
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    goto _17;
_19:
    sa(sp()+sp());
    printf("%lld", (int64)(sp()));
    goto __;
_20:
    sa(sr());
    sa(100);
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    {int64 v0=sp();sa((sp()>v0)?1:0);}
    goto _6;
_21:
    sa(sr());
    sa(1000);
    {int64 v0=sp();sa(sp()-v0);}
    goto _8;
_22:
    sa(sr());
    sa(100);
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    sa((sp()!=0)?0:1);
    goto _9;
_23:
    sa(sr());
    sa(100);
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(1);
    {int64 v0=sp();sa(gr(sp(),v0));}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(100);
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    sa(7);
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(3);
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(sr());
    sa((sp()!=0)?0:1);
    goto _2;
_24:
    sa(100);
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(1);
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(7);
    sa(0);
    sa(1);
    goto _2;
_25:
    sp();
    sa(3);
    sa(8);
    sa(0);
    sa(1);
    goto _2;
_26:
    sa(sr());
    sa(20);
    {int64 v0=sp();sa((sp()>v0)?1:0);}
    goto _7;
_27:
    sa(1);
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(0);
    sa(1);
    goto _2;
_28:
    sa(sr());
    sa(10);
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    sa(2);
    {int64 v0=sp();sa(gr(sp(),v0));}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(10);
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    sa(sr());
    sa((sp()!=0)?0:1);
    goto _2;
_29:
    sa(1);
    {int64 v0=sp();sa(sp()-v0);}
    sa(sr());
    sa(sr());
    sa(sr());
    sa(2);
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(48);
    {int64 v0=sp();sa(sp()-v0);}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(2);
    {int64 v0=sp();int64 v1=sp();gw(v1,v0,sp());}
    goto _1;
_30:
    sa(1);
    {int64 v0=sp();sa(sp()-v0);}
    sa(sr());
    sa(sr());
    sa(sr());
    sa(1);
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(48);
    {int64 v0=sp();sa(sp()-v0);}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(1);
    {int64 v0=sp();int64 v1=sp();gw(v1,v0,sp());}
    goto _0;
__:
    return 0;
}