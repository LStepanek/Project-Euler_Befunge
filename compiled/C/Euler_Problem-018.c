/* compiled with BefunCompile v1.0 (c) 2015 */
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#define int64 long long
int64 g[0x16][0x120]={{36,36,62,53,51,42,32,48,48,112,48,48,103,49,45,50,48,112,48,49,48,112,62,49,48,103,51,42,58,50,48,103,49,43,103,34,48,34,45,53,53,43,42,92,49,43,50,48,103,49,43,103,34,48,34,45,43,49,48,103,50,48,103,49,43,112,49,48,103,49,43,58,49,48,112,50,48,103,45,49,45,35,118,95,50,48,103,58,49,45,50,48,112,48,49,48,112,35,118,95,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{55,53,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{57,53,32,54,52,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{49,55,32,52,55,32,56,50,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,32,36,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{49,56,32,51,53,32,56,55,32,49,48,32,32,32,32,32,32,32,32,32,32,32,62,48,48,103,50,45,58,49,48,112,50,48,112,62,49,48,103,50,48,103,49,43,103,49,48,103,50,48,103,50,43,103,58,49,48,103,49,43,50,48,103,50,43,103,32,45,58,48,96,62,35,94,95,45,62,43,49,48,103,50,48,103,49,43,112,49,48,103,58,49,45,49,48,112,35,118,95,50,48,103,58,49,45,58,50,48,112,49,48,112,35,118,95,48,49,103,46,64},{50,48,32,48,52,32,56,50,32,52,55,32,54,53,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,60,32,32,32,32,32,32},{49,57,32,48,49,32,50,51,32,55,53,32,48,51,32,51,52,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{56,56,32,48,50,32,55,55,32,55,51,32,48,55,32,54,51,32,54,55,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{57,57,32,54,53,32,48,52,32,50,56,32,48,54,32,49,54,32,55,48,32,57,50,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{52,49,32,52,49,32,50,54,32,53,54,32,56,51,32,52,48,32,56,48,32,55,48,32,51,51,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{52,49,32,52,56,32,55,50,32,51,51,32,52,55,32,51,50,32,51,55,32,49,54,32,57,52,32,50,57,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{53,51,32,55,49,32,52,52,32,54,53,32,50,53,32,52,51,32,57,49,32,53,50,32,57,55,32,53,49,32,49,52,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{55,48,32,49,49,32,51,51,32,50,56,32,55,55,32,55,51,32,49,55,32,55,56,32,51,57,32,54,56,32,49,55,32,53,55,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{57,49,32,55,49,32,53,50,32,51,56,32,49,55,32,49,52,32,57,49,32,52,51,32,53,56,32,53,48,32,50,55,32,50,57,32,52,56,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{54,51,32,54,54,32,48,52,32,54,56,32,56,57,32,53,51,32,54,55,32,51,48,32,55,51,32,49,54,32,54,57,32,56,55,32,52,48,32,51,49,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{48,52,32,54,50,32,57,56,32,50,55,32,50,51,32,48,57,32,55,48,32,57,56,32,55,51,32,57,51,32,51,56,32,53,51,32,54,48,32,48,52,32,50,51,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32}};
int64 gr(int64 x,int64 y){if(x>=0&&y>=0&&x<120&&y<16){return g[y][x];}else{return 0;}}
void gw(int64 x,int64 y,int64 v){if(x>=0&&y>=0&&x<120&&y<16){g[y][x]=v;}}
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
    goto _5;
_0:
    if(sp()!=0)goto _16; else goto _7;
_1:
    if(sp()!=0)goto _15; else goto _8;
_2:
    if(sp()!=0)goto _9; else goto _12;
_3:
    if(sp()!=0)goto _9; else goto _13;
_4:
    if(((((((gr(gr(1,0),((gr(2,0))+(2))))-(gr(((gr(1,0))+(1)),((gr(2,0))+(2))))))>(0))?1:0))!=0)goto _14;else goto _10;
_5:
    gw(0,0,15);
    gw(2,0,((gr(0,0))-(1)));
    gw(1,0,0);
    gw(gr(1,0),((gr(2,0))+(1)),((((((gr(((gr(1,0))*(3)),((gr(2,0))+(1))))-(48)))*(10)))+(((gr(((((gr(1,0))*(3)))+(1)),((gr(2,0))+(1))))-(48)))));
    sp();
    sp();
    goto _6;
_6:
    sa(((gr(1,0))+(1)));
    gw(1,0,((gr(1,0))+(1)));
    sa(gr(2,0));
    {int64 v0=sp();sa(sp()-v0);}
    sa(1);
    {int64 v0=sp();sa(sp()-v0);}
    goto _0;
_7:
    sa(gr(2,0));
    gw(2,0,((gr(2,0))-(1)));
    gw(1,0,0);
    goto _1;
_8:
    sa(((gr(0,0))-(2)));
    gw(1,0,((gr(0,0))-(2)));
    gw(2,0,sp());
    goto _9;
_9:
    sa(gr(gr(1,0),((gr(2,0))+(1))));
    sa(gr(gr(1,0),((gr(2,0))+(2))));
    sa(((gr(gr(1,0),((gr(2,0))+(2))))-(gr(((gr(1,0))+(1)),((gr(2,0))+(2))))));
    goto _4;
_10:
    {int64 v0=sp();sa(sp()-v0);}
    goto _11;
_11:
    sa(sp()+sp());
    gw(gr(1,0),((gr(2,0))+(1)),sp());
    sa(gr(1,0));
    gw(1,0,((gr(1,0))-(1)));
    goto _2;
_12:
    sa(gr(2,0));
    sa(((gr(2,0))-(1)));
    gw(2,0,((gr(2,0))-(1)));
    gw(1,0,sp());
    goto _3;
_13:
    printf("%lld", (int64)(gr(0,1)));
    goto __;
_14:
    sp();
    goto _11;
_15:
    gw(gr(1,0),((gr(2,0))+(1)),((((((gr(((gr(1,0))*(3)),((gr(2,0))+(1))))-(48)))*(10)))+(((gr(((((gr(1,0))*(3)))+(1)),((gr(2,0))+(1))))-(48)))));
    goto _6;
_16:
    gw(gr(1,0),((gr(2,0))+(1)),((((((gr(((gr(1,0))*(3)),((gr(2,0))+(1))))-(48)))*(10)))+(((gr(((((gr(1,0))*(3)))+(1)),((gr(2,0))+(1))))-(48)))));
    goto _6;
__:
    return 0;
}