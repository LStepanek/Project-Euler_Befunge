/* compiled with BefunCompile v1.0.3 (c) 2015 */
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#define int64 long long
char* _g = "v ###    {#}  T{ }  <{#}  T{ }  3>190p191p020p130pv{ }  1>40g9+30g2%!g40g8+30g2%!g+vv!g!%2g03+9g04`**<>30g:\"d\"-!#v_1+:30p2/40p>3"
           "0g40g2*>-|{ }  9>:40g9+30g2%p\";};}@\"^^{ }  *>#<$ #<20g.@{ }  ,>40g8+30g2%!g2*{ }  +^>$40g9+1-30g2%!g!v{ }  6>30g40g2* -^v{ }  @{"
           "_v#!}  #<{ }  -^{ }  '_^#!p04:-1g04<p%2g03+9g040p02++1!!-*2g04g03g02{$<  }  # ";
int t=0;int z=0;
int64 g[560];
int d(){int s,w,i,j,h;h=z;for(;t<334;t++)if(_g[t]==';')g[z++]=_g[++t];else if(_g[t]=='}')return z-h;else if(_g[t]=='{'){t++;s=z;w=d();for(i=1;i<_g[t+1]*9025+_g[t+2]*95+_g[t+3]-291872;i++)for(j=0;j<w;g[z++]=g[s+j++]);t+=3;}else g[z++]=_g[t];return z-h;}
int64 gr(int64 x,int64 y){if(x>=0&&y>=0&&x<80&&y<7){return g[y*80+x];}else{return 0;}}
void gw(int64 x,int64 y,int64 v){if(x>=0&&y>=0&&x<80&&y<7){g[y*80+x]=v;}}
int rd(){return rand()%2==0;}
int64 td(int64 a,int64 b){ return (b==0)?0:(a/b); }
int64 tm(int64 a,int64 b){ return (b==0)?0:(a%b); }
int64*s;int q=16384;int y=0;
int64 sp(){if(!y)return 0;return s[--y];}
void sa(int64 v){if(q-y<8)s=(int64*)realloc(s,(q*=2)*sizeof(int64));s[y++]=v;}
int64 sr(){if(!y)return 0;return s[y-1];}
int main(void)
{
    d();
    srand(time(NULL));
    s=(int64*)calloc(q,sizeof(int64));
    goto _6;
_0:
    if(sp()!=0)goto _9; else goto _20;
_1:
    if(sp()!=0)goto _16; else goto _11;
_2:
    if(sp()!=0)goto _18; else goto _17;
_3:
    if(sp()!=0)goto _14; else goto _19;
_4:
    if(sp()!=0)goto _7; else goto _15;
_5:
    if(((((gr(3,0))-(100))!=0)?0:1)!=0)goto _21;else goto _8;
_6:
    gw(9,0,1);
    gw(9,1,1);
    gw(2,0,0);
    gw(3,0,1);
    goto _7;
_7:
    sa(gr(3,0));
    goto _5;
_8:
    sa(1);
    sa(sp()+sp());
    sa(sr());
    gw(3,0,sp());
    sa(2);
    {int64 v0=sp();sa((v0==0)?0:(sp()/v0));}
    gw(4,0,sp());
    sa((gr(3,0))-((gr(4,0))*(2)));
    goto _0;
_9:
    sa((gr((gr(4,0))+(9),((tm(gr(3,0),2))!=0)?0:1))+(gr((gr(4,0))+(8),((tm(gr(3,0),2))!=0)?0:1)));
    gw((gr(4,0))+(9),tm(gr(3,0),2),(gr((gr(4,0))+(9),((tm(gr(3,0),2))!=0)?0:1))+(gr((gr(4,0))+(8),((tm(gr(3,0),2))!=0)?0:1)));
    goto _10;
_10:
    sa(1000000);
    {int64 v0=sp();sa((sp()>v0)?1:0);}
    sa(((gr((gr(4,0))+(9),((tm(gr(3,0),2))!=0)?0:1))!=0)?0:1);
    sa(((((gr(((gr(4,0))+(9))-(1),((tm(gr(3,0),2))!=0)?0:1))!=0)?0:1)!=0)?0:1);
    goto _1;
_11:
    gw(2,0,(gr(2,0))+(((((((gr(3,0))-((gr(4,0))*(2)))!=0)?0:1)!=0)?0:1)+(1)));
    gw((gr(4,0))+(9),tm(gr(3,0),2),0);
    sp();
    goto _12;
_12:
    sp();
    goto _13;
_13:
    sp();
    goto _14;
_14:
    sa((gr(4,0))-(1));
    gw(4,0,(gr(4,0))-(1));
    sa((sp()!=0)?0:1);
    goto _4;
_15:
    sa((gr(3,0))-((gr(4,0))*(2)));
    {int64 v0=sp();sa(sp()-v0);}
    goto _0;
_16:
    sa((sp()!=0)?0:1);
    goto _2;
_17:
    gw(2,0,(gr(2,0))+(((((((gr(3,0))-((gr(4,0))*(2)))!=0)?0:1)!=0)?0:1)+(1)));
    gw((gr(4,0))+(9),tm(gr(3,0),2),0);
    goto _12;
_18:
    sa((sp()!=0)?0:1);
    goto _3;
_19:
    gw(2,0,(gr(2,0))+(((((((gr(3,0))-((gr(4,0))*(2)))!=0)?0:1)!=0)?0:1)+(1)));
    gw((gr(4,0))+(9),tm(gr(3,0),2),0);
    goto _13;
_20:
    sa((gr((gr(4,0))+(8),((tm(gr(3,0),2))!=0)?0:1))*(2));
    gw((gr(4,0))+(9),tm(gr(3,0),2),(gr((gr(4,0))+(8),((tm(gr(3,0),2))!=0)?0:1))*(2));
    goto _10;
_21:
    sp();
    printf("%lld", (int64)(gr(2,0)));
    goto __;
__:
    return 0;
}