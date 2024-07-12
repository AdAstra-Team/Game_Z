import requests
import json

# URL для запроса
url = 'https://example.com/api/endpoint'

# Заголовки
headers = {
    'X-Auth-Token': '668eaa760f55f668eaa760f563',
    'Content-Type': 'application/json'
}

# Тело запроса в формате JSON
data = {
    'key1': 'value1',
    'key2': 'value2'
}

# Преобразуем тело запроса в формат JSON
json_data = json.dumps(data)

# Выполняем POST запрос
response = requests.post(url, headers=headers, data=json_data)

# Проверяем статус-код ответа
if response.status_code == 200:
    print('Success:', response.json())
else:
    print('Failed:', response.status_code, response.text)
