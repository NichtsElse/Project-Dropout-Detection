import streamlit as st
import pandas as pd
import joblib

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Deteksi Dropout Mahasiswa",
    page_icon="🎓",
    layout="centered"
)

# 2. Load Model
@st.cache_resource
def load_model():
    return joblib.load('model_do_prediction.pkl')

try:
    model = load_model()
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

# 3. Header Aplikasi
st.title("🎓 Sistem Prediksi Dropout Mahasiswa")
st.markdown("Masukkan data mahasiswa pada masing-masing kategori di bawah ini, lalu klik tombol **Proses Prediksi**.")
st.markdown("---")

# 4. Membuat Tabs untuk Kategori Input
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👤 Profil & Demografi", 
    "🏫 Akademik Awal", 
    "💰 Finansial", 
    "📊 Semester 1", 
    "📈 Semester 2"
])

# Kategori 1: Profil & Demografi
with tab1:
    st.subheader("Data Demografi Mahasiswa")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Laki-laki" if x == 1 else "Perempuan")
        age = st.number_input("Age at Enrollment (Usia Masuk)", min_value=15, max_value=80, value=20)
    with col2:
        marital = st.selectbox("Marital Status", options=[1, 2, 3, 4, 5, 6], help="1: Single, 2: Married, 3: Widower, 4: Divorced, 5: Facto Union, 6: Legally Separated")
        displaced = st.selectbox("Displaced (Pindahan)", options=[0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")

# Kategori 2: Akademik Awal
with tab2:
    st.subheader("Latar Belakang Akademik")
    col1, col2 = st.columns(2)
    with col1:
        app_mode = st.number_input("Application Mode (Jalur Masuk)", value=1, help="Kode jalur pendaftaran (contoh: 1, 15, 17, 39, dst)")
    with col2:
        prev_grade = st.number_input("Previous Qualification Grade (Nilai Kelulusan Sebelumnya)", value=120.0, step=1.0)
        adm_grade = st.number_input("Admission Grade (Nilai Masuk)", value=120.0, step=1.0)

# Kategori 3: Finansial
with tab3:
    st.subheader("Status Finansial")
    col1, col2 = st.columns(2)
    with col1:
        scholarship = st.selectbox("Scholarship Holder (Penerima Beasiswa)", options=[0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
        debtor = st.selectbox("Debtor (Memiliki Hutang)", options=[0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
    with col2:
        tuition = st.selectbox("Tuition Fees Up to Date (Pembayaran UKT)", options=[0, 1], format_func=lambda x: "Lancar (1)" if x == 1 else "Menunggak (0)")

# Kategori 4: Kinerja Semester 1
with tab4:
    st.subheader("Performa Akademik - Semester 1")
    col1, col2 = st.columns(2)
    with col1:
        s1_enrolled = st.number_input("Curricular Units 1st Sem Enrolled", value=6)
        s1_approved = st.number_input("Curricular Units 1st Sem Approved", value=5)
    with col2:
        s1_grade = st.number_input("Curricular Units 1st Sem Grade", value=12.0, step=0.1)

# Kategori 5: Kinerja Semester 2
with tab5:
    st.subheader("Performa Akademik - Semester 2")
    col1, col2 = st.columns(2)
    with col1:
        s2_enrolled = st.number_input("Curricular Units 2nd Sem Enrolled", value=6)
        s2_eval = st.number_input("Curricular Units 2nd Sem Evaluations", value=6)
        s2_no_eval = st.number_input("Curricular Units 2nd Sem Without Eval", value=0)
    with col2:
        s2_approved = st.number_input("Curricular Units 2nd Sem Approved", value=5)
        s2_grade = st.number_input("Curricular Units 2nd Sem Grade", value=12.0, step=0.1)

st.markdown("---")

# 5. Tombol Proses & Logika Prediksi
if st.button("📊 Proses Prediksi", use_container_width=True):
    # Menyusun data sesuai dengan urutan fitur yang diminta model
    input_features = {
        'Age_at_enrollment': age,
        'Debtor': debtor,
        'Gender': gender,
        'Application_mode': app_mode,
        'Curricular_units_2nd_sem_without_evaluations': s2_no_eval,
        'Marital_status': marital,
        'Previous_qualification_grade': prev_grade,
        'Curricular_units_2nd_sem_evaluations': s2_eval,
        'Displaced': displaced,
        'Admission_grade': adm_grade,
        'Curricular_units_1st_sem_enrolled': s1_enrolled,
        'Curricular_units_2nd_sem_enrolled': s2_enrolled,
        'Scholarship_holder': scholarship,
        'Tuition_fees_up_to_date': tuition,
        'Curricular_units_1st_sem_grade': s1_grade,
        'Curricular_units_1st_sem_approved': s1_approved,
        'Curricular_units_2nd_sem_grade': s2_grade,
        'Curricular_units_2nd_sem_approved': s2_approved
    }
    
    df_input = pd.DataFrame([input_features])
    
    # Prediksi
    prediction = model.predict(df_input)
    prediction_proba = model.predict_proba(df_input)

    st.markdown("---")
    st.subheader("💡 Hasil Analisis:")
    
    if prediction[0] == 1:
        st.error(f"⚠️ **STATUS: BERISIKO TINGGI (DROPOUT)**")
        st.write(f"Tingkat Keyakinan Model: **{prediction_proba[0][1]*100:.2f}%**")
        st.warning("Rekomendasi: Segera jadwalkan sesi bimbingan konseling dan akademik untuk mahasiswa ini.")
    else:
        st.success(f"✅ **STATUS: AMAN (DIPREDIKSI LULUS/GRADUATE)**")
        st.write(f"Tingkat Keyakinan Model: **{prediction_proba[0][0]*100:.2f}%**")

st.markdown("---")
st.caption("Proyek Data Science - Jaya Jaya Institut")
