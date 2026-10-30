import math
F='/home/user/study/thesis/game/fonts/pretendard-variable-subset.woff2'
SKC={'O':'#ffd23f','W':'#ff6fae','R':'#3d7bff','C':'#3fd47a','S':'#ff8a2a'}
SK={'O':('Open','문 열기'),'W':('Welcome','반겨 주기'),'R':('Rhythm','정기 모임'),'C':('Connect','서로 알기'),'S':('Share','역할 나누기')}
# (키, 배경, 도형, 글자, 영문, 이름, 설명, 도형의 뜻, 질문, 생각해 볼 것, 스킬, 휴리스틱)
C=[('self','#2153e6','#d6e6ff','#14389e','SELF-RUNNING','스스로 굴러가는\n커뮤니티','운영자가 없어도 누군가 처음 온 사람을 맞이해요.','맞물려 굴러가는 바퀴 — 여러 사람이 서로를 받치며 스스로 굴러가요',
    '지금 커뮤니티를 이끄는 사람들이 빠지면, 누가 그 자리를 이어받을까요?',['처음 온 사람도 작은 일부터 맡아 볼 수 있나요?','커뮤니티 일을 몇몇이 나눠서 하고 있나요?'],['S'],'H9'),
 ('quiet','#1d6a4e','#c9f3a8','#175a3f','QUIETLY GROWING','조용히 자라는\n커뮤니티','크지 않지만 다시 오고 자리 잡는 사람이 꾸준히 생겼어요.','한 겹씩 쌓이는 나이테 — 크지 않아도 겹겹이 자라는 중이에요',
    '회원 수 말고, 우리 커뮤니티가 잘 되고 있다는 건 어떻게 알 수 있을까요?',['다시 나온 사람은 몇 명인가요?','두 번째 온 사람이 아는 얼굴을 만났나요?'],['R','C'],'H7 · H6'),
 ('crowd','#ff4f9a','#ffe55c','#b8135a','CROWDED,\nNOT STAYING','북적이지만\n머무르지 않는\n커뮤니티','많이 왔지만 대부분 아무와도 이어지지 못하고 떠났어요.','틈이 많은 그릇 — 많이 담기지만 틈으로 계속 빠져나가요',
    "처음 온 사람이 '여기 또 와야지' 하고 느낀 순간은 언제였을까요?",['처음 온 사람에게 먼저 말을 건 사람이 있었나요?','사람이 많아져도 한 명 한 명 챙길 수 있나요?'],['W'],'H3 · H6'),
 ('closed','#3a2f9e','#d3ccff','#2e2585','CLOSE-KNIT,\nCLOSED','끈끈하지만\n닫힌 커뮤니티','안쪽은 깊이 연결됐지만 바깥에서 들어오기 어려워요.','두 겹의 담장 — 안은 따뜻하지만 바깥에서 들어갈 문이 보이지 않아요',
    '오래된 멤버는 편하고, 새로 온 사람도 어색하지 않으려면 어떻게 해야 할까요?',['새로 온 사람도 쉽게 낄 수 있는 활동이 있나요?','오래된 멤버가 새 멤버를 챙겨 줄 수 있나요?'],['O','W'],'H8 · H4'),
 ('burn','#e8490f','#ffe8a6','#b0330a','BURNED OUT','운영자가 지친\n커뮤니티','모든 일이 한 사람에게 몰려 운영자가 먼저 지쳤어요.','녹아내리는 초 — 한 사람이 모든 무게를 버티다 녹아내려요',
    '운영자 말고도 "이건 제가 할게요" 할 수 있는 일이 있었나요?',['운영자만 할 수 있는 일과 누구나 할 수 있는 일을 나눠 봤나요?','돕고 싶어 하는 사람에게 처음 부탁할 일은 무엇인가요?'],['S'],'H9'),
 ('root','#0f8f96','#d5f6f0','#0b6268','NOT YET ROOTED','아직 뿌리내리지\n못한 커뮤니티','사람이 오고 갔지만 자리 잡은 사람이 적어요.','땅에 닿지 않은 씨앗 — 아직 뿌리를 내릴 자리를 찾는 중이에요',
    '한 번 온 사람이 다시 와야 할 이유가 있을까요?',['다음 모임 날짜가 정해져 있나요?','다시 왔을 때 반겨 줄 사람이 있나요?'],['R','W'],'H7 · H2')]
def scallop(pts,sweep=1):
    s=f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
    for i in range(len(pts)):
        a=pts[i];b=pts[(i+1)%len(pts)];r=math.dist(a,b)*.56
        s+=f' A{r:.1f},{r:.1f} 0 0 {sweep} {b[0]:.1f},{b[1]:.1f}'
    return s+'Z'
