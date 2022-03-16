import sys

import webbrowser as wb

print("СКРИПТ КАНАЛА: @CAVIsoft")
print("Сделана: @Azimjonm2333")

wb.open("https://t.me/CAVIsoft")

import requests
phone = input('Введите номер телефона c (+): ')
message = input ('Введите сообщение: ')
resp = requests.post('https://textbelt.com/text', {
  'phone': phone,
  'message': message,
  'key': 'textbelt',
})
print(resp.json())
