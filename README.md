# Proyek Akhir: Menyelesaikan Permasalahan Dropout Mahasiswa Jaya Jaya Institusi

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Meskipun telah mencetak banyak lulusan berprestasi, institusi ini menghadapi masalah tingginya angka mahasiswa yang putus kuliah (*dropout*). Tingginya angka *dropout* ini menjadi masalah besar karena berdampak pada reputasi institusi dan efisiensi operasional pendidikan. Oleh karena itu, Departemen Akademik Jaya Jaya Institut membutuhkan alat analisis dan prediksi untuk mendeteksi secepat mungkin siswa yang berisiko melakukan *dropout* agar dapat diberikan bimbingan khusus.

### Permasalahan Bisnis

Beberapa permasalahan utama yang dihadapi oleh institusi:

1. Faktor-faktor apa saja yang paling signifikan mempengaruhi keputusan seorang mahasiswa untuk putus kuliah (*dropout*)?
2. Bagaimana cara mengidentifikasi atau memprediksi mahasiswa yang berisiko tinggi untuk *dropout* sejak dini berdasarkan data profil dan kinerja akademis mereka?
3. Bagaimana memonitor performa mahasiswa dan tren *dropout* secara interaktif melalui *dashboard*?

### Cakupan Proyek

Cakupan proyek ini meliputi:

1. **Data Wrangling & Exploratory Data Analysis (EDA)**: Memahami karakteristik dataset `data.csv`, membersihkan data, memfilter status mahasiswa yang masih aktif belajar (*Enrolled*), dan menganalisis hubungan visual antara berbagai metrik (seperti nilai semester, status pembayaran UKT, usia) terhadap status kelulusan.
2. **Data Preprocessing**: Melakukan persiapan data untuk pemodelan, seperti pemisahan fitur dan target (*Dropout* vs *Graduate*), serta pembagian data menjadi *training* dan *testing set*.
3. **Machine Learning Modeling**: Membangun, melatih, dan mengevaluasi dua model klasifikasi menggunakan algoritma **Random Forest** dan **Gradient Boosting**. Model *Gradient Boosting* dipilih sebagai model final karena menghasilkan performa terbaik.
4. **Deployment**: Membuat purwarupa (*prototype*) aplikasi *machine learning* interaktif menggunakan Streamlit dan menghubungkannya dengan Streamlit Community Cloud agar siap digunakan dan diakses secara *remote*.
5. **Pembuatan Business Dashboard**: Menggunakan Looker Studio / Metabase / Tableau untuk memantau performa siswa dan metrik *dropout* secara interaktif.

### Persiapan

Sumber data: Dataset Mahasiswa Jaya Jaya Institut (`data.csv`)

Setup environment:
```bash
# Aktifkan virtual environment di terminal
conda create --name jaya-dropout python=3.9
# Aktifkan virtual environment
conda activate jaya-dropout
# Instal semua library yang dibutuhkan
pip install -r requirements.txt
```

## Business Dashboard

Dashboard dibuat menggunakan Looker Studio untuk membantu institusi memonitor performa siswa. Dashboard ini menampilkan metrik penting seperti persentase *dropout*, sebaran *dropout* berdasarkan jurusan, dan korelasi antara status pembayaran uang kuliah dengan tingkat *dropout*.Dashboard menampilkan beberapa visualisasi utama:

Metrik total mahasiswa dan tingkat persentase dropout.

Tingkat dropout berdasarkan program studi/jurusan (Course).

Tingkat dropout berdasarkan status pembayaran uang kuliah (Tuition fees up to date).

Perbandingan performa akademik (rata-rata nilai Semester 1 dan 2) antara mahasiswa yang dropout dan yang graduate.

Link Dashboard: https://lookerstudio.google.com/reporting/b1edfca2-ce68-474d-ab1d-4e810e1b026c

Link Aplikasi Prediksi (Streamlit): https://jaya-dropout-prediction.streamlit.app/

## Conclusion & Action Items
**Kesimpulan:**
Berdasarkan analisis data yang telah dilakukan, ditemukan beberapa faktor utama yang mempengaruhi tingginya tingkat dropout mahasiswa:

Kinerja Akademis: Mahasiswa yang memiliki jumlah mata kuliah yang lulus (approved units) dan nilai (grade) yang rendah pada Semester 1 dan Semester 2 memiliki kecenderungan sangat tinggi untuk dropout.

Faktor Finansial: Mahasiswa yang telat atau menunggak pembayaran uang kuliah (Tuition fees up to date = 0) memiliki persentase dropout yang jauh lebih tinggi dibandingkan mahasiswa yang membayar tepat waktu.

Usia saat Mendaftar: Mahasiswa yang mendaftar pada usia yang lebih tua (Age at enrollment) menunjukkan risiko dropout yang lebih tinggi, kemungkinan karena beban ganda dengan pekerjaan atau tanggung jawab keluarga.

**Rekomendasi Action Items:**
1. **Sistem Peringatan Dini (Early Warning System):** Pantau ketat mahasiswa yang memiliki tingkat kelulusan mata kuliah (*approved units*) dan nilai yang rendah di akhir Semester 1. Segera panggil mereka untuk sesi konseling akademik.
2. **Keringanan/Restrukturisasi Pembayaran UKT:** Karena fitur `Tuition_fees_up_to_date` sangat berpengaruh, institusi disarankan untuk proaktif menawarkan skema cicilan atau bantuan finansial/beasiswa bagi mahasiswa yang mulai menunggak biaya kuliah sebelum mereka memutuskan untuk *dropout*.
3. **Program Mentorship Tahun Pertama:** Mengingat performa di dua semester awal sangat krusial, bentuk program *mentoring* di mana mahasiswa tingkat akhir membimbing mahasiswa baru agar lebih adaptif terhadap kehidupan kampus.