/* compiled with BefunCompile v1.0 (c) 2015 */
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#define int64 long long
int64 g[0x28][0x123]={{118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,49,32,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,49,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{62,53,53,54,55,42,42,42,48,48,112,34,50,34,49,48,112,32,50,51,48,112,62,118,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{62,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,62,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,48,48,103,52,48,112,48,53,48,112,62,52,48,103,49,45,52,48,112,52,48,103,49,48,103,37,34,52,34,43,52,48,103,49,48,103,47,49,43,103,34,48,34,45,58,52,48,103,49,48,103,37,49,43,52,48,103,49,48,103,47,49,43,103,34,48,34,45,53,48,103,43,43,32,118},{32,118,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,118,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,124,103,48,52,112,43,49,47,103,48,49,103,48,52,43,49,37,103,48,49,103,48,52,43,34,48,34,112,43,49,47,103,48,49,103,48,52,43,34,52,34,37,103,48,49,103,48,52,43,34,48,34,37,43,53,53,112,48,53,47,43,53,53,58,60},{94,60,124,45,42,43,53,53,34,100,34,45,103,48,55,103,48,48,60,124,45,34,48,34,103,43,49,47,103,48,49,103,48,55,43,34,52,34,37,103,48,49,103,48,55,60,112,48,55,48,112,48,51,43,49,103,48,51,60,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32},{32,32,62,51,48,103,46,64,32,32,32,32,32,32,32,32,32,32,32,62,55,48,103,49,43,55,48,112,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32}};
int64 gr(int64 x,int64 y){if(x>=0&&y>=0&&x<123&&y<28){return g[y][x];}else{return 0;}}
void gw(int64 x,int64 y,int64 v){if(x>=0&&y>=0&&x<123&&y<28){g[y][x]=v;}}
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
    goto _3;
_0:
    if(sp()!=0)goto _4; else goto _8;
_1:
    if((gr(4,0))!=0)goto _5;else goto _6;
_2:
    if((((gr(((tm(gr(7,0),gr(1,0)))+(52)),((td(gr(7,0),gr(1,0)))+(1))))-(48)))!=0)goto _7;else goto _9;
_3:
    gw(0,0,1050);
    gw(1,0,50);
    gw(3,0,2);
    goto _4;
_4:
    gw(4,0,gr(0,0));
    gw(5,0,0);
    goto _5;
_5:
    gw(4,0,((gr(4,0))-(1)));
    sa(((gr(((tm(gr(4,0),gr(1,0)))+(52)),((td(gr(4,0),gr(1,0)))+(1))))-(48)));
    sa(((((gr(((tm(gr(4,0),gr(1,0)))+(52)),((td(gr(4,0),gr(1,0)))+(1))))-(48)))+(((((gr(((tm(gr(4,0),gr(1,0)))+(1)),((td(gr(4,0),gr(1,0)))+(1))))-(48)))+(gr(5,0))))));
    gw(5,0,td(((((gr(((tm(gr(4,0),gr(1,0)))+(52)),((td(gr(4,0),gr(1,0)))+(1))))-(48)))+(((((gr(((tm(gr(4,0),gr(1,0)))+(1)),((td(gr(4,0),gr(1,0)))+(1))))-(48)))+(gr(5,0))))),10));
    sa(10);
    {int64 v0=sp();sa((v0==0)?0:(sp()%v0));}
    sa(48);
    sa(sp()+sp());
    gw(((tm(gr(4,0),gr(1,0)))+(52)),((td(gr(4,0),gr(1,0)))+(1)),sp());
    sa(48);
    sa(sp()+sp());
    gw(((tm(gr(4,0),gr(1,0)))+(1)),((td(gr(4,0),gr(1,0)))+(1)),sp());
    goto _1;
_6:
    gw(3,0,((gr(3,0))+(1)));
    gw(7,0,0);
    goto _2;
_7:
    sa(((((gr(0,0))-(gr(7,0))))-(1000)));
    goto _0;
_8:
    printf("%lld", (int64)(gr(3,0)));
    goto __;
_9:
    gw(7,0,((gr(7,0))+(1)));
    goto _2;
__:
    return 0;
}