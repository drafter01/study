import json, time, urllib.request, sys
UA={"User-Agent":"Mozilla/5.0"}
def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=20))
ids=[]; off=0
while len(ids)<int(sys.argv[1]):
    d=get(f"https://www.wanted.co.kr/api/v4/jobs?country=kr&tag_type_ids=599&job_sort=job.latest_order&locations=all&years=-1&limit=20&offset={off}")
    if not d["data"]: break
    ids+= [j["id"] for j in d["data"]]; off+=20; time.sleep(0.3)
out=[]
for i in ids[:int(sys.argv[1])]:
    try:
        j=get(f"https://www.wanted.co.kr/api/v4/jobs/{i}")["job"]
        out.append({"id":i,"company":j["company"]["name"],"industry":j["company"].get("industry_name"),
            "position":j["position"],"detail":j["detail"],"category_tags":j.get("category_tags")})
    except Exception as e: print("err",i,e)
    time.sleep(0.3)
json.dump(out,open("wanted_ux.json","w"),ensure_ascii=False,indent=1)
print(len(out))
