import os
os.system("pip freeze > rewlibcheck.txt")
files=open("rewlibcheck.txt").read()
if "samino" not in files:
	os.system("pip install samino")
	os.remove("rewlibcheck.txt")
if os.path.exists("rewlibcheck.txt"):
	os.remove("rewlibcheck.txt")
import json
import samino
from datetime import datetime
from time import sleep
slep=int(input("how time you want to sleep (best for nice internet is 15 but bad is 12) :"))
RED="\033[1;31m"
GREEN="\033[1;32m"
def timezone():
	timezones ={1: -120, 2: -180, 3: -240, 4: -300, 5: -360, 6: -420, 7: -480, 8: -540, 9: -600, 10: -660, 11: -720, 12: -780, 13: 600, 14: 540, 15: 480, 16: 420, 17: 360, 18: 300, 19: 240, 20: 180, 21: 120, 22: 60, 23: 0}
	return int(timezones[datetime.utcnow().hour])
def get_timers():
	return [{"start":int(datetime.timestamp(datetime.now())),"end":int(datetime.timestamp(datetime.now()))+300} for _ in range(36)]
community = input("community accounts online in :")
accounts = open("accounts.json").read()
accounts = json.loads(accounts)
for account_info in accounts:
		email = account_info["email"]
		dev=account_info["device"]
		pas=account_info["password"]
		clint = samino.Client(deviceId=dev)
		try:
			clint.login(email,pas)
		except Exception as e:
			print(f"account error {e}")
			input()
			clint.login(email,pas)
		comId=clint.get_from_link(link=community).comId
		clint.join_community(comId)
		local = samino.Local(comId=comId)
		x=1
		for _ in range(24):
			local.send_active_time(timers=get_timers(),tz=timezone())
			print(f"{GREEN}{x} request has sent to {RED}{email}");x+=1
			sleep(slep)
		print(f"{GREEN}end this account :{RED}{email}")
