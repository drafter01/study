import math,random
F='/home/user/study/thesis/game/fonts/pretendard-variable-subset.woff2'
SK={'O':('Open','문 열기'),'W':('Welcome','반겨 주기'),'R':('Rhythm','정기 모임'),'C':('Connect','서로 알기'),'S':('Share','역할 나누기')}
C=[('self','#16b04a','SELF-RUNNING','스스로 굴러가는\n커뮤니티','운영자가 없어도 누군가 처음 온 사람을 맞이해요. 관계가 관계를 부르는 상태예요.',
    '지금 커뮤니티를 이끄는 사람들이 빠지면, 누가 그 자리를 이어받을까요?',['처음 온 사람도 작은 일부터 맡아 볼 수 있나요?','커뮤니티 일을 몇몇이 나눠서 하고 있나요?'],['S'],'H9'),
 ('quiet','#8acb12','QUIETLY GROWING','조용히 자라는\n커뮤니티','크지 않지만 다시 오고 자리 잡는 사람이 꾸준히 생겼어요.',
    '회원 수 말고, 우리 커뮤니티가 잘 되고 있다는 건 어떻게 알 수 있을까요?',['다시 나온 사람은 몇 명인가요?','두 번째 온 사람이 아는 얼굴을 만났나요?'],['R','C'],'H7 · H6'),
 ('crowd','#ff1f7a','CROWDED, NOT STAYING','북적이지만\n머무르지 않는 커뮤니티','많이 왔지만 대부분 아무와도 이어지지 못하고 떠났어요.',
    "처음 온 사람이 '여기 또 와야지' 하고 느낀 순간은 언제였을까요?",['처음 온 사람에게 먼저 말을 건 사람이 있었나요?','사람이 많아져도 한 명 한 명 챙길 수 있나요?'],['W'],'H3 · H6'),
 ('closed','#1e5bff','CLOSE-KNIT, CLOSED','끈끈하지만\n닫힌 커뮤니티','안쪽은 깊이 연결됐지만 바깥에서 들어오기 어려워요.',
    '오래된 멤버는 편하고, 새로 온 사람도 어색하지 않으려면 어떻게 해야 할까요?',['새로 온 사람도 쉽게 낄 수 있는 활동이 있나요?','오래된 멤버가 새 멤버를 챙겨 줄 수 있나요?'],['O','W'],'H8 · H4'),
 ('burn','#ff6a00','BURNED OUT','운영자가 지친\n커뮤니티','모든 일이 한 사람에게 몰려 운영자가 먼저 지쳤어요.',
    '운영자 말고도 "이건 제가 할게요" 할 수 있는 일이 있었나요?',['운영자만 할 수 있는 일과 누구나 할 수 있는 일을 나눠 봤나요?','돕고 싶어 하는 사람에게 처음 부탁할 일은 무엇인가요?'],['S'],'H9'),
 ('root','#10a7f0','NOT YET ROOTED','아직 뿌리내리지 못한\n커뮤니티','사람이 오고 갔지만 자리 잡은 사람이 적어요.',
    '한 번 온 사람이 다시 와야 할 이유가 있을까요?',['다음 모임 날짜가 정해져 있나요?','다시 왔을 때 반겨 줄 사람이 있나요?'],['R','W'],'H7 · H2')]
def circ(x,y,r):return f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}"/>'
def shape(k):  # 900x900 영역, 같은 색 도형을 겹쳐 하나의 비정형 모양으로
    s=''
    if k=='self':   # 손을 맞잡은 듯 둥근 혹이 이어진 꽃 모양
        s+=circ(450,450,300)
        for i in range(11):a=i/11*2*math.pi;s+=circ(450+330*math.cos(a),450+330*math.sin(a),118)
    elif k=='quiet':  # 아래에서 위로 조금씩 자라는 방울
        for x,y,r in [(450,770,120),(360,640,120),(540,640,120),(450,600,110),(300,470,130),(600,470,130),(450,430,160),(380,270,130),(520,270,130),(450,160,110)]:s+=circ(x,y,r)
    elif k=='crowd':  # 크게 퍼졌지만 서로 떨어진 조각들
        random.seed(3)
        for x,y,r in [(300,300,200),(640,250,120),(700,560,170),(380,640,130),(160,600,70),(560,820,60),(820,380,55),(200,830,45)]:s+=circ(x,y,r)
    elif k=='closed':  # 단단하게 닫힌 각진 덩어리
        pts=[];n=8
        for i in range(n):a=i/n*2*math.pi+math.pi/8;pts.append(f'{450+400*math.cos(a):.0f},{450+400*math.sin(a):.0f}')
        s+=f'<polygon points="{" ".join(pts)}" stroke-linejoin="round" stroke-width="60" stroke="currentColor"/>'
    elif k=='burn':  # 위는 둥글고 아래로 녹아내리는 모양
        s+='<rect x="120" y="140" width="660" height="380" rx="190"/>'
        for x,w,h in [(170,110,520),(330,90,360),(470,120,640),(640,100,430)]:s+=f'<rect x="{x}" y="300" width="{w}" height="{h}" rx="{w/2}"/>'
    elif k=='root':  # 땅에 닿지 못하고 떠 있는 작은 방울들
        for x,y,r in [(430,380,210),(600,300,140),(300,520,120),(560,560,90),(700,700,55),(260,760,40),(470,800,30)]:s+=circ(x,y,r)
    return s
