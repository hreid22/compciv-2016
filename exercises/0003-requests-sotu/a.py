import requests
url="http://example.com/"
resp= requests.get(url)
resp_txt= resp.text
print(resp.status_code)
print(len(resp_txt))
print(resp.url)
