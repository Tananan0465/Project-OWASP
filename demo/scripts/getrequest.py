import requests
r =requests.get('http://altoro.testfire.net/login.jsp')
f = open("req.txt","w")
f.write(r.text)
f.close