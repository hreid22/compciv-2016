import os
import requests
os.makedirs("tempdata", exist_ok= True)
baby= requests.get("http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt")
babyplace = os.path.join("tempdata", os.path.basename("http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt"))
baby_txt=baby.text
baby_open=open(babyplace, 'w')
baby_open.write(baby_txt)
length=len(baby_txt)
print("There are", length, "characters in", babyplace)