

import requests

ip = input("Enter your ip address: ")

url = f"https://ipinfo.io/{ip}/json"

response = requests.get(url)
data = response.json()


print("ip address info")
print("________________")
print("ip: ", data.get("ip","N/A"))
print("city: ", data.get("city","N/A"))
print("region: ", data.get("region","N/A"))
print("country: ", data.get("country","N/A"))
print("ISP/org: ", data.get("org","N/A"))