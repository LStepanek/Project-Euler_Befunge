/* compiled with BefunCompile v1.0.5 (c) 2015 */
#include <stdio.h>
#include <stdlib.h>
#define int64 long long
char* _g = "v{X}  ){ }  Zv{X}  ){ } !?>902p012p9>:0\\1pv{ }  ]|\\-1: <{ }  S>12g55+, #$ \" =\",, . @{ }  Gvp20<  |`9g20    <{ }  R<  <{ }  0>$0v"
           "{ }  (> v{ }  9>002g0g\"0\"-1p v>02g0g\"0\"-:9`|  >:22p55+-| >22g1g     #v_ 02g0g\"9\"`!#^_{ }  )## v{ }  ->1+^{ }  (>0|-9p22+1:g22<vp"
           "20-1g20p0g20+\"0\"g22p1g221<v!`g200{ }  A<{ }  -p20+1g20< ##{ }  =>  02g0g\"9\"`!#v_{ }  3^  +{ }  K>002g0g\"0\"-1p\"X\"02g0p^  1  >#v_0"
           "02p{ }  3032p0>:0g\"0\"-32g55v>12p>{ }  -^g    >02g9-!02g8-!02g7-!++v{ }  (|-9\\+1:p23+*+<+{ }  22    v{ }  4<{ }  (>$32g:.55+,12g^"
           "{ }  20    >02g6-70g\"0\"-55+*80g\"0\"-+55+*90g\"0\"-+89+%+!v>++#^_02g0g\"9\"`!#v_^    v!+%+58+-\"0\"g08*+55+-\"0\"g07*+55-\"0\"g06-5g20<+v\"X\""
           "p1-\"0\"g0g200<#     >02g4-50g\"0\"-55+*60g\"0\"-+55+*70g\"0\"-+47+%+!v+>02g0p02g1+02p   ^     v!+%+70+-\"0\"g06*+55+-\"0\"g05*+55-\"0\"g04-3g"
           "20<+{ }  7>02g2-30g\"0\"-55+*40g\"0\"-+55+*50g\"0\"-+05+%+!v+{ }  7v!+%+30+-\"0\"g04*+55+-\"0\"g03*+55-\"0\"g02-1g20<+{ }  7>02g0-10g\"0\"-55+"
           "*20g\"0\"-+55+*30g\"0\"-+02+%+!>^{ }  5";
int t=0;int z=0;
int64 g[1564];
int d(){int s,w,i,j,h;h=z;for(;t<931;t++)if(_g[t]==';')g[z++]=_g[++t];else if(_g[t]=='}')return z-h;else if(_g[t]=='{'){t++;s=z;w=d();for(i=1;i<_g[t+1]*9025+_g[t+2]*95+_g[t+3]-291872;i++)for(j=0;j<w;g[z++]=g[s+j++]);t+=3;}else g[z++]=_g[t];return z-h;}
int64 gr(int64 x,int64 y){if(x>=0&&y>=0&&x<68&&y<23){return g[y*68+x];}else{return 0;}}
void gw(int64 x,int64 y,int64 v){if(x>=0&&y>=0&&x<68&&y<23){g[y*68+x]=v;}}
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
    gw(0,2,9);
    gw(1,2,0);
    gw(9,1,0);
    sa(8);
    sa(9);
_1:
    if(sp()!=0)goto _26;else goto _2;
_2:
    sp();
_3:
    if(((gr(0,2))>(9)?1:0)!=0)goto _25;else goto _4;
_4:
    sa(gr(gr(0,2),0)-48);
    sa((gr(gr(0,2),0)-48)>(9)?1:0);
    if(sp()!=0)goto _24;else goto _5;
_5:
    sa(1);
    sa(sp()+sp());
    sa(sr());
    gw(2,2,sp());
    sa(10);
    {int64 v0=sp();sa(sp()-v0);}
_6:
    if(sp()!=0)goto _19;else goto _7;
_7:
    sa((((gr(gr(0,2),0))>(57)?1:0)!=0)?0:1);
    if(sp()!=0)goto _18;else goto _8;
_8:
    gw(0,2,gr(0,2)+1);
_9:
    sa((((0)>(gr(0,2))?1:0)!=0)?0:1);
    if(sp()!=0)goto _10;else goto _14;
