#!C:\Users\admin\AppData\Local\Programs\Python\Python313\python.exe
import json


satellites = [
    {'{#NAME}': 'nginx-443', '{#PORT}': 443},
    {'{#NAME}': 'nginx-23231', '{#PORT}': 23231},
    {'{#NAME}': 'postgres-5432', '{#PORT}': 5432},
    {'{#NAME}': 'redis-6379', '{#PORT}': 6379},
    {'{#NAME}': 'rabitmq-5672', '{#PORT}': 5672},
]

tmp = {
    'data': satellites
}

json_data = json.dumps(tmp)
print(json_data)