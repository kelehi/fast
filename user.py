import requests
import json

with open('master.json', 'r') as f:
    a = json.load(f)

params = {'item': 6}
# p = requests.get('http://127.0.0.1:8000/admin_login/login_admin&password_admin').json()
params1 = {
  "title": "123",
  "age": 19,
  "write": "456",
  "duration": "789",
  "date": "2024-09-09",
  "genres": [
    {
      "name": "123"
    }
  ]
}
p1 = requests.post('http://127.0.0.1:8000/user/', json=params1).json()
n = requests.get("http://127.0.0.1:8000").json()
print(n)