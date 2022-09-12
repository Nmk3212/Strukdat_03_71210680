#Inputan
input_kalimat = input("Masukkan input berupa kalimat teks: ")
input_kata = input("Masukkan input berupa satu buah kata: ")

#Lower dan Split
input_kalimat = input_kalimat.lower().split()
input_kata = input_kata.lower()

#Perulangan untuk menemukan jumlah kata yang berhasil ditemukan
index = 0
for i in input_kalimat:
    if i == input_kata:
        index += 1
        
#Output
print(index)