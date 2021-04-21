girdi = ("girilen sayi")
dizi =[]

for i in girdi:
    if not (i in dizi) and i != " ":
        dizi.append(i)
print(dizi)

dizi2 = []
for i in dizi:
    sayac = 0
    for j in girdi:
        if i ==j:
            sayac += 1
    dizi2.append(sayac)

for i in range(0, len(dizi)):
    print("{}'den {} tane var".format(dizi[i], dizi2[i]))