css=f'''@font-face{{font-family:P;src:url(file://{F});font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}body{{background:#cfcfcb;font-family:P,sans-serif}}
.card{{width:1050px;height:1480px;background:#fff;position:relative;overflow:hidden;color:var(--c)}}
.lbl{{position:absolute;font-weight:800;font-size:46px;letter-spacing:-.01em;line-height:1}}
.tl{{left:64px;top:64px}}.tr{{right:64px;top:64px}}.br{{right:64px;bottom:64px;text-align:right;font-size:38px!important}}
.art{{position:absolute;left:75px;top:170px;width:900px;height:900px;fill:var(--c);color:var(--c)}}
.bl{{position:absolute;left:64px;bottom:64px;width:520px}}
.bl h1{{font-size:62px;font-weight:800;line-height:1.16;letter-spacing:-.035em;white-space:pre-line;word-break:keep-all}}
.bl p{{font-size:23px;line-height:1.5;font-weight:600;margin-top:16px;word-break:keep-all;opacity:.85}}
.grain{{position:absolute;inset:0;pointer-events:none;opacity:.18;mix-blend-mode:multiply}}
.back h2{{position:absolute;left:64px;right:80px;top:170px;font-size:72px;font-weight:800;line-height:1.25;letter-spacing:-.035em;word-break:keep-all;color:#111}}
.think{{position:absolute;left:64px;right:64px;bottom:170px;border-top:6px solid var(--c);padding-top:34px}}
.think b{{font-size:26px;font-weight:800;letter-spacing:.02em}}
.think ul{{margin:16px 0 0;padding-left:34px;font-size:34px;line-height:1.5;color:#111;word-break:keep-all}}
.think li+li{{margin-top:10px}}
.sk{{display:flex;gap:12px;margin-top:30px;align-items:center;flex-wrap:wrap}}
.sk span{{font-size:24px;font-weight:800}}
.sk em{{display:flex;align-items:center;gap:12px;font-style:normal;border:4px solid var(--c);border-radius:999px;padding:4px 20px 4px 4px;font-size:27px;font-weight:800;color:#111}}
.sk em i{{width:40px;height:40px;border-radius:50%;background:var(--c);color:#fff;font-style:normal;font-size:19px;display:grid;place-items:center}}
.sk em small{{font-size:20px;color:#777;font-weight:600}}
.blob{{position:absolute;right:-110px;top:610px;width:380px;height:380px;fill:var(--c)}}'''
G='<svg class="grain" width="1050" height="1480"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2"/><feColorMatrix values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 1 0"/></filter><rect width="1050" height="1480" filter="url(#n)"/></svg>'
for i,(k,c,en,t,d,q,th,sk,h) in enumerate(C,1):
    fr=f'''<div class="card" style="--c:{c}"><svg class="art" viewBox="0 0 900 900">{shape(k)}</svg>
<div class="lbl tl">COMMUNITY</div><div class="lbl tr">{i:02d}</div><div class="lbl br">{en.replace(", ",",<br>")}</div>
<div class="bl"><h1>{t}</h1><p>{d}</p></div>{G}</div>'''
    bk=f'''<div class="card back" style="--c:{c}"><svg class="blob" viewBox="0 0 900 900">{shape(k)}</svg>
<div class="lbl tl">NEXT QUESTION</div><h2>{q}</h2>
<div class="think"><b>생각해 볼 것</b><ul>{''.join(f'<li>{x}</li>' for x in th)}</ul>
<div class="sk"><span>다시 설계한다면</span>{''.join(f'<em><i>{x}</i>{SK[x][0]}<small>{SK[x][1]}</small></em>' for x in sk)}</div></div>
<div class="lbl br" style="font-size:26px!important">휴리스틱 {h}</div><div class="lbl" style="left:64px;bottom:64px;font-size:26px">만드는 디자이너, 관계를 설계하다</div>{G}</div>'''
    for n,b in (('front',fr),('back',bk)):open(f'{n}_{i}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style>{b}')
