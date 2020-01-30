a = int(input("a: ")) #Perintah untuk memasukan Angka a
b = int(input("b: ")) #Perintah untuk memasukan Angka b

from ARITMATIKA.aritmatika import tambah, bagi, kurang, kali
print("Penjumlahan")
print(int(tambah(a, b)))
print("Pembagian")
print(int(bagi(a, b)))
print("Pengurangan")
print(int(kurang(a, b)))
print("Perkalian")
print(int(kali(a, b)))