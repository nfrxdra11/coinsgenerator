import json
password=input("accounts password :")
List=[]
for _ in open("emails.txt").read().split("\n"):
 List.append({"email":_,"password":password,"device":None})
open("accounts.json","w").write(json.dumps(List))
