# Membuat fungsi penjumlahan
def tambah(x, y):
   return x + y

# Membuat fungsi pengurangan
def kurang(x, y):
   return x - y

# Membuat fungsi perkalian
def kali(x, y):
   return x * y

# Membuat fungsi pembagian
def bagi(x, y):
   return x / y

print("Pilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Mengambil input dari user
pilihan = input("Masukkan pilihan (1/2/3/4):")

# Input bilangan
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))

if pilihan == '1':
   print(num1,"+",num2,"=", tambah(num1,num2))

elif pilihan == '2':
   print(num1,"-",num2,"=", kurang(num1,num2))

elif pilihan == '3':
   print(num1,"*",num2,"=", kali(num1,num2))

elif pilihan == '4':
   print(num1,"/",num2,"=", bagi(num1,num2))
else:
   print("Input tidak valid")