/* compiled with BefunCompile v1.0 (c) 2015 */
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#define int64 long long
int64 g[0x12][0x72]={{118,51,48,51,50,51,50,51,51,50,51,50,51,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{118,51,49,51,50,51,50,51,51,50,51,50,51,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{54,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{62,50,42,62,58,58,48,103,34,48,34,45,52,55,42,43,92,48,112,58,58,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,32,124,58,45,49,112,49,92,43,42,55,52,45,34,48,34,103,49,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{118,32,36,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{62,50,48,50,112,49,49,50,112,49,50,50,112,34,50,38,34,42,49,43,51,50,112,48,57,50,112,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{118,50,48,43,49,103,50,48,112,50,57,43,103,50,57,33,43,45,49,103,50,49,37,55,103,50,48,60,62,35,32,32,32,32,32,32,32,48,35,32,118,35,32,32,32,60,32,32,32,32,32,32,62,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,118},{62,112,49,50,103,49,43,49,50,112,51,50,103,52,37,32,32,32,32,32,32,32,32,32,32,32,32,32,124,32,32,32,32,32,32,32,62,49,32,62,62,50,50,103,92,103,49,50,103,49,45,45,124,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,51,50,103,34,100,34,37,124,32,32,48,94,32,60,32,32,35,32,32,32,32,32,32,62,49,49,50,112,50,50,103,58,49,43,50,50,112,54,54,43,45,124,32},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,118,37,42,52,34,100,34,103,50,51,60,62,35,94,95,49,94,32,32,124,45,43,49,42,34,40,50,34,103,50,51,60,112,50,51,43,49,103,50,51,112,50,50,49,60,32},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,32,32,32,32,32,32,32,32,32,32,94,62,49,94,32,32,32,32,62,57,50,103,46,64,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,60}};
int64 gr(int64 x,int64 y){if(x>=0&&y>=0&&x<72&&y<12){return g[y][x];}else{return 0;}}
void gw(int64 x,int64 y,int64 v){if(x>=0&&y>=0&&x<72&&y<12){g[y][x]=v;}}
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
    goto _7;
_0:
    if(sp()!=0)goto _21; else goto _8;
_1:
    if(sp()!=0)goto _10; else goto _16;
_2:
    if(sp()!=0)goto _11; else goto _14;
_3:
    if(sp()!=0)goto _13; else goto _12;
_4:
    if(sp()!=0)goto _11; else goto _15;
_5:
    if(sp()!=0)goto _17; else goto _18;
_6:
    if(sp()!=0)goto _19; else goto _20;
_7:
    gw(12,0,((((gr(12,0))-(48)))+(28)));
    gw(12,1,((((gr(12,1))-(48)))+(28)));
    sa(11);
    sa(11);
    goto _0;
_8:
    gw(0,2,2);
    gw(1,2,1);
    gw(2,2,1);
    gw(3,2,1901);
    gw(9,2,0);
    gw(9,2,((((((tm(gr(0,2),7))+(((gr(1,2))-(1)))))!=0)?0:1)+(gr(9,2))));
    gw(0,2,((gr(0,2))+(1)));
    gw(1,2,((gr(1,2))+(1)));
    sp();
    goto _9;
_9:
    sa(tm(gr(3,2),4));
    goto _1;
_10:
    sa(((gr(gr(2,2),0))-(((gr(1,2))-(1)))));
    goto _2;
_11:
    sa(((gr(3,2))-(2001)));
    goto _3;
_12:
    printf("%lld", (int64)(gr(9,2)));
    goto __;
_13:
    gw(9,2,((((((tm(gr(0,2),7))+(((gr(1,2))-(1)))))!=0)?0:1)+(gr(9,2))));
    gw(0,2,((gr(0,2))+(1)));
    gw(1,2,((gr(1,2))+(1)));
    goto _9;
_14:
    gw(1,2,1);
    sa(gr(2,2));
    gw(2,2,((gr(2,2))+(1)));
    sa(12);
    {int64 v0=sp();sa(sp()-v0);}
    goto _4;
_15:
    gw(2,2,1);
    gw(3,2,((gr(3,2))+(1)));
    goto _11;
_16:
    sa(tm(gr(3,2),100));
    goto _5;
_17:
    sa(((gr(gr(2,2),1))-(((gr(1,2))-(1)))));
    goto _2;
_18:
    sa(tm(gr(3,2),400));
    goto _6;
_19:
    sa(((gr(gr(2,2),0))-(((gr(1,2))-(1)))));
    goto _2;
_20:
    sa(((gr(gr(2,2),1))-(((gr(1,2))-(1)))));
    goto _2;
_21:
    sa(sr());
    sa(sr());
    sa(0);
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(48);
    {int64 v0=sp();sa(sp()-v0);}
    sa(28);
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(0);
    {int64 v0=sp();int64 v1=sp();gw(v1,v0,sp());}
    sa(sr());
    sa(sr());
    sa(1);
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(48);
    {int64 v0=sp();sa(sp()-v0);}
    sa(28);
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(1);
    {int64 v0=sp();int64 v1=sp();gw(v1,v0,sp());}
    sa(1);
    {int64 v0=sp();sa(sp()-v0);}
    sa(sr());
    goto _0;
__:
    return 0;
}