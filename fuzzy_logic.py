import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# ============================================================
# 1. VARIABEL INPUT DAN OUTPUT
# ============================================================

# IPK
ipk = ctrl.Antecedent(np.arange(0, 4.01, 0.01), "ipk")

# Penghasilan orang tua dalam satuan juta rupiah
penghasilan = ctrl.Antecedent(
    np.arange(0, 10.01, 0.01),
    "penghasilan"
)

# Prestasi mahasiswa
prestasi = ctrl.Antecedent(
    np.arange(0, 100.1, 0.1),
    "prestasi"
)

# Output kelayakan
kelayakan = ctrl.Consequent(
    np.arange(0, 100.1, 0.1),
    "kelayakan"
)


# ============================================================
# 2. MEMBERSHIP FUNCTION
# ============================================================

# ---------- IPK ----------
ipk["rendah"] = fuzz.trapmf(
    ipk.universe,
    [0, 0, 2.0, 2.5]
)

ipk["sedang"] = fuzz.trimf(
    ipk.universe,
    [2.0, 2.75, 3.5]
)

ipk["tinggi"] = fuzz.trapmf(
    ipk.universe,
    [3.0, 3.5, 4.0, 4.0]
)


# ---------- Penghasilan ----------
penghasilan["rendah"] = fuzz.trapmf(
    penghasilan.universe,
    [0, 0, 2, 3]
)

penghasilan["sedang"] = fuzz.trimf(
    penghasilan.universe,
    [2, 4, 6]
)

penghasilan["tinggi"] = fuzz.trapmf(
    penghasilan.universe,
    [5, 6, 10, 10]
)


# ---------- Prestasi ----------
prestasi["rendah"] = fuzz.trapmf(
    prestasi.universe,
    [0, 0, 30, 40]
)

prestasi["sedang"] = fuzz.trimf(
    prestasi.universe,
    [30, 50, 70]
)

prestasi["tinggi"] = fuzz.trapmf(
    prestasi.universe,
    [60, 70, 100, 100]
)


# ---------- Kelayakan ----------
kelayakan["tidak_layak"] = fuzz.trapmf(
    kelayakan.universe,
    [0, 0, 30, 40]
)

kelayakan["dipertimbangkan"] = fuzz.trimf(
    kelayakan.universe,
    [30, 50, 70]
)

kelayakan["layak"] = fuzz.trapmf(
    kelayakan.universe,
    [60, 70, 100, 100]
)


# ============================================================
# 3. RULE FUZZY
# ============================================================