def shape(k,fill,ink):  # 820 x 980 영역
    if k=='self':
        n=16;pts=[(410+330*math.cos(i/n*2*math.pi),470+330*math.sin(i/n*2*math.pi)) for i in range(n)]
        return f'<path d="{scallop(pts)}" fill="{fill}"/>'
    if k=='quiet':  # 아래는 평평, 위로 갈수록 좁아지며 한 겹씩 쌓인 나이테
        s=''
        for j,(w,y) in enumerate([(640,820),(560,660),(470,510),(370,370),(260,240)]):
            s+=f'<rect x="{410-w/2}" y="{y-150}" width="{w}" height="{170}" rx="85" fill="{fill}"/>'
        return s+f'<rect x="90" y="760" width="640" height="170" rx="40" fill="{fill}"/>'
    if k=='crowd':  # 크게 퍼졌지만 가장자리마다 틈(홈)이 파인 그릇
        P=[(70,150),(300,110),(360,200),(420,100),(760,150),(700,380),(780,430),(740,700),(620,690),(640,880),(380,860),(330,760),(270,880),(60,820),(130,560),(40,500),(110,360)]
        pts=' '.join(f'{x},{y}' for x,y in P)
        return f'<polygon points="{pts}" fill="{fill}" stroke="{fill}" stroke-width="70" stroke-linejoin="round"/>'
    if k=='closed':  # 두 겹의 담장
        return (f'<rect x="80" y="130" width="660" height="720" rx="120" fill="{fill}"/>'
                f'<rect x="120" y="170" width="580" height="640" rx="88" fill="none" stroke="{ink}" stroke-width="6"/>'
                f'<rect x="138" y="188" width="544" height="604" rx="76" fill="none" stroke="{ink}" stroke-width="2"/>')
    if k=='burn':  # 위는 반듯하고 아래로 흘러내리는 초
        s=f'<rect x="100" y="120" width="620" height="460" rx="40" fill="{fill}"/>'
        for x,w,h in [(100,140,590),(260,110,470),(390,150,700),(560,160,520)]:
            s+=f'<rect x="{x}" y="400" width="{w}" height="{h}" rx="{w/2}" fill="{fill}"/>'
        return s
    if k=='root':  # 아래가 뾰족한 씨앗, 땅(선)과 떨어져 떠 있음
        return (f'<path d="M110,170 Q110,110 170,110 L650,110 Q710,110 710,170 L710,560 Q710,610 670,640 L450,800 Q410,830 370,800 L150,640 Q110,610 110,560 Z" fill="{fill}"/>'
                '')
TPOS={'self':470,'quiet':540,'crowd':480,'closed':490,'burn':330,'root':380}
css=f'''@font-face{{font-family:P;src:url(file://{F});font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}body{{background:#111;font-family:P,sans-serif}}
.card{{width:1050px;height:1480px;position:relative;overflow:hidden;background:var(--bg);color:var(--sh)}}
.mono{{font-family:"DejaVu Sans Mono",ui-monospace,monospace;font-weight:400;letter-spacing:.02em}}
.c-t{{position:absolute;top:58px;left:64px;right:64px;display:flex;justify-content:space-between;font-size:26px}}
.art{{position:absolute;left:66px;top:128px;width:918px;height:1097px}}
.ttl{{position:absolute;left:66px;width:918px;text-align:center;color:var(--ink);font-size:78px;font-weight:700;line-height:1.12;letter-spacing:-.04em;white-space:pre-line;word-break:keep-all}}
.c-b{{position:absolute;left:64px;right:64px;bottom:58px;display:flex;justify-content:space-between;align-items:end;gap:40px}}
.c-b p{{font-size:27px;line-height:1.5;max-width:560px;word-break:keep-all}}
.c-b p b{{display:block;font-weight:700;margin-bottom:6px}}
.c-b .en{{font-size:30px;text-align:right;white-space:pre-line;line-height:1.2}}
.pan{{position:absolute;border-radius:44px;background:var(--sh);color:var(--ink)}}
.q{{left:40px;right:40px;top:40px;height:820px;padding:56px 60px;display:flex;flex-direction:column}}
.q small{{font-size:26px}}
.q h2{{margin-top:auto;margin-bottom:auto;font-size:76px;font-weight:700;line-height:1.24;letter-spacing:-.035em;word-break:keep-all}}
.th{{left:40px;width:610px;top:880px;bottom:40px;padding:48px 50px;background:color-mix(in srgb,var(--sh) 55%,var(--bg))}}
.th small{{font-size:24px}}
.th ul{{margin:22px 0 0;padding-left:30px;font-size:33px;line-height:1.5;font-weight:600;word-break:keep-all}}
.th li+li{{margin-top:14px}}
.sk{{left:670px;right:40px;top:880px;bottom:40px;padding:44px 34px;display:flex;flex-direction:column;gap:14px;background:#fff}}
.sk small{{font-size:22px}}
.sk em{{font-style:normal;font-size:34px;font-weight:700;display:flex;align-items:center;gap:12px}}
.sk em i{{width:46px;height:46px;border-radius:50%;background:var(--ink);color:#fff;font-style:normal;font-size:21px;display:grid;place-items:center;flex:none}}
.sk em span{{display:block;font-size:20px;font-weight:600;opacity:.6}}
.sk .h{{margin-top:auto;font-size:22px}}
.mini{{position:absolute;right:70px;top:52px;width:110px;height:132px}}'''
for i,(k,bg,sh,ink,en,t,d,mean,q,th,sk,h) in enumerate(C,1):
    v=f'--bg:{bg};--sh:{sh};--ink:{ink}'
    fr=f'''<div class="card" style="{v}"><div class="c-t mono"><span>COMMUNITY</span></div>
<svg class="art" viewBox="0 0 820 980">{shape(k,sh,ink)}</svg><div class="ttl" style="top:{128+TPOS[k]*1.12-105:.0f}px">{t}</div>
<div class="c-b"><p><b>{d}</b></p><div class="en mono">{en}</div></div></div>'''
    bk=f'''<div class="card" style="{v}"><div class="pan q"><small class="mono">NEXT QUESTION</small><h2>{q}</h2></div>
<div class="pan th"><small class="mono">생각해 볼 것</small><ul>{''.join(f'<li>{x}</li>' for x in th)}</ul></div>
<div class="pan sk"><small class="mono">다시 설계한다면</small>{''.join(f'<em><i style="background:{SKC[x]};color:#111">{x}</i><div>{SK[x][0]}<span>{SK[x][1]}</span></div></em>' for x in sk)}</div></div>'''
    for n,b in (('front',fr),('back',bk)):open(f'{n}_{i}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style>{b}')
