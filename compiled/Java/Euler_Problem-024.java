/* transpiled with BefunCompile v1.1.0 (c) 2015 */
class Program{
private final static String _g = "AR+LCAAAAAAABACdUDGOAyEM/AqBrVgRMbtc7oKQdQ+xNlesREuFUvD4mCVpI+WmsEdG4xlcPZY1fF2+f67qY5De911bi/q5VtWC5VoAl/4hfgWoNKxHTU/SN9LgxHBc"+
                                 "j2lBmJEREi3IEXOj1plninDRbLeJLB89NhGuKApBirAckC2Q/07t6Ty9CTVhk9acvmuVfeTESOI7cnX89nTvUI93wsw9CsZwk4M5+cDSj2Y7CxlrBs7Fs3ix016LHxmn"+
                                 "DJSZlBHDbYgfFCr43OgBAAA=";
private final long[] g=zc(zd(java.util.Base64.getDecoder().decode(_g)));
private long[]zc(byte[]b){long[]r=new long[488];for(int i=0;i<488;i++)r[i]=b[i];return r;}
private byte[]zd(byte[]o){byte[]d=java.util.Arrays.copyOfRange(o,1,o.length);for(int i=0;i<o[0];i++)d=zs(d);return d;}
private byte[]zs(byte[]o){try{
java.io.ByteArrayInputStream  y=new java.io.ByteArrayInputStream(o);
java.util.zip.GZIPInputStream s=new java.util.zip.GZIPInputStream(y);
java.io.ByteArrayOutputStream a=new java.io.ByteArrayOutputStream();
int res=0;byte buf[]=new byte[1024];while(res>=0){res=s.read(buf,0,1024);if(res>0)a.write(buf,0,res);}return a.toByteArray();
}catch(java.io.IOException e){return null;}}
private long gr(long x,long y){return(x>=0&&y>=0&&x<61&&y<8)?g[(int)(y*61+x)]:0;}
private void gw(long x,long y,long v){if(x>=0&&y>=0&&x<61&&y<8)g[(int)(y*61+x)]=v;}
private java.io.BufferedReader ib=new java.io.BufferedReader(new java.io.InputStreamReader(System.in));
private long td(long a,long b){return(b==0)?0:(a/b);}
private long tm(long a,long b){return(b==0)?0:(a%b);}
private final static java.util.Stack<Long> s=new java.util.Stack<Long>();
private long sp(){return(s.size()==0)?0:s.pop();}
private void sa(long v){s.push(v);}
private long sr(){return(s.size()==0)?0:s.peek();}
long t0;
private int _0(){
    gw(1,1,999999);
    gw(2,1,9);
    return 1;
}
private int _1(){
    t0=gr(2,1);

    if((gr(2,1)+1)!=0)return 3;else return 2;
}
private int _2(){
    return 23;
}
private int _3(){
    if((t0)!=0)return 11;else return 4;
}
private int _4(){
    sa(1);
    return 5;
}
private int _5(){
    sa(1);
    sa(gr(1,0)-120);
    return 6;
}
private int _6(){
    if(sp()!=0)return 10;else return 7;
}
private int _7(){
    sa(sp()+1L);

    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    sa(sr());

    if(sp()!=0)return 9;else return 8;
}
private int _8()throws java.io.IOException{
    sp();
    sa(sp()-1L);

    sa(sr());
    sa(0);
    {long v0=sp();t0=gr(sp(),v0);}
    t0-=48;
    sa(120);
    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    sa(0);
    {long v0=sp();long v1=sp();gw(v1,v0,sp());}
    System.out.print(String.valueOf(t0));
    gw(1,1,gr(1,1)-(gr(3,1)*(gr(4,1)-1)));
    gw(2,1,gr(2,1)-1);
    return 1;
}
private int _9(){
    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    sa(sr());
    sa(0);
    {long v0=sp();sa(gr(sp(),v0));}
    sa(sp()-120L);
    return 6;
}
private int _10(){
    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    sa(sp()-1L);

    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    return 7;
}
private int _11(){
    sa(0);
    sa(gr(2,1));
    sa(gr(2,1)-1);
    sa(gr(2,1)-1);
    return 12;
}
private int _12(){
    if(sp()!=0)return 22;else return 13;
}
private int _13(){
    sp();
    return 14;
}
private int _14(){
    sa(sp()*sp());

    {long v0=sp();long v1=sp();sa(v0);sa(v1);}
    sa(sr());
    return 15;
}
private int _15(){
    if(sp()!=0)return 14;else return 16;
}
private int _16(){
    sp();
    sa(sr());

    if(sp()!=0)return 17;else return 21;
}
private int _17(){
    gw(3,1,sp());
    gw(4,1,1);
    return 18;
}
private int _18(){
    if((gr(3,1)*gr(4,1))<=gr(1,1))return 20;else return 19;
}
private int _19(){
    sa(gr(4,1));
    return 5;
}
private int _20(){
    gw(4,1,gr(4,1)+1);
    return 18;
}
private int _21(){
    gw(3,1,1);
    gw(4,1,1);
    sp();
    return 18;
}
private int _22(){
    sa(sr()-1);
    sa(sr());
    return 12;
}

public void main()throws java.io.IOException{
    int c=0;
    while(c<23){
    switch(c){
    case 0:c=_0();break;
    case 1:c=_1();break;
    case 2:c=_2();break;
    case 3:c=_3();break;
    case 4:c=_4();break;
    case 5:c=_5();break;
    case 6:c=_6();break;
    case 7:c=_7();break;
    case 8:c=_8();break;
    case 9:c=_9();break;
    case 10:c=_10();break;
    case 11:c=_11();break;
    case 12:c=_12();break;
    case 13:c=_13();break;
    case 14:c=_14();break;
    case 15:c=_15();break;
    case 16:c=_16();break;
    case 17:c=_17();break;
    case 18:c=_18();break;
    case 19:c=_19();break;
    case 20:c=_20();break;
    case 21:c=_21();break;
    case 22:c=_22();break;
}
}
}
public static void main(String[]a){try{new Program().main();}catch(java.io.IOException e){}}
}
