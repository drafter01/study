import sys
S=sys.argv[1]
imgs=['1_홈.png','2_모임선택.png','3_설계.png','6_끝장면.png','7_결과.png','8_홈_내모임.png']
css='''*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;background:#ecebe7;display:grid;place-items:center;overflow:hidden}
.m{display:flex;flex-direction:column;align-items:center;filter:drop-shadow(0 40px 50px rgba(0,0,0,.14))}
.mon{width:1000px;background:#e2e1dc;border-radius:26px;padding:16px 16px 0;overflow:hidden}
.scr{width:968px;height:544.5px;border-radius:8px;background-size:cover;background-position:center;outline:10px solid #111;outline-offset:-1px;box-shadow:0 0 0 10px #111}
.chin{height:78px;background:#d6d5cf;margin:0 -16px;margin-top:10px}
.neck{width:200px;height:150px;background:linear-gradient(#c9c8c2,#d9d8d3);clip-path:polygon(8% 0,92% 0,100% 100%,0 100%)}
.base{width:300px;height:14px;border-radius:0 0 10px 10px;background:#cfcec8}'''
for i,f in enumerate(imgs,1):
    open(f'{S}/mock/m{i}.html','w',encoding='utf-8').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style><div class="m"><div class="mon"><div class="scr" style="background-image:url(\'file://{S}/insta/src/{f}\')"></div><div class="chin"></div></div><div class="neck"></div><div class="base"></div></div>')
