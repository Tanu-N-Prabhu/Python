import requests
import json


# server = "https://cdn-api.co-vin.in/api"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate", "accpet": "application/json", "Content-Type": "application/json"}

# user_auth_api = "/v2/auth/public/generateOTP"

# response = requests.post(server + user_auth_api, headers=headers, data={"mobile":"7893273022"})
# print(response.text)

# get_states = "/v2/admin/location/states"
# response = requests.get(server + get_states, headers=headers)
# print(response.text)


r = requests.get("https://google.com")
print(r.status_code)
print(r.headers['Content-Type'])
print(r.encoding)
print(r.text) 