import requests

url = "https://students.amrita.edu/client/class-attendance"   # endpoint for posts


resp = requests.get(url)
if resp.status_code==200:
        print("success!",resp.status_code)
else:
        print("fail",resp.status_code)

