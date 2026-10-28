import json,sys
S=sys.argv[1]; F='/home/user/study/thesis/game/fonts/'
slides=[
 dict(n='',k='COMMUNITY DESIGN SIMULATOR',h='How might we design a community filled with connection?',p='모임 설계자 — 사람 사이의 연결을 설계해 보는 시뮬레이션',img='8_홈_내모임.png',c=[100,16,915,700],cover=1),
 dict(n='01',k='고르기',h='세 가지 모임 중<br>하나를 골라요',p='독서모임, 러닝크루, 플로깅 모임. 사람이 들어오고 머무는 방식이 저마다 달라요.',img='2_모임선택.png',c=[560,84,800,560]),
 dict(n='02',k='설계하기',h='다섯 가지 스킬을<br>나눠 줘요',p='Open · Welcome · Rhythm · Connect · Share',img='3_설계.png',c=[100,168,790,884]),
 dict(n='03',k='지켜보기',h='여덟 번의 모임 동안<br>사람들이 이어지고 떠나요',p='점 하나가 한 사람이에요. 관계가 생기면 가운데로 모여요.',img='6_끝장면.png',c=[880,168,940,884]),
 dict(n='04',k='돌아보기',h='어떤 모임이 되었는지<br>돌아봐요',p='머무는 사람과 공동체 의식으로 모임을 읽어요.',img='7_결과.png',c=[684,84,1136,830]),
 dict(n='05',k='다음 질문',h='그리고 다음 질문을<br>남겨요',p='정답 대신, 이 모임을 다시 설계할 때 생각해 볼 질문이에요.',img='7_결과.png',c=[92,76,584,756]),
 dict(n='06',k='쌓이기',h='관람객이 만든 모임이<br>하나의 지도가 돼요',p='작고 진한 원은 단단한 모임, 크고 옅게 퍼진 원은 느슨한 모임이에요.',img='8_홈_내모임.png',c=[175,150,825,820]),
]
css=f'''@font-face{{font-family:G;src:url(file://{F}GothicA1-Regular-subset.woff2);font-weight:400}}
@font-face{{font-family:G;src:url(file://{F}GothicA1-Bold-subset.woff2);font-weight:700}}
@font-face{{font-family:G;src:url(file://{F}GothicA1-ExtraBold-subset.woff2);font-weight:800}}
*{{box-sizing:border-box;margin:0}}body{{width:1080px;height:1350px;background:#ecebe7;font-family:G,sans-serif;color:#111;overflow:hidden}}
.s{{position:relative;width:1080px;height:1350px;padding:72px 64px 56px;display:flex;flex-direction:column}}
.top{{display:flex;justify-content:space-between;font-family:'Inter Tight';font-weight:600;font-size:22px;letter-spacing:.06em}}
.top span:last-child{{color:#8a8984}}
h1{{font-weight:800;font-size:68px;line-height:1.18;letter-spacing:-.035em;margin-top:44px;word-break:keep-all}}
p{{font-size:26px;line-height:1.5;margin-top:22px;color:#4a4945;word-break:keep-all;max-width:880px}}
.card{{margin-top:auto;border-radius:44px;overflow:hidden;background:#fff;background-repeat:no-repeat}}
.cover h1{{font-family:'Inter Tight';font-weight:600;font-size:92px;line-height:.98;letter-spacing:-.05em;margin-top:40px}}
.cover .card{{margin-top:0}}
.foot{{margin-top:36px;display:flex;justify-content:space-between;font-size:20px;font-weight:700;color:#8a8984}}'''
for i,d in enumerate(slides,1):
    x,y,w,h=d['c']; W=952; H=round(W*h/w)
    if H>860: H=860; W=round(H*w/h)
    sc=W/w
    card=f'<div class="card" style="width:{W}px;height:{H}px;align-self:center;background-image:url(\'file://{S}/insta/src/{d["img"]}\');background-size:{1920*sc:.1f}px {1080*sc:.1f}px;background-position:{-x*sc:.1f}px {-y*sc:.1f}px"></div>'
    if d.get('cover'):
        body=f'<div class="top"><span>{d["k"]}</span><span>GRADUATION EXHIBITION</span></div><div style="margin-top:36px">{card}</div><h1>{d["h"]}</h1><p>{d["p"]}</p>'
    else:
        body=f'<div class="top"><span>{d["n"]}  {d["k"]}</span><span>{i}/{len(slides)}</span></div><h1>{d["h"]}</h1><p>{d["p"]}</p>{card}<div class="foot"><span>모임 설계자</span><span>Community Design Simulator</span></div>'
    html=f'<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600&display=block"><style>{css}</style><div class="s{" cover" if d.get("cover") else ""}">{body}</div>'
    open(f'{S}/insta/s{i}.html','w',encoding='utf-8').write(html)
print(len(slides))
