from fuzzy_logic import hitung_beasiswa

data_mahasiswa = [
    ("Budi", 3.65, 2.5, 80),
    ("Siti", 2.80, 5.0, 40),
    ("Andi", 3.20, 1.5, 60),
    ("Dewi", 3.90, 8.0, 95),
    ("Eko", 2.10, 3.0, 20),
    ("Fajar", 3.50, 2.0, 75),
    ("Gita", 2.50, 6.0, 45),
    ("Hendra", 3.80, 1.0, 90),
    ("Indah", 2.30, 7.0, 30),
    ("Joko", 3.00, 4.0, 50),
]

print("=" * 75)
print("PENGUJIAN 10 SKENARIO SIBEA")
print("=" * 75)

for nama, ipk, penghasilan, prestasi in data_mahasiswa:
    skor, kategori = hitung_beasiswa(
        ipk,
        penghasilan,
        prestasi
    )

    print(
        f"{nama:<10} | "
        f"IPK: {ipk:.2f} | "
        f"Penghasilan: {penghasilan:.1f} jt | "
        f"Prestasi: {prestasi:>3} | "
        f"Skor: {skor:>6.2f} | "
        f"{kategori}"
    )