from fuzzy_logic import hitung_beasiswa

print("=" * 70)
print("SENSITIVITY TEST - PERUBAHAN PRESTASI")
print("=" * 70)

ipk = 3.20
penghasilan = 3.0

for prestasi in [
    0, 10, 20, 30, 35,
    40, 45, 50, 55, 60,
    65, 70, 75, 80, 85,
    90, 95, 100
]:

    skor, kategori = hitung_beasiswa(
        ipk,
        penghasilan,
        prestasi
    )

    print(
        f"Prestasi: {prestasi:3} | "
        f"Skor: {skor:6.2f} | "
        f"{kategori}"
    )

print("=" * 70)