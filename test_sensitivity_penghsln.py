from fuzzy_logic import hitung_beasiswa

print("=" * 70)
print("SENSITIVITY TEST - PERUBAHAN PENGHASILAN")
print("=" * 70)

ipk = 3.20
prestasi = 70

for penghasilan in [
    1.0, 1.5, 2.0, 2.5, 3.0,
    3.5, 4.0, 4.5, 5.0, 5.5,
    6.0, 6.5, 7.0, 7.5, 8.0,
    8.5, 9.0, 9.5, 10.0
]:

    skor, kategori = hitung_beasiswa(
        ipk,
        penghasilan,
        prestasi
    )

    print(
        f"Penghasilan: {penghasilan:4.1f} jt | "
        f"Skor: {skor:6.2f} | "
        f"{kategori}"
    )

print("=" * 70)
