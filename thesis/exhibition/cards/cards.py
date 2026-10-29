import json
C=[('self','스스로 굴러가는 모임','운영자가 없어도 누군가 처음 온 사람을 맞이해요. 관계가 관계를 부르는 상태예요.',
    '지금 모임을 이끄는 사람들이 빠지면, 누가 그 자리를 이어받을까요?',['처음 온 사람도 작은 일부터 맡아 볼 수 있나요?','모임 일을 몇몇이 나눠서 하고 있나요?'],['S'],'H9',dict(total=30,rooted=10,leaders=3,links=14)),
 ('quiet','조용히 자라는 모임','크지 않지만 다시 오고 자리 잡는 사람이 꾸준히 생겼어요.',
    '회원 수 말고, 우리 모임이 잘 되고 있다는 건 어떻게 알 수 있을까요?',['다시 나온 사람은 몇 명인가요?','두 번째 온 사람이 아는 얼굴을 만났나요?'],['R','C'],'H7 · H6',dict(total=16,rooted=6,leaders=1,links=6)),
 ('crowd','북적이지만 머무르지 않는 모임','많이 왔지만 대부분 아무와도 이어지지 못하고 떠났어요.',
    "처음 온 사람이 '여기 또 와야지' 하고 느낀 순간은 언제였을까요?",['처음 온 사람에게 먼저 말을 건 사람이 있었나요?','사람이 많아져도 한 명 한 명 챙길 수 있나요?'],['W'],'H3 · H6',dict(total=42,rooted=3,leaders=0,links=2)),
 ('closed','끈끈하지만 닫힌 모임','안쪽은 깊이 연결됐지만 바깥에서 들어오기 어려워요.',
    '오래된 멤버는 편하고, 새로 온 사람도 어색하지 않으려면 어떻게 해야 할까요?',['새로 온 사람도 쉽게 낄 수 있는 활동이 있나요?','오래된 멤버가 새 멤버를 챙겨 줄 수 있나요?'],['O','W'],'H8 · H4',dict(total=10,rooted=6,leaders=1,links=14)),
 ('burn','운영자가 지친 모임','모든 일이 한 사람에게 몰려 운영자가 먼저 지쳤어요.',
    '운영자 말고도 "이건 제가 할게요" 할 수 있는 일이 있었나요?',['운영자만 할 수 있는 일과 누구나 할 수 있는 일을 나눠 봤나요?','돕고 싶어 하는 사람에게 처음 부탁할 일은 무엇인가요?'],['S'],'H9',dict(total=22,rooted=4,leaders=0,links=4)),
 ('root','아직 뿌리내리지 못한 모임','사람이 오고 갔지만 자리 잡은 사람이 적어요.',
    '한 번 온 사람이 다시 와야 할 이유가 있을까요?',['다음 모임 날짜가 정해져 있나요?','다시 왔을 때 반겨 줄 사람이 있나요?'],['R','W'],'H7 · H2',dict(total=8,rooted=1,leaders=0,links=0))]
SK={'O':('Open','문 열기'),'W':('Welcome','반겨 주기'),'R':('Rhythm','정기 모임'),'C':('Connect','서로 알기'),'S':('Share','역할 나누기')}
F='/home/user/study/thesis/game/fonts/pretendard-variable-subset.woff2'
def glyph(r,V,u):
    cl=lambda x,a,b:max(a,min(b,x))
    tot=max(3,r['total']);ro=r['rooted'];le=r['leaders']
    coh=cl(r['links']/max(1,ro)/1.4,0,1)
    halo=u*(.16+tot*.024);core=u*min(.36,.07+ro*.026);mid=core*(1.25+.6*(1-coh))
    hc,ho,cc,co,mc,mo='#a9c6f7',.07+.09*(1-coh),'#2f6fe0',.25+.72*coh,'#7fa6f2',.12+.3*coh
    if V=='closed':halo=core*1.25;cc='#173a86';co=.95;mc='#2f55b0';mo=.7
    if V=='crowd':core=max(u*.1,core*.7);mid=core*1.4;ho=.16
    if V=='root':halo*=.6;co=.3;mo=.12
    if V=='burn':hc='#c9c8c2';mc='#c9c8c2'
    halo=min(halo,u*.82)
    s=f'<circle r="{halo:.1f}" fill="{hc}" fill-opacity="{ho*2.2:.2f}"/><circle r="{mid:.1f}" fill="{mc}" fill-opacity="{mo*1.4:.2f}"/>'
    s+=(f'<circle r="{core:.1f}" fill="none" stroke="#2f6fe0" stroke-width="{u*.05:.1f}" stroke-dasharray="{u*.09:.1f} {u*.07:.1f}" stroke-opacity=".7"/>' if V=='burn' else f'<circle r="{core:.1f}" fill="{cc}" fill-opacity="{co:.2f}"/>')
    if le:s+=f'<circle r="{u*(.04+le**.5*.035):.1f}" fill="#0d2766"/>'
    return s
