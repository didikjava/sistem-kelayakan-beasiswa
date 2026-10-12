from fuzzy_logic import hitung_beasiswa

print("=" * 80)
print("PENGUJIAN BOUNDARY SIBEA")
print("=" * 80)

# Pengujian batas IPK
data_ipk = [
    ("IPK 2.00", 2.00, 3.0, 70),
    ("IPK 2.50", 2.50, 3.0, 70),
    ("IPK 2.75", 2.75, 3.0, 70),
    ("IPK 3.00", 3.00, 3.0, 70),
    ("IPK 3.50", 3.50, 3.0, 70),
    ("IPK 4.00", 4.00, 3.0, 70),
]

print("\n--- Batas IPK ---")

for nama, ipk, penghasilan, prestasi in data_ipk:
    skor, kategori = hitung_beasiswa(
        ipk,
        penghasilan,
        prestasi
    )

    print(
        f"{nama:<12} | "
        f"Skor: {skor:>6.2f} | "
        f"{kategori}"
    )


# Pengujian batas Penghasilan
data_penghasilan = [
    ("Income 2 jt", 3.2, 2.0, 70),
    ("Income 3 jt", 3.2, 3.0, 70),
    ("Income 4 jt", 3.2, 4.0, 70),
    ("Income 5 jt", 3.2, 5.0, 70),
    ("Income 6 jt", 3.2, 6.0, 70),
    ("Income 10 jt", 3.2, 10.0, 70),
]

print("\n--- Batas Penghasilan ---")

for nama, ipk, penghasilan, prestasi in data_penghasilan:
    skor, kategori = hitung_beasiswa(
        ipk,
        penghasilan,
        prestasi
    )

    print(
        f"{nama:<15} | "
        f"Skor: {skor:>6.2f} | "
        f"{kategori}"
    )


# Pengujian batas Prestasi
data_prestasi = [
    ("Prestasi 30", 3.2, 3.0, 30),
    ("Prestasi 40", 3.2, 3.0, 40),
    ("Prestasi 50", 3.2, 3.0, 50),
    ("Prestasi 60", 3.2, 3.0, 60),
    ("Prestasi 70", 3.2, 3.0, 70),
    ("Prestasi 100", 3.2, 3.0, 100),
]

print("\n--- Batas Prestasi ---")

for nama, ipk, penghasilan, prestasi in data_prestasi:
    skor, kategori = hitung_beasiswa(
        ipk,
        penghasilan,
        prestasi
    )

    print(
        f"{nama:<15} | "
        f"Skor: {skor:>6.2f} | "
        f"{kategori}"
    )

print("\n" + "=" * 80)
print("PENGUJIAN SELESAI")
print("=" * 80)