_10:
    sa(((gr(0,2)-9!=0)?0:1)+((gr(0,2)-8!=0)?0:1)+((gr(0,2)-7!=0)?0:1)+(((gr(0,2)-6)+(tm(((((gr(7,0)-48)*10)+(gr(8,0)-48))*10)+(gr(9,0)-48),17))!=0)?0:1)+(((gr(0,2)-5)+(tm(((((gr(6,0)-48)*10)+(gr(7,0)-48))*10)+(gr(8,0)-48),13))!=0)?0:1)+(((gr(0,2)-4)+(tm(((((gr(5,0)-48)*10)+(gr(6,0)-48))*10)+(gr(7,0)-48),11))!=0)?0:1)+(((gr(0,2)-3)+(tm(((((gr(4,0)-48)*10)+(gr(5,0)-48))*10)+(gr(6,0)-48),7))!=0)?0:1)+(((gr(0,2)-2)+(tm(((((gr(3,0)-48)*10)+(gr(4,0)-48))*10)+(gr(5,0)-48),5))!=0)?0:1)+(((gr(0,2)-1)+(tm(((((gr(2,0)-48)*10)+(gr(3,0)-48))*10)+(gr(4,0)-48),3))!=0)?0:1)+(((gr(0,2)-0)+(tm(((((gr(1,0)-48)*10)+(gr(2,0)-48))*10)+(gr(3,0)-48),2))!=0)?0:1));
    if(sp()!=0)goto _3;else goto _11;
_11:
    sa((((gr(gr(0,2),0))>(57)?1:0)!=0)?0:1);
    if(sp()!=0)goto _13;else goto _12;
_12:
    gw(0,2,gr(0,2)+1);
    goto _3;
_13:
    gw(gr(gr(0,2),0)-48,1,0);
    gw(gr(0,2),0,88);
    gw(0,2,gr(0,2)+1);
    goto _3;
_14:
    gw(0,2,0);
    gw(3,2,0);
    gw(3,2,(gr(0,0)-48)+(gr(3,2)*10));
    sa(1);
    sa(-9);
_15:
    if(sp()!=0)goto _17;else goto _16;
_16:
    sp();
    sa(gr(3,2));
    printf("%lld", (int64)(gr(3,2)));
    printf("\n");
    sa(gr(1,2));
    sa(sp()+sp());
    gw(1,2,sp());
    goto _3;
_17:
    sa(sr());
    sa(0);
    {int64 v0=sp();sa(gr(sp(),v0));}
    sa(48);
    {int64 v0=sp();sa(sp()-v0);}
    sa(gr(3,2)*10);
    sa(sp()+sp());
    gw(3,2,sp());
    sa(sr());
    sa(1);
    sa(sp()+sp());
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(9);
    {int64 v0=sp();sa(sp()-v0);}
    goto _15;
_18:
    gw(gr(gr(0,2),0)-48,1,0);
    gw(gr(0,2),0,88);
    goto _8;
_19:
    sa(gr(gr(2,2),1));
    if(sp()!=0)goto _20;else goto _21;
_20:
    sa(gr(2,2));
    gw(2,2,gr(2,2)+1);
    sa(9);
    {int64 v0=sp();sa(sp()-v0);}
    if(sp()!=0)goto _19;else goto _7;
_21:
    sa((((gr(gr(0,2),0))>(57)?1:0)!=0)?0:1);
    if(sp()!=0)goto _23;else goto _22;
_22:
    gw(gr(2,2),1,1);
    gw(gr(0,2),0,gr(2,2)+48);
    gw(0,2,gr(0,2)-1);
    goto _9;
_23:
    gw(gr(gr(0,2),0)-48,1,0);
    goto _22;
_24:
    gw(2,2,0);
    sp();
    sa(-10);
    goto _6;
_25:
    sa(gr(1,2));
    printf("\n");
    sa(32);
    printf("=");
    printf("%c", (char)(sp()));
    printf("%lld", (int64)(sp()));
    return 0;
_26:
    sa(sr());
    sa(0);
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    sa(1);
    {int64 v0=sp();int64 v1=sp();gw(v1,v0,sp());}
    sa(sr());
    sa(1);
    {int64 v0=sp();sa(sp()-v0);}
    {int64 v0=sp();int64 v1=sp();sa(v0);sa(v1);}
    goto _1;
}