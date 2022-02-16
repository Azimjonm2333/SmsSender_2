import sys

import webbrowser as wb

print("СКРИПТ КАНАЛА: @b1n_bash")
print("Версия: 0.2")
print("Сделана: @Azimjonm2333")

wb.open("https://t.me/b1n_bash")

import requests
phone = input('Введите номер телефона: ')
message = input ('Введите сообщение c (+): ')
resp = requests.post('https://textbelt.com/text', {
  'phone': phone,
  'message': message,
  'key': 'textbelt',
})
print(resp.json())
