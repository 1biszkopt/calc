import requests 
r = requests.get('https://api.minecraftservices.com/')  
print(r.status_code) 
print(r.elapsed)
