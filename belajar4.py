# setiap siswa harus mendapatkan nilai minimal 60 agar lulus.
# buatlah program yang meminta pengguna untuk memasukan jumlah siswa di kelas.
# meminta pengguna untuk memasukkan nilai setiap siswa.
# jika nilai siswa dibawah 60, tampilkan pesan "lulus".
# setelah semua nilai dimasukkan, tampilkan jumlah siswa yang lulus dan jumlah siswa yang tidak lulus.

jumlah_siswa = int(input("Masukkan jumlah siswa : "))

lulus = 0
tidak_lulus = 0

for i in range(jumlah_siswa):
        nilai_siswa = int(input(f"Masukkan nilai siswa ke-{i+1} : "))
        if nilai_siswa >= 60:
                print ("Lulus")
                lulus += 1
        else:
                print ("Tidak Lulus")
                tidak_lulus += 1

print(f"\nJumlah siswa yang lulus : {lulus}")
print(f"Jumlah siswa yang tidak lulus : {tidak_lulus}")
