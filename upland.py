import requests

url = 'https://v6.exchangerate-api.com/v6/ee15a2956a8828023a294906/latest/USD'

response = requests.get(url)
data = response.json()

upland_usd = float(input("How many dollars you have in Upland: "))

upland_tax = 0.95

usd_to_brl = data['conversion_rates']['BRL']

usd_to_brl *= 0.95

real = upland_usd * upland_tax * usd_to_brl

print(f'{real:.2f}')
