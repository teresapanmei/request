import requests
import json
def request():
    a = requests.get("http://saral.navgurukul.org/api/courses")
    x=a.json()
    with open("detail.json","w") as f:
        json.dump(x,f,indent=4)
    with open("detail.json","r") as f:
        data = json.load(f)
    id= [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i+1,":",data['availableCourses'][i]['name'],"---",data['availableCourses'][i]['id'])
        id.append(data['availableCourses'][i]['id'])
        i+=1
    user= int(input("enter any ID you want:"))-1
    ex=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
    a=ex.json()
    with open ("url link2.json","w")as k:
        json.dump(a,k,indent=4)
    with open ("url link2.json","r") as k:
        c=json.load(k)
    j=0
    l=0
    slug=[]
    while j<len(c["data"]):
        print(l+1,c["data"][j]["name"])
        slug.append(c['data'][j]["slug"])
        l=l+1
        j=j+1
    slugname=int(input("Enter your slug number:"))-1
    sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=sluglist.json()
    with open("slunglist.json","w") as k:
        json.dump(b,k,indent=4)
    with open("slunglist.json","r") as k:
        d=json.load(k)
    s=d["name"]
    u=d["content"]
    print(s)
    print(u)
request()

