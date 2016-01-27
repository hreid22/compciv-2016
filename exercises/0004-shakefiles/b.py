import os
import requests
resp = requests.get("http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz")
shakename = os.path.join('tempdata', 'matty.shakespeare.tar.gz')
zfile = open(shakename, 'wb')
respdata= resp.content
zfile.write(respdata)
zfile.close