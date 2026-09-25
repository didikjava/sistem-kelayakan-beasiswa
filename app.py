import textwrap

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from fuzzy_logic import (
    hitung_beasiswa,
    hitung_membership,
    hitung_firing_strength,
    ipk,
    penghasilan,
    prestasi,
    kelayakan,
    rule_data,
)


# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="SIBEA | Sistem Penilaian Beasiswa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# HELPER HTML
# ============================================================

def render_html(content):
    st.html(textwrap.dedent(content).strip())


# ============================================================
# CSS
# ============================================================

render_html(
    """
    <style>

    /* ========================================================
       GLOBAL
    ======================================================== */

    .stApp {
        background: #f6f8fc;
    }

    .main .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* ========================================================
       SIDEBAR
    ======================================================== */

    [data-testid="stSidebar"] {
        background: #081b33;
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.2rem;
    }

    [data-testid="stSidebar"] * {
        color: #ffffff;
    }

    .sidebar-brand {
        padding: 12px 12px 25px 12px;
    }

    .sidebar-logo {
        width: 58px;
        height: 58px;
        background: #ffffff;
        border-radius: 16px;

        display: flex;
        align-items: center;
        justify-content: center;

        font-size: 29px;

        margin-bottom: 14px;

        box-shadow:
            0 8px 20px rgba(0,0,0,0.15);
    }

    .sidebar-title {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
        color: #ffffff !important;
    }

    .sidebar-subtitle {
        font-size: 12px;
        line-height: 1.6;
        color: #aebed2 !important;
        margin-top: 3px;
    }

    .sidebar-section {
        margin-top: 20px;
        margin-bottom: 8px;

        font-size: 11px;
        font-weight: 800;
        letter-spacing: 1.8px;

        color: #7f9ab5 !important;
    }

    .sidebar-footer {
        margin-top: 35px;
        padding: 15px;

        border-radius: 14px;

        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.07);

        font-size: 11px;
        color: #9fb2c7 !important;
        text-align: center;
        line-height: 1.6;
    }


    /* ========================================================
       RADIO SIDEBAR
    ======================================================== */

    [data-testid="stSidebar"] div[role="radiogroup"] {
        gap: 5px;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label {
        border-radius: 10px;
        padding: 8px 10px;
        transition: 0.2s;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: rgba(255,255,255,0.07);
    }


    /* ========================================================
       PAGE HEADER
    ======================================================== */

    .page-kicker {
        display: inline-block;

        padding: 7px 13px;

        border-radius: 30px;

        background: #eaf0f8;
        color: #18385f !important;

        font-size: 11px;
        font-weight: 800;

        letter-spacing: 1.5px;

        margin-bottom: 12px;
    }

    .page-title {
        font-size: 35px;
        font-weight: 850;

        color: #0b2845 !important;

        margin-bottom: 5px;
        letter-spacing: -0.8px;
    }

    .page-description {
        color: #687b8e !important;

        font-size: 14px;

        line-height: 1.7;

        margin-bottom: 25px;
    }


    /* ========================================================
       HERO
    ======================================================== */

    .hero-card {
        position: relative;

        background:
            linear-gradient(
                135deg,
                #082b4d 0%,
                #103f68 65%,
                #194d78 100%
            );

        border-radius: 26px;

        padding: 38px;

        margin: 10px 0 25px 0;

        overflow: hidden;

        box-shadow:
            0 18px 45px rgba(8,43,77,0.18);
    }

    .hero-card:after {
        content: "";

        position: absolute;

        width: 300px;
        height: 300px;

        right: -120px;
        top: -140px;

        border-radius: 50%;

        background:
            rgba(255,255,255,0.06);
    }

    .hero-label {
        position: relative;
        z-index: 2;

        font-size: 11px;

        color: #a9c6de !important;

        font-weight: 800;

        letter-spacing: 2px;

        margin-bottom: 12px;
    }

    .hero-title {
        position: relative;
        z-index: 2;

        font-size: 31px;

        font-weight: 850;

        color: #ffffff !important;

        margin-bottom: 12px;
    }

    .hero-text {
        position: relative;
        z-index: 2;

        max-width: 850px;

        font-size: 14px;

        line-height: 1.8;

        color: #d6e5f1 !important;
    }


    /* ========================================================
       INFO CARD
    ======================================================== */

    .info-card {
        background: #ffffff;

        border: 1px solid #e6edf4;

        border-radius: 20px;

        padding: 24px;

        min-height: 155px;

        box-shadow:
            0 8px 25px rgba(20,50,80,0.05);
    }

    .info-icon {
        font-size: 25px;
        margin-bottom: 12px;
    }

    .info-label {
        font-size: 10px;

        letter-spacing: 1.5px;

        font-weight: 800;

        color: #8494a5 !important;

        margin-bottom: 7px;
    }

    .info-value {
        font-size: 21px;

        font-weight: 800;

        color: #123b5d !important;

        margin-bottom: 7px;
    }

    .info-text {
        font-size: 13px;

        line-height: 1.7;

        color: #6c7e90 !important;
    }


    /* ========================================================
       SECTION
    ======================================================== */

    .section-header {
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .section-title {
        font-size: 20px;

        font-weight: 800;

        color: #123b5d !important;

        margin-bottom: 4px;
    }

    .section-description {
        font-size: 13px;

        color: #78899a !important;

        line-height: 1.6;
    }


    /* ========================================================
       INPUT CARD
    ======================================================== */

    .input-card {
        background: #ffffff;

        border: 1px solid #e6edf4;

        border-radius: 20px;

        padding: 22px;

        margin-bottom: 12px;

        box-shadow:
            0 8px 25px rgba(20,50,80,0.05);
    }

    .input-icon {
        width: 46px;
        height: 46px;

        border-radius: 13px;

        background: #edf4fa;

        display: flex;
        align-items: center;
        justify-content: center;

        font-size: 22px;

        margin-bottom: 14px;
    }

    .input-title {
        font-size: 18px;

        font-weight: 800;

        color: #123b5d !important;

        margin-bottom: 4px;
    }

    .input-description {
        font-size: 12px;

        color: #8190a0 !important;

        line-height: 1.5;
    }


    /* ========================================================
       RESULT CARD
    ======================================================== */

    /* ========================================================
       PREMIUM SYSTEM FLOW
       ======================================================== */

    .flow-section { margin-top: 38px; margin-bottom: 18px; }
    .flow-heading { font-size: 21px; font-weight: 850; color: #0b2845 !important; margin-bottom: 5px; }
    .flow-description { font-size: 13px; color: #78899a !important; line-height: 1.6; }
    .flow-wrapper { display: grid; grid-template-columns: 1fr 34px 1fr 34px 1fr 34px 1fr; align-items: stretch; gap: 0; margin-top: 20px; }
    .flow-card { position: relative; min-height: 185px; padding: 23px; background: rgba(255,255,255,0.96); border: 1px solid #e2eaf2; border-radius: 20px; box-shadow: 0 10px 28px rgba(13,48,78,0.055); transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease; }
    .flow-card:hover { transform: translateY(-5px); border-color: #b9ccdd; box-shadow: 0 18px 38px rgba(13,48,78,0.11); }
    .flow-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 22px; }
    .flow-number { display: flex; align-items: center; justify-content: center; width: 34px; height: 34px; border-radius: 10px; background: #0b3153; color: #ffffff !important; font-size: 11px; font-weight: 850; letter-spacing: 0.5px; }
    .flow-icon { font-size: 21px; opacity: 0.85; }
    .flow-title { font-size: 17px; font-weight: 850; color: #123b5d !important; margin-bottom: 9px; }
    .flow-text { font-size: 12px; line-height: 1.65; color: #718397 !important; }
    .flow-line { display: flex; align-items: center; justify-content: center; }
    .flow-line-inner { width: 24px; height: 2px; background: #b9c9d8; position: relative; }
    .flow-line-inner:after { content: ""; position: absolute; right: -1px; top: -4px; width: 8px; height: 8px; border-top: 2px solid #8da5ba; border-right: 2px solid #8da5ba; transform: rotate(45deg); }
    .flow-note { margin-top: 15px; padding: 12px 15px; border-radius: 12px; background: #edf4f9; color: #567086 !important; font-size: 11px; text-align: center; }
    @media (max-width: 1000px) { .flow-wrapper { grid-template-columns: 1fr 1fr; gap: 14px; } .flow-line { display: none; } }
    @media (max-width: 650px) { .flow-wrapper { grid-template-columns: 1fr; } }

    .result-card {
        background:
            linear-gradient(
                135deg,
                #082b4d,
                #154d78
            );

        border-radius: 24px;

        padding: 38px;

        text-align: center;

        color: white;

        box-shadow:
            0 18px 40px rgba(8,43,77,0.18);

        margin-top: 10px;
    }

    .result-label {
        color: #b7cede !important;

        font-size: 11px;

        font-weight: 800;

        letter-spacing: 2px;
    }

    .result-score {
        font-size: 65px;

        line-height: 1;

        font-weight: 900;

        color: #ffffff !important;

        margin: 18px 0;
    }

    .result-score span {
        font-size: 17px;

        color: #b9cddd !important;

        font-weight: 500;
    }

    .result-badge {
        display: inline-block;

        padding: 9px 22px;

        border-radius: 50px;

        background: rgba(255,255,255,0.13);

        border: 1px solid rgba(255,255,255,0.20);

        color: #ffffff !important;

        font-size: 12px;

        font-weight: 800;

        letter-spacing: 1.3px;
    }


    /* ========================================================
       STREAMLIT METRIC
    ======================================================== */

    div[data-testid="stMetric"] {
        background: #ffffff;

        border: 1px solid #e7edf3;

        padding: 18px;

        border-radius: 17px;

        box-shadow:
            0 6px 20px rgba(20,50,80,0.04);
    }

    div[data-testid="stMetricLabel"] {
        color: #75879a !important;
    }


    /* ========================================================
       BUTTON
    ======================================================== */

    .stButton > button {
        border-radius: 11px;

        border: none;

        background: #0d426c;

        color: white;

        font-weight: 750;

        min-height: 44px;

        transition: 0.2s;
    }

    .stButton > button:hover {
        background: #082b4d;

        color: white;
    }


    /* ========================================================
       DATAFRAME
    ======================================================== */

    [data-testid="stDataFrame"] {
        border-radius: 14px;
        overflow: hidden;
    }


    /* ========================================================
       FOOTER
    ======================================================== */

    .footer {
        margin-top: 45px;

        padding: 22px;

        text-align: center;

        border-top: 1px solid #e0e7ee;

        color: #8191a2 !important;

        font-size: 11px;

        line-height: 1.7;
    }

    </style>
    """
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    render_html(
        """
        <div class="sidebar-brand">

            <div class="sidebar-logo">
                🎓
            </div>

            <div class="sidebar-title">
                SIBEA
            </div>

            <div class="sidebar-subtitle">
                Sistem Penilaian<br>
                Kelayakan Beasiswa
            </div>

        </div>
        """
    )

    render_html(
        """
        <div class="sidebar-section">
            NAVIGASI
        </div>
        """
    )

    menu = st.radio(
        "Navigasi",
        [
            "🏠 Dashboard",
            "🧮 Penilaian Beasiswa",
            "📋 Rule Fuzzy",
            "📈 Membership Function",
            "ℹ️ Tentang Sistem",
        ],
        label_visibility="collapsed",
    )

    render_html(
        """
        <div class="sidebar-footer">
            <b>SIBEA</b><br>
            Artificial Intelligence<br>
            Fuzzy Logic Scholarship Assessment
        </div>
        """
    )


# ============================================================
# DASHBOARD
# ============================================================

if menu == "🏠 Dashboard":

    render_html(
        """
        <div class="page-kicker">
            SCHOLARSHIP ELIGIBILITY ASSESSMENT
        </div>

        <div class="page-title">
            Sistem Penilaian Kelayakan Beasiswa
        </div>

        <div class="page-description">
            Sistem penilaian kelayakan beasiswa menggunakan
            metode Fuzzy Logic untuk membantu proses evaluasi
            mahasiswa berdasarkan IPK, penghasilan orang tua,
            dan prestasi.
        </div>
        """
    )

    render_html(
        """
        <div class="hero-card">

            <div class="hero-label">
                FUZZY ASSESSMENT SYSTEM
            </div>

            <div class="hero-title">
                Evaluasi Beasiswa Berbasis Fuzzy Logic
            </div>

            <div class="hero-text">
                SIBEA mengolah tiga parameter utama mahasiswa
                melalui proses fuzzifikasi, fuzzy inference,
                dan defuzzifikasi untuk menghasilkan nilai
                kelayakan beasiswa.
            </div>

        </div>
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        render_html(
            """
            <div class="info-card">

                <div class="info-icon">
                    ⚙️
                </div>

                <div class="info-label">
                    METODE
                </div>

                <div class="info-value">
                    Fuzzy Logic
                </div>

                <div class="info-text">
                    Metode fuzzy digunakan untuk memproses
                    parameter yang memiliki nilai linguistik
                    seperti rendah, sedang, dan tinggi.
                </div>

            </div>
            """
        )

    with col2:

        render_html(
            """
            <div class="info-card">

                <div class="info-icon">
                    📊
                </div>

                <div class="info-label">
                    INPUT
                </div>

                <div class="info-value">
                    3 Parameter
                </div>

                <div class="info-text">
                    IPK, penghasilan orang tua,
                    dan prestasi mahasiswa digunakan
                    sebagai input sistem.
                </div>

            </div>
            """
        )

    with col3:

        render_html(
            """
            <div class="info-card">

                <div class="info-icon">
                    🎯
                </div>

                <div class="info-label">
                    RULE
                </div>

                <div class="info-value">
                    27 Rules
                </div>

                <div class="info-text">
                    Sistem menggunakan 27 aturan fuzzy
                    untuk menentukan tingkat kelayakan.
                </div>

            </div>
            """
        )

    render_html(
        """
        <div class="flow-section">
            <div class="flow-heading">Alur Sistem</div>
            <div class="flow-description">
                Empat tahapan utama dalam proses penilaian kelayakan
                beasiswa menggunakan Fuzzy Logic.
            </div>
        </div>

        <div class="flow-wrapper">
            <div class="flow-card">
                <div class="flow-top">
                    <div class="flow-number">01</div>
                    <div class="flow-icon">📝</div>
                </div>
                <div class="flow-title">Input Data</div>
                <div class="flow-text">
                    Data mahasiswa berupa IPK, penghasilan orang tua,
                    dan nilai prestasi dimasukkan ke dalam sistem.
                </div>
            </div>

            <div class="flow-line"><div class="flow-line-inner"></div></div>

            <div class="flow-card">
                <div class="flow-top">
                    <div class="flow-number">02</div>
                    <div class="flow-icon">📊</div>
                </div>
                <div class="flow-title">Fuzzifikasi</div>
                <div class="flow-text">
                    Nilai input diubah menjadi derajat keanggotaan
                    seperti rendah, sedang, dan tinggi.
                </div>
            </div>

            <div class="flow-line"><div class="flow-line-inner"></div></div>

            <div class="flow-card">
                <div class="flow-top">
                    <div class="flow-number">03</div>
                    <div class="flow-icon">⚙️</div>
                </div>
                <div class="flow-title">Fuzzy Inference</div>
                <div class="flow-text">
                    Sistem mengevaluasi 27 rule fuzzy menggunakan
                    firing strength untuk menentukan hasil inferensi.
                </div>
            </div>

            <div class="flow-line"><div class="flow-line-inner"></div></div>

            <div class="flow-card">
                <div class="flow-top">
                    <div class="flow-number">04</div>
                    <div class="flow-icon">🎯</div>
                </div>
                <div class="flow-title">Defuzzifikasi</div>
                <div class="flow-text">
                    Hasil fuzzy diubah menjadi nilai kelayakan akhir
                    pada skala 0 sampai 100.
                </div>
            </div>
        </div>

        <div class="flow-note">
            <b>Input → Fuzzifikasi → Fuzzy Inference → Defuzzifikasi</b>
            &nbsp; • &nbsp; Menghasilkan nilai kelayakan beasiswa
        </div>
        """
    )


# ============================================================
# PENILAIAN BEASISWA
# ============================================================

elif menu == "🧮 Penilaian Beasiswa":

    render_html(
        """
        <div class="page-kicker">
            SCHOLARSHIP ASSESSMENT
        </div>

        <div class="page-title">
            Penilaian Kelayakan Beasiswa
        </div>

        <div class="page-description">
            Masukkan data mahasiswa untuk mendapatkan nilai
            kelayakan beasiswa menggunakan metode Fuzzy Logic.
        </div>
        """
    )

    render_html(
        """
        <div class="hero-card">

            <div class="hero-label">
                FUZZY ASSESSMENT ENGINE
            </div>

            <div class="hero-title">
                Masukkan Data Mahasiswa
            </div>

            <div class="hero-text">
                Sistem akan memproses IPK, penghasilan orang tua,
                dan prestasi melalui membership function dan
                27 aturan fuzzy.
            </div>

        </div>
        """
    )

    col1, col2, col3 = st.columns(
        3,
        gap="large",
    )


    # --------------------------------------------------------
    # IPK
    # --------------------------------------------------------

    with col1:

        render_html(
            """
            <div class="input-card">

                <div class="input-icon">
                    📚
                </div>

                <div class="input-title">
                    IPK
                </div>

                <div class="input-description">
                    Indeks Prestasi Kumulatif mahasiswa
                </div>

            </div>
            """
        )

        nilai_ipk = st.number_input(
            "Nilai IPK",
            min_value=0.0,
            max_value=4.0,
            value=3.65,
            step=0.01,
            format="%.2f",
            key="input_ipk",
        )

        st.caption(
            "Rentang nilai: 0.00 – 4.00"
        )


    # --------------------------------------------------------
    # PENGHASILAN
    # --------------------------------------------------------

    with col2:

        render_html(
            """
            <div class="input-card">

                <div class="input-icon">
                    💰
                </div>

                <div class="input-title">
                    Penghasilan
                </div>

                <div class="input-description">
                    Penghasilan orang tua per bulan
                </div>

            </div>
            """
        )

        nilai_penghasilan = st.number_input(
            "Penghasilan Orang Tua",
            min_value=0,
            max_value=10_000_000,
            value=2_500_000,
            step=100_000,
            format="%d",
            key="input_penghasilan",
        )

        st.caption(
            f"Rp {nilai_penghasilan:,.0f}".replace(",", ".")
            + " / bulan"
        )


    # --------------------------------------------------------
    # PRESTASI
    # --------------------------------------------------------

    with col3:

        render_html(
            """
            <div class="input-card">

                <div class="input-icon">
                    🏆
                </div>

                <div class="input-title">
                    Prestasi
                </div>

                <div class="input-description">
                    Nilai prestasi mahasiswa
                </div>

            </div>
            """
        )

        nilai_prestasi = st.number_input(
            "Nilai Prestasi",
            min_value=0.0,
            max_value=100.0,
            value=80.0,
            step=1.0,
            format="%.0f",
            key="input_prestasi",
        )

        st.caption(
            "Rentang nilai: 0 – 100"
        )


    # --------------------------------------------------------
    # BUTTON
    # --------------------------------------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    proses = st.button(
        "🔍  Hitung Kelayakan Beasiswa",
        use_container_width=True,
    )


    # --------------------------------------------------------
    # PROSES
    # --------------------------------------------------------

    if proses:

        # Penghasilan di fuzzy_logic menggunakan satuan juta
        penghasilan_juta = nilai_penghasilan / 1_000_000

        nilai_kelayakan, kategori = hitung_beasiswa(
            nilai_ipk,
            penghasilan_juta,
            nilai_prestasi,
        )


        # ----------------------------------------------------
        # HASIL
        # ----------------------------------------------------

        render_html(
            f"""
            <div class="result-card">

                <div class="result-label">
                    NILAI KELAYAKAN BEASISWA
                </div>

                <div class="result-score">
                    {nilai_kelayakan:.2f}
                    <span>/ 100</span>
                </div>

                <div class="result-badge">
                    {kategori.upper()}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # RINGKASAN INPUT
        # ----------------------------------------------------

        st.markdown("<br>", unsafe_allow_html=True)

        m1, m2, m3 = st.columns(3)

        with m1:

            st.metric(
                "IPK",
                f"{nilai_ipk:.2f}",
            )

        with m2:

            st.metric(
                "Penghasilan",
                f"Rp {nilai_penghasilan:,.0f}".replace(",", "."),
            )

        with m3:

            st.metric(
                "Prestasi",
                f"{nilai_prestasi:.0f}",
            )


        # ----------------------------------------------------
        # MEMBERSHIP
        # ----------------------------------------------------

        membership = hitung_membership(
            nilai_ipk,
            penghasilan_juta,
            nilai_prestasi,
        )

        render_html(
            """
            <div class="section-header">

                <div class="section-title">
                    Derajat Keanggotaan
                </div>

                <div class="section-description">
                    Hasil proses fuzzifikasi dari setiap parameter
                    input mahasiswa.
                </div>

            </div>
            """
        )


        tabel_membership = pd.DataFrame(
            [
                {
                    "Variabel": "IPK",
                    "Nilai Input": nilai_ipk,
                    "Rendah": membership["ipk"]["rendah"],
                    "Sedang": membership["ipk"]["sedang"],
                    "Tinggi": membership["ipk"]["tinggi"],
                },
                {
                    "Variabel": "Penghasilan",
                    "Nilai Input": (
                        f"Rp {nilai_penghasilan:,.0f}"
                        .replace(",", ".")
                    ),
                    "Rendah": membership["penghasilan"]["rendah"],
                    "Sedang": membership["penghasilan"]["sedang"],
                    "Tinggi": membership["penghasilan"]["tinggi"],
                },
                {
                    "Variabel": "Prestasi",
                    "Nilai Input": nilai_prestasi,
                    "Rendah": membership["prestasi"]["rendah"],
                    "Sedang": membership["prestasi"]["sedang"],
                    "Tinggi": membership["prestasi"]["tinggi"],
                },
            ]
        )


        for kolom in [
            "Rendah",
            "Sedang",
            "Tinggi",
        ]:

            tabel_membership[kolom] = (
                tabel_membership[kolom].round(3)
            )


        st.dataframe(
            tabel_membership,
            use_container_width=True,
            hide_index=True,
        )


        # ----------------------------------------------------
        # RULE AKTIF
        # ----------------------------------------------------

        render_html(
            """
            <div class="section-header">

                <div class="section-title">
                    Rule Fuzzy Aktif
                </div>

                <div class="section-description">
                    Rule dengan firing strength lebih besar
                    dari 0 akan digunakan dalam proses inferensi.
                </div>

            </div>
            """
        )


        rule_aktif = hitung_firing_strength(
            membership
        )

        rule_aktif = [
            rule
            for rule in rule_aktif
            if rule["firing_strength"] > 0
        ]


        # Urutkan rule berdasarkan firing strength
        rule_aktif = sorted(
            rule_aktif,
            key=lambda x: x["firing_strength"],
            reverse=True,
        )


        if rule_aktif:

            tabel_rule = pd.DataFrame(
                [
                    {
                        "Rule": rule["rule"],
                        "Kondisi": rule["kondisi"],
                        "Output": rule["output"],
                        "Firing Strength": round(
                            rule["firing_strength"],
                            3,
                        ),
                    }
                    for rule in rule_aktif
                ]
            )


            st.dataframe(
                tabel_rule,
                use_container_width=True,
                hide_index=True,
            )


            rule_terkuat = rule_aktif[0]


            st.info(
                f"⭐ Rule terkuat: "
                f"{rule_terkuat['rule']}  •  "
                f"Firing Strength = "
                f"{rule_terkuat['firing_strength']:.3f}  →  "
                f"{rule_terkuat['output']}"
            )

        else:

            st.warning(
                "Tidak ada rule fuzzy yang aktif."
            )


# ============================================================
# RULE FUZZY
# ============================================================

elif menu == "📋 Rule Fuzzy":

    render_html(
        """
        <div class="page-kicker">
            FUZZY KNOWLEDGE BASE
        </div>

        <div class="page-title">
            Rule Fuzzy
        </div>

        <div class="page-description">
            Daftar 27 aturan fuzzy yang digunakan dalam
            sistem penilaian kelayakan beasiswa.
        </div>
        """
    )


    data_rule = []


    # rule_data berbentuk:
    # (nomor, ipk, penghasilan, prestasi, output)

    for rule in rule_data:

        nomor = rule[0]
        ipk_kat = rule[1]
        penghasilan_kat = rule[2]
        prestasi_kat = rule[3]
        output = rule[4]


        data_rule.append(
            {
                "Rule": nomor,
                "IPK": ipk_kat,
                "Penghasilan": penghasilan_kat,
                "Prestasi": prestasi_kat,
                "Output": output,
            }
        )


    df_rule = pd.DataFrame(
        data_rule
    )


    st.dataframe(
        df_rule,
        use_container_width=True,
        hide_index=True,
        height=650,
    )


# ============================================================
# MEMBERSHIP FUNCTION
# ============================================================

elif menu == "📈 Membership Function":

    render_html(
        """
        <div class="page-kicker">
            FUZZY MEMBERSHIP
        </div>

        <div class="page-title">
            Membership Function
        </div>

        <div class="page-description">
            Visualisasi fungsi keanggotaan yang digunakan
            dalam sistem Fuzzy Logic.
        </div>
        """
    )


    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📚 IPK",
            "💰 Penghasilan",
            "🏆 Prestasi",
            "🎯 Kelayakan",
        ]
    )


    # --------------------------------------------------------
    # IPK
    # --------------------------------------------------------

    with tab1:

        fig, ax = plt.subplots(
            figsize=(10, 4)
        )


        for nama in [
            "rendah",
            "sedang",
            "tinggi",
        ]:

            ax.plot(
                ipk.universe,
                ipk[nama].mf,
                label=nama.capitalize(),
                linewidth=2,
            )


        ax.set_title(
            "Membership Function IPK"
        )

        ax.set_xlabel(
            "IPK"
        )

        ax.set_ylabel(
            "Derajat Keanggotaan"
        )

        ax.legend()
        ax.grid(alpha=0.2)

        st.pyplot(fig)

        plt.close(fig)


    # --------------------------------------------------------
    # PENGHASILAN
    # --------------------------------------------------------

    with tab2:

        fig, ax = plt.subplots(
            figsize=(10, 4)
        )


        for nama in [
            "rendah",
            "sedang",
            "tinggi",
        ]:

            ax.plot(
                penghasilan.universe,
                penghasilan[nama].mf,
                label=nama.capitalize(),
                linewidth=2,
            )


        ax.set_title(
            "Membership Function Penghasilan Orang Tua"
        )

        ax.set_xlabel(
            "Penghasilan (Juta Rupiah)"
        )

        ax.set_ylabel(
            "Derajat Keanggotaan"
        )

        ax.legend()
        ax.grid(alpha=0.2)

        st.pyplot(fig)

        plt.close(fig)


    # --------------------------------------------------------
    # PRESTASI
    # --------------------------------------------------------

    with tab3:

        fig, ax = plt.subplots(
            figsize=(10, 4)
        )


        for nama in [
            "rendah",
            "sedang",
            "tinggi",
        ]:

            ax.plot(
                prestasi.universe,
                prestasi[nama].mf,
                label=nama.capitalize(),
                linewidth=2,
            )


        ax.set_title(
            "Membership Function Prestasi"
        )

        ax.set_xlabel(
            "Nilai Prestasi"
        )

        ax.set_ylabel(
            "Derajat Keanggotaan"
        )

        ax.legend()
        ax.grid(alpha=0.2)

        st.pyplot(fig)

        plt.close(fig)


    # --------------------------------------------------------
    # KELAYAKAN
    # --------------------------------------------------------

    with tab4:

        fig, ax = plt.subplots(
            figsize=(10, 4)
        )


        for nama in [
            "tidak_layak",
            "dipertimbangkan",
            "layak",
        ]:

            ax.plot(
                kelayakan.universe,
                kelayakan[nama].mf,
                label=nama.replace(
                    "_",
                    " "
                ).title(),
                linewidth=2,
            )


        ax.set_title(
            "Membership Function Kelayakan"
        )

        ax.set_xlabel(
            "Nilai Kelayakan"
        )

        ax.set_ylabel(
            "Derajat Keanggotaan"
        )

        ax.legend()
        ax.grid(alpha=0.2)

        st.pyplot(fig)

        plt.close(fig)


