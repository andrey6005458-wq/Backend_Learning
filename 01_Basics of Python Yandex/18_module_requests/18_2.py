from requests import get

adress = 'http://' + input()
sum = 0
while data := int(get(adress).text):
    sum += data
print(sum)