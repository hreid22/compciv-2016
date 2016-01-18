import requests
url="https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/"
resp= requests.get(url)
resp_txt = resp.text
print(resp_txt.count('Applause'))
print(resp_txt.upper().count('APPLAUSE'))
print(resp_txt.count('<p>'))