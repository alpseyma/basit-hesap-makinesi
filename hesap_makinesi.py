def hesap_makinesi():
    print("Hesap Makinesine Hoş Geldiniz!")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    while True:
        islem = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/3/4) veya çıkmak için 'q' tuşuna basın: ")
        
        if islem == 'q':
            print("Hesap makinesi kapatılıyor...")
            break

        if islem not in ['1', '2', '3', '4']:
            print("Geçersiz seçim! Lütfen 1, 2, 3, 4 veya 'q' tuşlayın.")
            continue
        
        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        if islem == '1':
            sonuc = sayi1 + sayi2
            print(f"Toplam: {sayi1} + {sayi2} = {sonuc}")
        
        elif islem == '2':
            sonuc = sayi1 - sayi2
            print(f"Fark: {sayi1} - {sayi2} = {sonuc}")
        
        elif islem == '3':
            sonuc = sayi1 * sayi2
            print(f"Çarpım: {sayi1} * {sayi2} = {sonuc}")
        
        elif islem == '4':
            if sayi2 == 0:
                print("Hata: Sıfıra bölme tanımsızdır.")
            else:
                sonuc = sayi1 / sayi2
                print(f"Bölüm: {sayi1} / {sayi2} = {sonuc}")

if __name__ == "__main__":
    hesap_makinesi()
