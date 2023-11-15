def buatprima(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

def masukan():
    nomor = int(input("angka = "))
    
    if buatprima(nomor):
        print(f"{nomor} adalah bilangan PRIMA")
    else:
        print(f"{nomor} bukanlah bilangan PRIMA")
        
masukan()