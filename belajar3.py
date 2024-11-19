# Tugas kamu adalah membuat sebuah program yang dapat menghitung total biaya pembelian berdasarkan daftar buku yang dibeli oleh pelanggan. Setiap buku memiliki nama, harga, dan jumlah yang dibeli.
# Jika total harga buku melebihi Rp 500.000, maka pelanggan mendapatkan diskon 10%
# Input:
# Nama buku, harga buku, dan jumlah buku yang dibeli (bisa lebih dari satu buku).
# Output:
# Tampilkan daftar buku yang dibeli beserta total harga sebelum dan sesudah diskon (jika ada).

buku_a = 90000
buku_b = 120000
buku_c = 160000

buku = input("masukkan nama buku (buku_a), (buku_b), (buku_c) : ")
jumlah = int(input("masukkan jumlah yang dibeli : "))

harga = buku * jumlah
harga_awal = harga

if buku == "buku_a":
        harga = buku_a * jumlah
        print ("Harga sebelum diskon : ", harga)
elif buku == "buku_b":
        harga = buku_b * jumlah
        print ("Harga sebelum diskon : ", harga)
elif buku == "buku_c":
        harga = buku_c * jumlah
        print ("Harga sebelum diskon : ", harga)

if harga > 500000:
        harga -= harga * 0.10

harga_total = harga

if harga_awal == harga:
        print ("Tidak ada diskon yang anda dapatkan")
else:
        print ("Nama buku : ", buku, "Harga Total :", int(harga_total))
