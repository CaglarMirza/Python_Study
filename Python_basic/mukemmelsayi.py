def muk_sayi(sayi):
    toplam = 0 
    sayac = 1
    while (sayac < sayi / 2 + 1):
        if sayi % sayac == 0:
            toplam += sayac
        sayac += 1
    if sayi == toplam:
        return True
    else:
        return False

if __name__ == "__main__":
    for i in range(2, 1000):
        if muk_sayi(i):
            print(i, "sayisi mukemmel sayidir.")