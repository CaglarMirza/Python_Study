def asal(sayi):
    sayac = 2
    while sayac <sayi //2 +1:
        if sayi % sayac == 0:
            return False
        sayac += 1
    return True


def ucuz_sayi(sayi):
    if asal(sayi):
        if (asal(sayi) and asal(sayi+2) and asal(sayi+6)) or (asal(sayi) and asal(sayi+4) and asal(sayi+6)):
            print("sayi ucuz asal sayidir.")
        else:
            print("sayi ucuz asal sayi degildir.")
    else:
        print("gonderilen sayi asal sayi degildir")

if __name__ == "__main__":
    ucuz_sayi(45)