# ============================================================
# TENTANG SISTEM
# ============================================================

elif menu == "ℹ️ Tentang Sistem":

    render_html(
        """
        <div class="page-kicker">
            ABOUT SIBEA
        </div>

        <div class="page-title">
            Tentang Sistem
        </div>

        <div class="page-description">
            Informasi mengenai Sistem Penilaian Kelayakan
            Beasiswa berbasis Fuzzy Logic.
        </div>
        """
    )


    render_html(
        """
        <div class="hero-card">

            <div class="hero-label">
                SIBEA
            </div>

            <div class="hero-title">
                Sistem Penilaian Kelayakan Beasiswa
            </div>

            <div class="hero-text">
                SIBEA merupakan prototype sistem berbasis
                Artificial Intelligence yang menggunakan metode
                Fuzzy Logic untuk membantu proses penilaian
                kelayakan beasiswa mahasiswa.
            </div>

        </div>
        """
    )


    col1, col2 = st.columns(2)


    with col1:

        render_html(
            """
            <div class="info-card">

                <div class="info-label">
                    INPUT SISTEM
                </div>

                <div class="info-value">
                    Parameter Penilaian
                </div>

                <div class="info-text">

                    • IPK mahasiswa<br>
                    • Penghasilan orang tua<br>
                    • Prestasi mahasiswa

                </div>

            </div>
            """
        )


    with col2:

        render_html(
            """
            <div class="info-card">

                <div class="info-label">
                    OUTPUT SISTEM
                </div>

                <div class="info-value">
                    Nilai Kelayakan
                </div>

                <div class="info-text">

                    Sistem menghasilkan nilai kelayakan
                    0–100 dengan kategori Layak,
                    Dipertimbangkan, atau Tidak Layak.

                </div>

            </div>
            """
        )


    render_html(
        """
        <div class="section-header">

            <div class="section-title">
                Teknologi yang Digunakan
            </div>

        </div>
        """
    )


    t1, t2, t3, t4 = st.columns(4)


    with t1:
        st.metric(
            "Language",
            "Python",
        )


    with t2:
        st.metric(
            "Framework",
            "Streamlit",
        )


    with t3:
        st.metric(
            "AI Method",
            "Fuzzy Logic",
        )


    with t4:
        st.metric(
            "Library",
            "Scikit-Fuzzy",
        )


# ============================================================
# FOOTER
# ============================================================

render_html(
    """
    <div class="footer">

        <b>SIBEA</b> — Sistem Penilaian Kelayakan Beasiswa

        <br>

        Artificial Intelligence • Fuzzy Logic

    </div>
    """
)