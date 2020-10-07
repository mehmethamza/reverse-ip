import requests,re
pages = []

a = input("site:")

def wiew(link) :
    req = requests.get(f"https://viewdns.info/reverseip/?host={a}&t=1",headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    reqs = re.findall("<td>(.*?)</td>",req.text)
    for site in reqs:
        
        pages.append(site)
    
    

wiew(a)
for x in pages:
        with open("f.txt","a") as dosya :
            dosya.write("http://"+x+"/\n")
            dosya.close