rules = [

    # IPK RENDAH
    ctrl.Rule(
        ipk["rendah"] & penghasilan["rendah"] & prestasi["rendah"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["rendah"] & penghasilan["rendah"] & prestasi["sedang"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["rendah"] & penghasilan["rendah"] & prestasi["tinggi"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["rendah"] & penghasilan["sedang"] & prestasi["rendah"],
        kelayakan["tidak_layak"]
    ),

    ctrl.Rule(
        ipk["rendah"] & penghasilan["sedang"] & prestasi["sedang"],
        kelayakan["tidak_layak"]
    ),

    ctrl.Rule(
        ipk["rendah"] & penghasilan["sedang"] & prestasi["tinggi"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["rendah"] & penghasilan["tinggi"] & prestasi["rendah"],
        kelayakan["tidak_layak"]
    ),

    ctrl.Rule(
        ipk["rendah"] & penghasilan["tinggi"] & prestasi["sedang"],
        kelayakan["tidak_layak"]
    ),

    ctrl.Rule(
        ipk["rendah"] & penghasilan["tinggi"] & prestasi["tinggi"],
        kelayakan["dipertimbangkan"]
    ),


    # IPK SEDANG
    ctrl.Rule(
        ipk["sedang"] & penghasilan["rendah"] & prestasi["rendah"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["sedang"] & penghasilan["rendah"] & prestasi["sedang"],
        kelayakan["layak"]
    ),

    ctrl.Rule(
        ipk["sedang"] & penghasilan["rendah"] & prestasi["tinggi"],
        kelayakan["layak"]
    ),

    ctrl.Rule(
        ipk["sedang"] & penghasilan["sedang"] & prestasi["rendah"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["sedang"] & penghasilan["sedang"] & prestasi["sedang"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["sedang"] & penghasilan["sedang"] & prestasi["tinggi"],
        kelayakan["layak"]
    ),

    ctrl.Rule(
        ipk["sedang"] & penghasilan["tinggi"] & prestasi["rendah"],
        kelayakan["tidak_layak"]
    ),

    ctrl.Rule(
        ipk["sedang"] & penghasilan["tinggi"] & prestasi["sedang"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["sedang"] & penghasilan["tinggi"] & prestasi["tinggi"],
        kelayakan["dipertimbangkan"]
    ),


    # IPK TINGGI
    ctrl.Rule(
        ipk["tinggi"] & penghasilan["rendah"] & prestasi["rendah"],
        kelayakan["layak"]
    ),

    ctrl.Rule(
        ipk["tinggi"] & penghasilan["rendah"] & prestasi["sedang"],
        kelayakan["layak"]
    ),

    ctrl.Rule(
        ipk["tinggi"] & penghasilan["rendah"] & prestasi["tinggi"],
        kelayakan["layak"]
    ),

    ctrl.Rule(
        ipk["tinggi"] & penghasilan["sedang"] & prestasi["rendah"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["tinggi"] & penghasilan["sedang"] & prestasi["sedang"],
        kelayakan["layak"]
    ),

    ctrl.Rule(
        ipk["tinggi"] & penghasilan["sedang"] & prestasi["tinggi"],
        kelayakan["layak"]
    ),

    ctrl.Rule(
        ipk["tinggi"] & penghasilan["tinggi"] & prestasi["rendah"],
        kelayakan["tidak_layak"]
    ),

    ctrl.Rule(
        ipk["tinggi"] & penghasilan["tinggi"] & prestasi["sedang"],
        kelayakan["dipertimbangkan"]
    ),

    ctrl.Rule(
        ipk["tinggi"] & penghasilan["tinggi"] & prestasi["tinggi"],
        kelayakan["dipertimbangkan"]
    ),
]


# ============================================================
# 4. CONTROL SYSTEM
# ============================================================

sistem_fuzzy = ctrl.ControlSystem(rules)


# ============================================================
# 5. FUNGSI PERHITUNGAN
# ============================================================

def hitung_beasiswa(nilai_ipk, nilai_penghasilan, nilai_prestasi):
    """
    Menghitung kelayakan beasiswa berdasarkan:
    - IPK
    - Penghasilan orang tua
    - Prestasi

    nilai_penghasilan menggunakan satuan juta rupiah.
    """

    simulasi = ctrl.ControlSystemSimulation(sistem_fuzzy)

    simulasi.input["ipk"] = nilai_ipk
    simulasi.input["penghasilan"] = nilai_penghasilan
    simulasi.input["prestasi"] = nilai_prestasi

    simulasi.compute()

    nilai_kelayakan = simulasi.output["kelayakan"]

    # Menentukan kategori
    if nilai_kelayakan < 40:
        kategori = "Tidak Layak"
    elif nilai_kelayakan < 70:
        kategori = "Dipertimbangkan"
    else:
        kategori = "Layak"

    return nilai_kelayakan, kategori


# ============================================================
# 6. FUNGSI DERAJAT KEANGGOTAAN
# ============================================================

def hitung_membership(
    nilai_ipk,
    nilai_penghasilan,
    nilai_prestasi
):

    membership = {

        "ipk": {
            "rendah": fuzz.interp_membership(
                ipk.universe,
                ipk["rendah"].mf,
                nilai_ipk
            ),
            "sedang": fuzz.interp_membership(
                ipk.universe,
                ipk["sedang"].mf,
                nilai_ipk
            ),
            "tinggi": fuzz.interp_membership(
                ipk.universe,
                ipk["tinggi"].mf,
                nilai_ipk
            ),
        },

        "penghasilan": {
            "rendah": fuzz.interp_membership(
                penghasilan.universe,
                penghasilan["rendah"].mf,
                nilai_penghasilan
            ),
            "sedang": fuzz.interp_membership(
                penghasilan.universe,
                penghasilan["sedang"].mf,
                nilai_penghasilan
            ),
            "tinggi": fuzz.interp_membership(
                penghasilan.universe,
                penghasilan["tinggi"].mf,
                nilai_penghasilan
            ),
        },

        "prestasi": {
            "rendah": fuzz.interp_membership(
                prestasi.universe,
                prestasi["rendah"].mf,
                nilai_prestasi
            ),
            "sedang": fuzz.interp_membership(
                prestasi.universe,
                prestasi["sedang"].mf,
                nilai_prestasi
            ),
            "tinggi": fuzz.interp_membership(
                prestasi.universe,
                prestasi["tinggi"].mf,
                nilai_prestasi
            ),
        }
    }

    return membership


# ============================================================
# 7. DATA 27 RULE
# ============================================================

rule_data = [

    ("R1", "Rendah", "Rendah", "Rendah", "Dipertimbangkan"),
    ("R2", "Rendah", "Rendah", "Sedang", "Dipertimbangkan"),
    ("R3", "Rendah", "Rendah", "Tinggi", "Dipertimbangkan"),

    ("R4", "Rendah", "Sedang", "Rendah", "Tidak Layak"),
    ("R5", "Rendah", "Sedang", "Sedang", "Tidak Layak"),
    ("R6", "Rendah", "Sedang", "Tinggi", "Dipertimbangkan"),

    ("R7", "Rendah", "Tinggi", "Rendah", "Tidak Layak"),
    ("R8", "Rendah", "Tinggi", "Sedang", "Tidak Layak"),
    ("R9", "Rendah", "Tinggi", "Tinggi", "Dipertimbangkan"),

    ("R10", "Sedang", "Rendah", "Rendah", "Dipertimbangkan"),
    ("R11", "Sedang", "Rendah", "Sedang", "Layak"),
    ("R12", "Sedang", "Rendah", "Tinggi", "Layak"),

    ("R13", "Sedang", "Sedang", "Rendah", "Dipertimbangkan"),
    ("R14", "Sedang", "Sedang", "Sedang", "Dipertimbangkan"),
    ("R15", "Sedang", "Sedang", "Tinggi", "Layak"),

    ("R16", "Sedang", "Tinggi", "Rendah", "Tidak Layak"),
    ("R17", "Sedang", "Tinggi", "Sedang", "Dipertimbangkan"),
    ("R18", "Sedang", "Tinggi", "Tinggi", "Dipertimbangkan"),

    ("R19", "Tinggi", "Rendah", "Rendah", "Layak"),
    ("R20", "Tinggi", "Rendah", "Sedang", "Layak"),
    ("R21", "Tinggi", "Rendah", "Tinggi", "Layak"),

    ("R22", "Tinggi", "Sedang", "Rendah", "Dipertimbangkan"),
    ("R23", "Tinggi", "Sedang", "Sedang", "Layak"),
    ("R24", "Tinggi", "Sedang", "Tinggi", "Layak"),

    ("R25", "Tinggi", "Tinggi", "Rendah", "Tidak Layak"),
    ("R26", "Tinggi", "Tinggi", "Sedang", "Dipertimbangkan"),
    ("R27", "Tinggi", "Tinggi", "Tinggi", "Dipertimbangkan"),
]


# ============================================================
# 8. HITUNG FIRING STRENGTH
# ============================================================

def hitung_firing_strength(membership):

    hasil = []

    for nomor, ipk_kat, penghasilan_kat, prestasi_kat, output in rule_data:

        nilai_ipk = membership["ipk"][ipk_kat.lower()]
        nilai_penghasilan = membership["penghasilan"][
            penghasilan_kat.lower()
        ]
        nilai_prestasi = membership["prestasi"][
            prestasi_kat.lower()
        ]

        # Operator AND menggunakan MIN
        firing_strength = min(
            nilai_ipk,
            nilai_penghasilan,
            nilai_prestasi
        )

        kondisi = (
            f"IPK {ipk_kat} AND "
            f"Penghasilan {penghasilan_kat} AND "
            f"Prestasi {prestasi_kat}"
        )

        hasil.append({
            "rule": nomor,
            "kondisi": kondisi,
            "output": output,
            "firing_strength": firing_strength
        })

    return hasil