css=f'''@font-face{{font-family:P;src:url(file://{F});font-weight:100 900}}
*{{box-sizing:border-box;margin:0}}body{{background:#d9d8d2;font-family:P,sans-serif;color:#111}}
.card{{width:1050px;height:1480px;border-radius:44px;overflow:hidden;position:relative;display:flex;flex-direction:column}}
.front{{background:#f4f3ef;padding:84px 80px 76px}}
.top{{display:flex;justify-content:space-between;font-size:26px;font-weight:600;letter-spacing:.06em;color:#8a8984}}
.art{{flex:1;display:grid;place-items:center}}
.front h1{{font-size:84px;font-weight:800;line-height:1.12;letter-spacing:-.04em;word-break:keep-all}}
.front p{{font-size:32px;line-height:1.55;color:#55544f;margin-top:26px;word-break:keep-all}}
.foot{{display:flex;justify-content:space-between;margin-top:56px;font-size:24px;font-weight:600;color:#8a8984}}
.back{{background:#ff5a1f;color:#fff;padding:84px 80px 76px}}
.back .top{{color:rgba(255,255,255,.75)}}
.back h2{{font-size:76px;font-weight:800;line-height:1.24;letter-spacing:-.035em;margin-top:90px;word-break:keep-all}}
.think{{margin-top:auto;background:#fff;color:#111;border-radius:32px;padding:44px 46px}}
.think b{{font-size:24px;font-weight:700;color:#8a8984;letter-spacing:.04em}}
.think ul{{margin:18px 0 0;padding-left:34px;font-size:33px;line-height:1.5;word-break:keep-all}}
.think li+li{{margin-top:12px}}
.sk{{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px;align-items:center}}
.sk span{{font-size:22px;font-weight:700;color:#ff5a1f;margin-right:6px}}
.sk em{{display:flex;align-items:center;gap:12px;font-style:normal;background:#f4f3ef;border-radius:999px;padding:6px 20px 6px 6px;font-size:26px;font-weight:700}}
.sk em i{{width:40px;height:40px;border-radius:50%;background:#111;color:#fff;font-style:normal;font-size:19px;display:grid;place-items:center}}
.sk em small{{font-size:20px;color:#8a8984;font-weight:600}}
.back .foot{{color:rgba(255,255,255,.75)}}'''
for i,(k,t,d,q,th,sk,h,r) in enumerate(C,1):
    fr=f'''<div class="card front"><div class="top"><span>MOIM DESIGNER</span><span>{i:02d} / 06</span></div>
<div class="art"><svg width="760" height="760" viewBox="-380 -380 760 760" style="overflow:visible">{glyph(r,k,400)}</svg></div>
<h1>{t}</h1><p>{d}</p><div class="foot"><span>나의 모임 결과</span><span>뒷면에 다음 질문이 있어요 →</span></div></div>'''
    bk=f'''<div class="card back"><div class="top"><span>NEXT QUESTION</span><span>{i:02d} / 06</span></div>
<h2>{q}</h2><div class="think"><b>생각해 볼 것</b><ul>{''.join(f'<li>{x}</li>' for x in th)}</ul>
<div class="sk"><span>다시 설계한다면</span>{''.join(f'<em><i>{c}</i>{SK[c][0]}<small>{SK[c][1]}</small></em>' for c in sk)}</div></div>
<div class="foot"><span>휴리스틱 {h}</span><span>만드는 디자이너, 관계를 설계하다</span></div></div>'''
    for n,b in (('front',fr),('back',bk)):
        open(f'{n}_{i}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style>{b}')
