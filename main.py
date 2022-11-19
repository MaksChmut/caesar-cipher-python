
lang_ol ='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ0123456789'
value = 1
message = input('Повідомлення для шифровки: ').upper()
result = ''
lang = input('для шифрації натисніть A: ')

if lang == 'A':
 for i in message:
  place = lang_ol.find(i)
  new_place = place + value
  if i in lang_ol:
   result += lang_ol[new_place]
  else:
   result += i

print(result)

#