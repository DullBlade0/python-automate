import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
print(len(res.text))
print(res.text[:250])
