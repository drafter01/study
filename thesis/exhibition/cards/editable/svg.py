# 카드 데이터와 도형은 make.py에서 그대로 가져와, 글자가 <text>로 살아 있는 SVG를 만든다
import re,html
src=open('make.py',encoding='utf-8').read()
exec(src.split("TPOS=")[0])          # SK, C, scallop, shape
TPOS={'self':470,'quiet':540,'crowd':480,'closed':490,'burn':330,'root':380}
FB="Pretendard, 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif";FM="'IBM Plex Mono', 'DejaVu Sans Mono', 'Courier New', monospace"
def w(ch,fs): return fs*(1.0 if ord(ch)>0x2e80 else .58 if ch!=' ' else .3)
def wrap(t,fs,maxw):
    out=[]
    for para in t.split('\n'):
        line='';
        for word in para.split(' '):
            cand=(line+' '+word).strip()
            if sum(w(c,fs) for c in cand)>maxw and line: out.append(line);line=word
            else: line=cand
        out.append(line)
    return out
E=html.escape
def T(x,y,lines,fs,fill,weight=400,lh=1.3,anchor='start',fam=FB,ls=0):
    s=f'<text x="{x}" y="{y}" font-family="{E(fam)}" font-size="{fs}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">'
    for i,l in enumerate(lines): s+=f'<tspan x="{x}" dy="{0 if i==0 else fs*lh:.1f}">{E(l)}</tspan>'
    return s+'</text>'
def mix(a,b,t):
    a=[int(a[i:i+2],16) for i in (1,3,5)];b=[int(b[i:i+2],16) for i in (1,3,5)]
    return '#'+''.join(f'{round(x+(y-x)*t):02x}' for x,y in zip(a,b))
def svg(body): return f'<svg xmlns="http://www.w3.org/2000/svg" width="105mm" height="148mm" viewBox="0 0 1050 1480">{body}</svg>'
for i,(k,bg,sh,ink,en,t,d,mean,q,th,sk,h) in enumerate(C,1):
    # 앞면
    b=f'<g id="background"><rect width="1050" height="1480" fill="{bg}"/></g>'
    b+=f'<g id="shape" transform="translate(66 128) scale(1.12)">{shape(k,sh,ink)}</g>'
    tl=t.split('\n');ty=128+TPOS[k]*1.12-105+70
    b+='<g id="title">'+T(525,ty,tl,78,ink,700,1.12,'middle',ls=-3)+'</g>'
    b+='<g id="labels">'+T(64,84,['COMMUNITY'],26,sh,fam=FM)+T(986,84,[f'{i:02d} / 06'],26,sh,anchor='end',fam=FM)
    enl=en.split('\n');b+=T(986,1422-36*(len(enl)-1),enl,30,sh,lh=1.2,anchor='end',fam=FM)+'</g>'
    dl=wrap(d,27,560);ml=wrap(mean,27,560);yy=1422-40*(len(dl)+len(ml)-1)
    b+='<g id="description">'+T(64,yy,dl,27,sh,700,1.5)+T(64,yy+40*len(dl),ml,27,sh,400,1.5)+'</g>'
    open(f'svg/front_{i:02d}.svg','w',encoding='utf-8').write(svg(b))
    # 뒷면
    b=f'<g id="background"><rect width="1050" height="1480" fill="{bg}"/></g>'
    b+=f'<g id="panel-question"><rect x="40" y="40" width="970" height="820" rx="44" fill="{sh}"/>'+T(100,122,[f'NEXT QUESTION — {i:02d}'],26,ink,fam=FM)
    b+=f'<g transform="translate(870 52) scale(.134)">{shape(k,ink,sh)}</g>'
    ql=wrap(q,76,800);qy=450-(len(ql)-1)*94/2
    b+=T(100,qy,ql,76,ink,700,1.24,ls=-2.5)+'</g>'
    b+=f'<g id="panel-think"><rect x="40" y="880" width="610" height="560" rx="44" fill="{mix(sh,bg,.45)}"/>'+T(90,950,['생각해 볼 것'],24,ink,fam=FM)
    y=1015
    for x in th:
        ll=wrap(x,33,470);b+=f'<circle cx="104" cy="{y-11}" r="6" fill="{ink}"/>'+T(126,y,ll,33,ink,600,1.5);y+=50*len(ll)+14
    b+='</g>'
    b+=f'<g id="panel-skill"><rect x="670" y="880" width="340" height="560" rx="44" fill="#ffffff"/>'+T(704,945,['다시 설계한다면'],22,ink,fam=FM)
    y=1000
    for x in sk:
        b+=f'<circle cx="727" cy="{y+12}" r="23" fill="{ink}"/>'+T(727,y+20,[x],21,'#ffffff',700,anchor='middle')+T(764,y+14,[SK[x][0]],34,ink,700)+T(764,y+44,[SK[x][1]],20,ink,600)
        y+=80
    b+='</g>'
    open(f'svg/back_{i:02d}.svg','w',encoding='utf-8').write(svg(b))
print('ok')
