"""게임 소스의 자리 표시를 실제 파일로 채워, 파일 하나로 열리는 HTML을 만든다.
- 글꼴: __PRETENDARD__, __KODDI_*__, __GOTHIC_*__ → game/fonts/ 의 글꼴을 base64로
- 인트로 이미지: __IMG:파일이름__ → game/intro_img/ 의 이미지를 data URI로
- 인트로 통째로: __INTRO_B64__ → game/intro.src.html 을 같은 방식으로 채운 뒤 base64로 (시뮬레이터 안에서 재생)
사용: python3 scripts/build_game.py [소스 파일] [결과 파일]
      (기본: game/community_simulator.src.html → game/community_simulator.html)"""
import base64, pathlib, re, sys
here = pathlib.Path(__file__).resolve().parent.parent / "game"
src_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else here / "community_simulator.src.html"
out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else here / "community_simulator.html"
fonts = {"__PRETENDARD__": "pretendard-variable-subset.woff2", "__KODDI_R__": "KoddiUDOnGothic-Regular.woff2",
         "__KODDI_B__": "KoddiUDOnGothic-Bold.woff2", "__KODDI_EB__": "KoddiUDOnGothic-ExtraBold.woff2",
         "__GOTHIC_R__": "GothicA1-Regular-subset.woff2", "__GOTHIC_B__": "GothicA1-Bold-subset.woff2", "__GOTHIC_EB__": "GothicA1-ExtraBold-subset.woff2"}
b64 = lambda data: base64.b64encode(data).decode()


def fill(src):
    for key, name in fonts.items():
        if key in src:
            src = src.replace(key, b64((here / "fonts" / name).read_bytes()))
    return re.sub(r"__IMG:([\w.-]+)__", lambda m: "data:image/jpeg;base64," + b64((here / "intro_img" / m.group(1)).read_bytes()), src)


src = fill(src_path.read_text(encoding="utf-8"))
if "__INTRO_B64__" in src:
    src = src.replace("__INTRO_B64__", b64(fill((here / "intro.src.html").read_text(encoding="utf-8")).encode("utf-8")))
out_path.write_text(src, encoding="utf-8")
print("built", out_path)
