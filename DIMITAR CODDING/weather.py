import requests
import time
city = input('Enter city name: ')
print('Displaying Weather report for' , city)

url = 'https://wttr.in/{} '.format(city)
res = requests.get(url)

print(res.text)