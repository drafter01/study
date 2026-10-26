import json,re
D=json.load(open("main_data.json")); J=D["jobs"]
ux=[J[str(i)] if str(i) in J else J.get(i) for i in D["ux_ids"]]
ux=[x for x in ux if x]
cand=re.compile(r"오프라인|현장|매장|공간|하드웨어|디바이스|기기|키오스크|차량|모임|커뮤니티|사용자 간|유저 간|관계|소셜|멤버 간|이웃|팬덤|크리에이터|서비스 블루프린트|블루프린트|옴니채널|고객 여정|행사|이벤트 현장",re.I)
print(len(ux))
for x in ux:
    mt=x["detail"].get("main_tasks") or ""
    hits=set(m.group(0) for m in cand.finditer(mt))
    if hits:
        snip=[]
        for h in list(hits)[:3]:
            k=mt.find(h); snip.append(mt[max(0,k-45):k+35].replace("\n"," "))
        print(f"[{x['id']}] {x['company']} | {x['position'][:30]} || "+" ## ".join(snip))
