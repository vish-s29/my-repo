##variables,strings,io
#fibonacci series
#def fib(n):
#  fibseries = [0,1]                                    ## assingning what fibseries is
#  for i in range(1,n-1):         
#    fibseries.append(fibseries[-1]+fibseries[-2])      ##formula
#  return fibseries
#c=fib(5)
#print(c)
##lists and tuples

#tuple1=(1,2,3,4)
#tuple2=(1,2,3,5)
#tuplex=tuple1*2
#print(tuplex)

a=int(input("enter a num1"))
b=int(input("enter a num2"))
result=1
i=1
while b>0:
    result=result*a
    b=b-1
print(result)

import requests
import pandas as pd

# Replace with the actual API URL
api_url = 'https://dummyjson.com/posts'

response = requests.get(api_url)
json_data = response.json()

# Example: JSON list of dicts
df = pd.DataFrame(json_data)

# Save to Excel
df.to_excel('data_from_api.xlsx', index=False)


import requests
import pandas as pd

url = "https://dummyjson.com/posts"   # endpoint for posts

try:
    resp = requests.get(url)
    if resp.status_code==200:
        print("success!",resp.status_code)
    else:
        print("fail",resp.status_code)
    resp.raise_for_status()  # will raise an error for non-2xx HTTP codes
  
except Exception as e:
    print("Error fetching data:", e)
    print
    


    