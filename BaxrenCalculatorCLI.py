import math

def hesap_islemleri(işlem):
    if '+' in işlem:
        sayılar = işlem.split('+')
        return float(sayılar[0]) + float(sayılar[1])
    elif '-' in işlem:
        sayılar = işlem.split('-')
        return float(sayılar[0]) - float(sayılar[1])
    elif 'x' in işlem:
        sayılar = işlem.split('x')
        return float(sayılar[0]) * float(sayılar[1])
    elif '/' in işlem:
        sayılar = işlem.split('/')
        if float(sayılar[1]) != 0:
            return float(sayılar[0]) / float(sayılar[1])
        else:
            raise ZeroDivisionError("Sıfıra bölme hatası!")
    elif '%' in işlem:
        sayılar = işlem.split('%')
        return (float(sayılar[0]) / 100) * float(sayılar[1])
    elif 'sin' in işlem:
        sayı = float(işlem.replace('sin', ''))
        return math.sin(math.radians(sayı))
    elif 'cos' in işlem:
        sayı = float(işlem.replace('cos', ''))
        return math.cos(math.radians(sayı))
    elif 'tan' in işlem:
        sayı = float(işlem.replace('tan', ''))
        return math.tan(math.radians(sayı))
    elif 'sqrt' in işlem:
        sayı = float(işlem.replace('sqrt', ''))
        return math.sqrt(sayı)
    elif 'log' in işlem:
        sayı = float(işlem.replace('log', ''))
        return math.log(sayı)
    elif 'exp' in işlem:
        sayı = float(işlem.replace('exp', ''))
        return math.exp(sayı)
    elif 'perm' in işlem:
        sayılar = işlem.split('perm')
        n = int(sayılar[0])
        r = int(sayılar[1])
        return math.factorial(n) / math.factorial(n-r)
    elif 'comb' in işlem:
        sayılar = işlem.split('comb')
        n = int(sayılar[0])
        r = int(sayılar[1])
        return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
    elif 'mod' in işlem:
        sayılar = işlem.split('mod')
        return int(sayılar[0]) % int(sayılar[1])
    elif 'fact' in işlem:
        sayı = int(işlem.replace('fact', ''))
        return math.factorial(sayı)
    else:
        raise ValueError("Geçersiz işlem!")

def hesap_makinesi():
    print("BaxrenCalculator'a hoş geldiniz")
    print("Yapılabilir işlemler: Toplama: 2+2, Çıkarma: 5-3, Çarpma: 4x5, Bölme: 10/2, Yüzde: 20%25, Sinüs: sin(30), Cosinüs: cos(30), Tanjant: tan(30), Karekök: sqrt(4), Logaritma: log(10), Üstel: exp(2), Permütasyon: 5perm3, Kombinasyon: 5comb3, Modül: 10mod3, Faktöriyel: 5fact. Çıkmak için 'q', verileri sıfırlamak için 'c' yazabilirsiniz.")

    while True:
        işlem = input("İşlemi giriniz: ")

        if işlem.lower() == 'q':
            print("Çıkış yapılıyor...")
            break
        elif işlem.lower() == 'c':
            print("Veriler sıfırlandı.")
            continue

        try:
            sonuç = hesap_islemleri(işlem)
            print(f"{işlem} = {sonuç}")
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    hesap_makinesi()
