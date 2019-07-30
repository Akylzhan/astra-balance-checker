import requests 
import re

URL = "http://epay.transcard.kz/"
#The url from which we get second token
URL2 = 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeGoI8UAAAAAAUR-ZPuceq9RsmUfJYCKhG-m7D1&co=aHR0cDovL2VwYXkudHJhbnNjYXJkLmt6Ojgw&hl=en&v=v1562567553145&size=invisible&cb=4s2te38oygvz'


reGex = re.compile(r'<input (.*?)>')

s = requests.Session()

r = s.get(URL) 
r2 = s.get(URL2)

#i don't sharit' python, ne beite
token = re.findall(reGex,r.text)[0].split()[2][7:-1]
token2 = re.findall(reGex,r2.text)[0].split()[2][7:-1]


headers = {
	"User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0", 
	'Content-Type': 'application/x-www-form-urlencoded'
	}

data = {'token':str(token2)
,'action':'get_balance',
'_token':str(token),'cardNumber': "YOUR_CARD_NUMBER"}



r3 = s.post(url=URL, data= data, headers=headers, cookies = r.cookies)

print(r3.text)