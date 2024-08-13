# Toplama fonksiyonu
def toplama(x, y):
    return x + y

# Çıkarma fonksiyonu
def cikarma(x, y):
    return x - y

# Çarpma fonksiyonu
def carpma(x, y):
    return x * y

# Bölme fonksiyonu
def bolme(x, y):
    if y == 0:
        return "Hata! Sıfıra bölme tanımsızdır."
    else:
        return x / y

def hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    secim = input("Seçiminiz (1/2/3/4): ")

    if secim in ['1', '2', '3', '4']:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print(f"{sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")

        elif secim == '2':
            print(f"{sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")

        elif secim == '3':
            print(f"{sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")

        elif secim == '4':
            print(f"{sayi1} / {sayi2} = {bolme(sayi1, sayi2)}")

    else:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    hesap_makinesi()
