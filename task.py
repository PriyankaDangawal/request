import requests
import json
url=requests.get("http://join.navgurukul.org/api/partners")
data=url.json()
with open("project_data.json","w") as k:
    json.dump(data,k,indent=4)
list1=[]
list2=[]
serial_no=0
for i in data["data"]:
    patner_name=data["data"]
    id=data["data"]
    print(serial_no+1,("-"),i["name"],(" - "),i["id"])
    list1.append(i["name"])
    list2.append(i["id"])
    serial_no=serial_no+1

y={}
for i in range(len(list1)):
    for k in range(len(list2)):
        y[list1[i]]=(list2[i])
print("     ")

choice=input("enter your choice assending ya dissending(a/d): ")
if choice=="a":
    list3=[]
    for p in y:
        a=y[p]
        list3.append(p)
        list3.append(a)
    n=1
    while n<len(list3):
        j=n+2
        while j<len(list3):
            if list3[n]>list3[j]:
                c=list3[n]
                list3[n]=list3[j]
                list3[j]=c
                p=a
            j=j+2
        n=n+2
    i=0
    m=1
    while i<len(list3):
        print(m,"-",list3[i],list3[i+1])
        m=m+1
        i=i+2

elif choice=="d":
    list_key=[]
    list_value=[]

    for i in range(len(y)):
        max=0
        for x in y:
            if max<y[x]:
                key=x
                max=y[x]
        list_key.append(key)
        list_value.append(max)
        y.pop(key)
    i=0
    s=1
    while i<len(list_value):
        print(s,list_key[i],list_key[i+1])
        s=s+1
        i=i+2

else:
    print("please chhose assending ya dissending\n you have not other choice::")
