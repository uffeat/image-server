import requests

url = 'https://image-server.anvil.app/_/theme/index.html'



r = requests.get(url)
if r.status_code == 200:
    text = r.text
    