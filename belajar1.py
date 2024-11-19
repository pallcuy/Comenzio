durian = 30000

jumlah = int(input("jumlah durian yang di beli : "))

harga = durian * jumlah

harga_awal = harga

if harga >= 100000:
        harga -= harga * 0.1
elif harga < 100000:
        harga -= harga * 0.05

harga_total = harga

if harga_awal == harga:
    print("Tidak ada diskon yang diterapkan.")
else:
    print("Harga sebelum diskon: ", harga_awal)
    print("Harga total setelah diskon: ", int(harga_total))
