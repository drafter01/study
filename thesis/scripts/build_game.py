"""게임 소스의 글꼴 자리(__PRETENDARD__, __KODDI_R__, __KODDI_B__, __KODDI_EB__, __GOTHIC_*__)에 글꼴을 base64로 넣어 HTML을 만든다.
사용: python3 scripts/build_game.py [소스 파일] [결과 파일]  (기본: game/moim.src.html → game/moim.html)"""
import base64, pathlib, sys
here = pathlib.Path(__file__).resolve().parent.parent / "game"
src_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else here / "moim.src.html"
out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else here / "moim.html"
fonts = {"__PRETENDARD__": "pretendard-variable-subset.woff2", "__KODDI_R__": "KoddiUDOnGothic-Regular.woff2",
         "__KODDI_B__": "KoddiUDOnGothic-Bold.woff2", "__KODDI_EB__": "KoddiUDOnGothic-ExtraBold.woff2",
         "__GOTHIC_R__": "GothicA1-Regular-subset.woff2", "__GOTHIC_B__": "GothicA1-Bold-subset.woff2", "__GOTHIC_EB__": "GothicA1-ExtraBold-subset.woff2"}
src = src_path.read_text(encoding="utf-8")
for key, name in fonts.items():
    if key in src:
        src = src.replace(key, base64.b64encode((here / "fonts" / name).read_bytes()).decode())
# 인트로 이미지: __IMG:파일이름__ → game/intro_img/파일이름 을 data URI로
import re
src = re.sub(r"__IMG:([\w.-]+)__", lambda m: "data:image/jpeg;base64," + base64.b64encode((here / "intro_img" / m.group(1)).read_bytes()).decode(), src)
out_path.write_text(src, encoding="utf-8")
print("built", out_path)
