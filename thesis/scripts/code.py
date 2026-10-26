import json, re, collections
data=json.load(open("wanted_ux.json"))
CODES={
 "대상: 앱·웹·화면":["앱","웹","모바일","화면","반응형","ui","gui","figma","피그마","디자인 시스템","디자인시스템","인터페이스","대시보드","saas","플랫폼"],
 "대상: 서비스·오프라인 접점":["서비스 디자인","서비스디자인","오프라인","매장","공간","옴니채널","서비스 블루프린트","블루프린트","현장","키오스크","고객 여정","고객여정"],
 "대상: 브랜드·콘텐츠·마케팅":["브랜딩","브랜드","bx","콘텐츠","마케팅","배너","프로모션","상세페이지","sns"],
 "대상: 커뮤니티·관계":["커뮤니티","모임","멤버십","소셜","유저 간","사용자 간","크리에이터","팬"],
 "활동: 사용자 리서치":["리서치","인터뷰","사용성 테스트","사용성테스트","usability","ux 조사","사용자 조사","유저 테스트","fgi"],
 "활동: 데이터·지표":["데이터","지표","a/b","ab 테스트","ga","amplitude","mixpanel","정량"],
 "활동: 구조 설계":["플로우","flow","와이어프레임","wireframe","정보구조","ia","프로토타입","prototype","시나리오","여정","journey"],
 "활동: 시각 디자인":["비주얼","시각","그래픽","아이콘","일러스트","모션","인터랙션"],
 "활동: 개발 협업·QA":["개발자","개발 협업","핸드오프","qa","스펙","가이드"],
}
def has(text,kws):
    t=text.lower()
    for k in kws:
        if re.fullmatch(r"[a-z/ ]+",k) and len(k)<=4:
            if re.search(r"(?<![a-z])"+re.escape(k)+r"(?![a-z])",t): return True
        elif k in t: return True
    return False
n=len(data); cnt=collections.Counter(); comm_examples=[]; svc_examples=[]
for d in data:
    det=d["detail"]; job=" ".join(det.get(k) or "" for k in ["main_tasks","requirements","preferred_points"])+" "+d["position"]
    for c,k in CODES.items():
        if has(job,k): cnt[c]+=1
    if has(job,CODES["대상: 커뮤니티·관계"]): comm_examples.append(d)
    if has(job,CODES["대상: 서비스·오프라인 접점"]): svc_examples.append(d)
print("N=",n)
for c in CODES: print(f"{c}: {cnt[c]} ({cnt[c]/n*100:.0f}%)")
print("\n산업:",collections.Counter(d["industry"] for d in data).most_common(8))
# 커뮤니티 키워드가 어떤 맥락인지 확인
print("\n--- 커뮤니티·관계 키워드 맥락 ---")
for d in comm_examples:
    job=" ".join(d["detail"].get(k) or "" for k in ["main_tasks","requirements","preferred_points"])
    for kw in CODES["대상: 커뮤니티·관계"]:
        for m in re.finditer(re.escape(kw),job.lower()):
            print(d["company"],"|",kw,"|",job[max(0,m.start()-40):m.end()+40].replace("\n"," "))
            break
print("\n--- 서비스·오프라인 키워드 맥락 ---")
for d in svc_examples:
    job=" ".join(d["detail"].get(k) or "" for k in ["main_tasks","requirements","preferred_points"])
    for kw in CODES["대상: 서비스·오프라인 접점"]:
        i=job.lower().find(kw)
        if i>=0: print(d["company"],"|",kw,"|",job[max(0,i-40):i+40].replace("\n"," ")); break
