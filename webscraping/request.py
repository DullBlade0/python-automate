import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
len(res.text)
print(res.text[:250])
