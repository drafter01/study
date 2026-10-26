import json,time,urllib.request,sys
UA={"User-Agent":"Mozilla/5.0"}
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=20))
res={}
for t in sys.argv[1:]:
    out=[];off=0
    while True:
        d=get(f"https://www.wanted.co.kr/api/v4/jobs?country=kr&tag_type_ids={t}&job_sort=job.latest_order&locations=all&years=-1&limit=100&offset={off}")
        if not d["data"]: break
        out+=[{"id":j["id"],"position":j["position"],"company":j["company"]["name"]} for j in d["data"]]
        off+=100; time.sleep(0.3)
        if off>3000: break
    res[t]=out; print(t,len(out),flush=True)
json.dump(res,open("listing.json","w"),ensure_ascii=False)
