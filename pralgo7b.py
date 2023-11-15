# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:48:14 2023

@author: Gwen
"""
def buatkeluaran(inputan):
    if inputan == 0:
        return "selesai."

    ordinalnya = "th"
    if inputan == 1:
        ordinalnya ="st"
    elif inputan == 2:
        ordinalnya ="nd"
    elif inputan == 3:
        ordinalnya ="rd"
    elif inputan == 0:
        ordinalnya ="th"
        
    result = f"({inputan},'{ordinalnya}')"
    return result

print ("Ordinal Number\nketik 0 untuk menghentikan program")
masukkan= int(input("masukkan angka = "))

while masukkan != 0:
    output = buatkeluaran(masukkan)
    print(output)
    masukkan = int(input("Masukkan angka : "))
    
print ("terima kasih telah menggunakan program saya")
