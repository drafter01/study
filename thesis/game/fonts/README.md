# 글꼴
- pretendard-variable-subset.woff2: Pretendard Variable 1.3.9 (SIL Open Font License 1.1, https://github.com/orioncactus/pretendard)를 KS X 1001 한글 2,350자 + 영문·숫자·기호로 줄인 것
- moim.src.html의 __PRETENDARD__ 자리에 base64로 넣어 moim.html을 만든다 (scripts/build_game.py). 전시장에서 인터넷이 없어도 본문 글꼴이 유지됨
- KoddiUDOnGothic-Regular/Bold/ExtraBold.woff2: KoddiUD 온고딕 (한국장애인개발원, npm koddiud-ongothic 1.0.0). 상업·비상업 디자인과 2차 저작물에 자유롭게 사용 가능, 서체 판매·유통과 서체 데이터 수정·개작은 금지 → 파일을 고치지 않고(서브셋 없이) 그대로 base64로 넣음 (v0.7부터 본문 글꼴)
- GothicA1-Regular/Bold/ExtraBold-subset.woff2: Gothic A1 (HanYang I&C, SIL Open Font License 1.1, google/fonts ofl/gothica1)를 KS X 1001 한글 2,350자 + 영문·숫자·기호로 줄인 것. OFL은 서브셋을 허용(파생 글꼴 이름 규정은 GothicA1-OFL.txt 참고). v1.5부터 본문 글꼴 (연구자 요청으로 KoddiUD 온고딕에서 변경)

## Unbounded (첫 화면 영문 질문)
- `Unbounded-latin.woff2`: Google Fonts의 Unbounded 가변 글꼴, 라틴 글자만. SIL Open Font License 1.1 (NamelessDesign). 수정 없이 그대로 사용
