import requests
for x in range(8):
	if x == 0:
		url="https://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-address-joint-session-congress"
	if x == 1: 
		url = "https://www.whitehouse.gov/the-press-office/remarks-president-state-union-address"
	if x == 2:
		url="https://www.whitehouse.gov/the-press-office/2011/01/25/remarks-president-state-union-address"
	if x ==3:
		url ="https://www.whitehouse.gov/the-press-office/2012/01/24/remarks-president-state-union-address"
	if x ==4:
		url="https://www.whitehouse.gov/the-press-office/2013/02/12/remarks-president-state-union-address"
	if x ==5:
		url ="https://www.whitehouse.gov/the-press-office/2014/01/28/president-barack-obamas-state-union-address"
	if x == 6:
		url= "https://www.whitehouse.gov/the-press-office/2015/01/20/remarks-president-state-union-address-january-20-2015"
	if x== 7:
		url="https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/"
	resp = requests.get(url)
	resp_txt= requests.get(url).text
	print(resp.url)
	print(len(resp_txt))
	print(resp_txt.upper().count('APPLAUSE'))