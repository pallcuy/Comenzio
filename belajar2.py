a = 60000

jumlah = int(input("masukkan jumlah belanjaan : "))

harga = a * jumlah
harga_awal = harga

if harga < 500000:
        harga -= harga * 0.5
elif harga >= 500000:
        harga -= harga * 0.10
elif harga <= 1000000:
        harga -= harga * 0.10
elif harga > 1000000:
        harga -= harga * 0.15

harga_total = harga

if harga_awal == harga:
    print("Tidak ada diskon yang diterapkan.")
else:
    print("Harga sebelum diskon: ", harga_awal)
    print("Harga total setelah diskon: ", int(harga_total))
