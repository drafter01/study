"""moim.src.html의 __PRETENDARD__ 자리에 글꼴을 base64로 넣어 moim.html을 만든다."""
import base64, pathlib
here = pathlib.Path(__file__).resolve().parent.parent / "game"
font = base64.b64encode((here / "fonts" / "pretendard-variable-subset.woff2").read_bytes()).decode()
src = (here / "moim.src.html").read_text(encoding="utf-8")
(here / "moim.html").write_text(src.replace("__PRETENDARD__", font), encoding="utf-8")
print("built", here / "moim.html")
