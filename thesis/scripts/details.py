import json,time,urllib.request,re
UA={"User-Agent":"Mozilla/5.0"}
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20))
L=json.load(open("listing.json"))
ux_ids=[]; 
for t in ["599","10530","597"]:
    for j in L[t]:
        if j["id"] not in ux_ids: ux_ids.append(j["id"])
comm_re=re.compile(r"커뮤니티|모임|멤버십|커뮤니케이터|community",re.I)
comm=[]
for t in ["554","523","565","559","721","599","10530","597"]:
    for j in L[t]:
        if comm_re.search(j["position"]): comm.append((t,j["id"]))
print("UX union",len(ux_ids),"community-titled",len(comm))
want=set(ux_ids)|{i for _,i in comm}
cache={}
for i in want:
    try:
        j=get(f"https://www.wanted.co.kr/api/v4/jobs/{i}")["job"]
        cache[i]={"id":i,"company":j["company"]["name"],"industry":j["company"].get("industry_name"),"position":j["position"],"detail":j["detail"],"category_tags":j.get("category_tags")}
    except Exception as e: print("err",i,e)
    time.sleep(0.25)
json.dump({"ux_ids":ux_ids,"comm":comm,"jobs":cache},open("main_data.json","w"),ensure_ascii=False)
print("fetched",len(cache))
