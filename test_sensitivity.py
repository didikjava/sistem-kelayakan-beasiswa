from fuzzy_logic import hitung_beasiswa

print("=" * 70)
print("SENSITIVITY TEST - PERUBAHAN IPK")
print("=" * 70)

penghasilan = 3.0
prestasi = 70

for ipk in [2.00, 2.10, 2.20, 2.30, 2.40,
            2.50, 2.60, 2.70, 2.80, 2.90,
            3.00, 3.10, 3.20, 3.30, 3.40,
            3.50, 3.60, 3.70, 3.80, 3.90, 4.00]:

    skor, kategori = hitung_beasiswa(
        ipk,
        penghasilan,
        prestasi
    )

    print(
        f"IPK: {ipk:.2f} | "
        f"Skor: {skor:6.2f} | "
        f"{kategori}"
    )

print("=" * 70)