import requests

urllink = requests.get("https://reqres.in/api/users/2")

print(urllink.url)
print(urllink.status_code)
number = urllink.status_code

assert 200 == number
print("assertion passed")

print(urllink.content)
print(urllink.text)
