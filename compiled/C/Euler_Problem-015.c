/* compiled with BefunCompile v1.0.4 (c) 2015 */
#include <stdio.h>
#include <stdlib.h>
#define int64 long long
char* _g = "v{ }  n{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{"
           "0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }  Y{0}  5{ }"
           "  .>{ }  H{v{ }  8>}  \"00g1-10gg00g10g1-g+00g10gpv>100p110p> 00g492*+10g-*|>00g392*+`#^_>00g1-10g1-*|{ }  )vp01+1g01p00-1g00<{ }"
           "  )^p011p00+g01g00<{ }  9>100g10gp{ }  2^{ }  )|!  `+2*58+g00g01{ }  B<{ }  3@.g:*73<{ }  d";
int t=0;int z=0;
int64 g[2106];
int d(){int s,w,i,j,h;h=z;for(;t<475;t++)if(_g[t]==';')g[z++]=_g[++t];else if(_g[t]=='}')return z-h;else if(_g[t]=='{'){t++;s=z;w=d();for(i=1;i<_g[t+1]*9025+_g[t+2]*95+_g[t+3]-291872;i++)for(j=0;j<w;g[z++]=g[s+j++]);t+=3;}else g[z++]=_g[t];return z-h;}
int64 gr(int64 x,int64 y){if(x>=0&&y>=0&&x<78&&y<27){return g[y*78+x];}else{return 0;}}
void gw(int64 x,int64 y,int64 v){if(x>=0&&y>=0&&x<78&&y<27){g[y*78+x]=v;}}
int64 td(int64 a,int64 b){ return (b==0)?0:(a/b); }
int64 tm(int64 a,int64 b){ return (b==0)?0:(a%b); }
int64*s;int q=16384;int y=0;
int64 sp(){if(!y)return 0;return s[--y];}
void sa(int64 v){if(q-y<8)s=(int64*)realloc(s,(q*=2)*sizeof(int64));s[y++]=v;}
int64 sr(){if(!y)return 0;return s[y-1];}
int main(void)
{
    d();
    s=(int64*)calloc(q,sizeof(int64));
    goto _1;
_0:
    if(((gr(0,0))*((22)-(gr(1,0))))!=0)goto _6;else goto _5;
_1:
    gw(0,0,1);
    gw(1,0,1);
    goto _0;
_2:
    printf("%lld", (int64)(gr(21,21)));
    return 0;
_3:
    gw(gr(0,0),gr(1,0),(gr((gr(0,0))-(1),gr(1,0)))+(gr(gr(0,0),(gr(1,0))-(1))));
    goto _8;
_4:
    gw(gr(0,0),gr(1,0),1);
    goto _8;
_5:
    gw(0,0,(gr(0,0))+(gr(1,0)));
    gw(1,0,1);
    goto _0;
_6:
    sa((gr(0,0))>(21)?1:0);
    if(sp()!=0)goto _8; else goto _7;
_7:
    sa(((gr(0,0))-(1))*((gr(1,0))-(1)));
    if(sp()!=0)goto _3; else goto _4;
_8:
    gw(0,0,(gr(0,0))-(1));
    gw(1,0,(gr(1,0))+(1));
    sa(((((gr(1,0))+(gr(0,0)))>(42)?1:0)!=0)?0:1);
    if(sp()!=0)goto _0; else goto _2;
}