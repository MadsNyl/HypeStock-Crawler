from util import http_get


res = http_get("https://www.washingtonpost.com/world/2023/06/17/children-plane-crash-survivors-amazon-colombia/", timeout=20)
print(res)