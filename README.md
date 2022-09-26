# Predictive-Analystics
# LAPORAN PROYEK PREDICTIVE ANALYTICS - PUTRI WULANDARI

**Domain Proyek** 

	 Domain proyek yang saya pilih ialah tema kesehatan dengan judul proyek "Prediksi Penyakit Kanker Payudara pada Manusia atau Wanita".
**Latar Belakang**

Kanker payudara ialah kanker paling umum pada wanita di seluruh dunia dengan menyumbang 25,4% dari total jumlah kasus baru yang didiagnosis pada tahun 2018. Kanker adalah sekelompok besar penyakit yang dapat dimulai di hampir semua organ atau jaringan tubuh ketika sel abnormal tumbuh tak terkendali, melampaui batas biasanya untuk menyerang bagian tubuh yang berdekatan dan atau menyebar ke organ lain [1]. Merujuk data yang dipaparkan Kemenkes per 31 Januari 2019, terdapat angka kanker payudara 42,1 per 100.000 penduduk dengan rata-rata kematian 17 per 100.000 penduduk [2]. Penyakit ini merupakan salah satu penyakit yang menjadi momok bagi kaum wanita walaupun tidak menutup kemungkinan pria juga bisa terkena penyakit ini. Dimana, menjadi momok bagi kaum wanita karena penyakit ini menyerang bagian tubuh yang menjadi salah satu ciri khas kaum wanita. Kanker payudara merupakan penyakit yang tidak menular yang cenderung terus meningkat setiap tahunnya, sehingga dapat dikatakan bahwa beban yang harus ditanggung dunia akibat penyakit tersebut semakin meningkat [3]. 

Mulai dari tahun 2008 terdapat 12,7 juta kasus kanker di dunia dan terus menerus mengalami peningkatan hingga tahun 2018 menjadi 18,1 juta kasus kanker. Kematian yang disebabkan oleh kanker juga mengalami peningkatan dari 7,6 juta pada tahun 2008 menjadi 9,6 juta pada tahun 2018. IARC menyatakan bahwa terjadi peningkatan kasus kanker payudara yang menyerang wanita dengan tingkat kematian sebesar 627.000 di seluruh dunia. Berdasarkan data dari Riset Kesehatan Dasar (RISKESDAS) tahun 2018 jumlah kejadian kanker payudara yang menyerang wanita adalah sebesar 42,1 per 100.000 penduduk dengan rata-rata kematian 17 per 100.000 penduduk dan data pada tahun 2012 sebesar 12,1 per 100.000 penduduk dengan jumlah kematian secara keseluruhan adalah 522.000 [4]. Dengan demikian, data tersebut menunjukkan setiap tahunnya terjadi peningkatan kejadian kanker payudara di Indonesia. 

Oleh karena itu, dibutuhkan simpati dan empati setiap orang karena masalah ini ialah masalah yang serius yang dialami oleh seorang wanita atau ibu menyusui. Untuk itu, dibuatlah sebuah model machine learning yang bertujuan memprediksi apakah seseorang yang menderita penyakit kanker payudara dengan diagnosis kanker ganas atau jinak. Dengan adanya model machine learning ini diharapkan sebagai salah satu solusi pekerjaan dokter dalam mengindentifikasi penyakit kanker lebih awal.

## BUSSINES UNDERSTANDING

**Problem Statement**
Berdasarkan latar belakang di atas, maka dapat dirumuskan masalah yang akan diselesaikan pada proyek ini:
 - Bagaimana cara melakukan pra-pemrosesan pada data penyakit kanker payudara yang akan digunakan untuk membuat model yang baik?
 - Bagaimana cara memilih atau membuat algoritma yang mampu menghasilkan nilai akurasi diatas 90%.
 - Bagaimana cara membuat model untuk memprediksi penyakit kanker payudara jinak atau ganas pada manusia dengan menggunakan machine learning?
 
 **Goals**
 
 Berdasarkan problem statement, maka mempunyai tujuan sebagai berikut:
 - Melakukan pra-pemrosesan dengan baik agar dapat digunakan dalam
    pembuatan model. 
 - Membuat model machine learning dengan nilai akurasi
    yang mencapai 90%.
 - Mengetahui cara membuat model machine learning untuk memprediksi penyakit kanker payudara jinak atau ganas pada wanita atau ibu menyusui.

**Solusion Statement**

Berdasarkan tujuan di atas dapat dihasilkan solusi dari proyek ini antara lain:

 1.  Pra-pemrosesan data dapat dilakukan beberapa teknik, antara lain:
           - Mengatasi masalah data yang kosong dengan melakukan pengecekan terlebih dahulu lalu menggantinya dengan nilai rata-rata atau nilai median (kebetulan pada project ini tidak ditemukan data yg kosong).
           - Melakukan Encoding terhadap kolom yang bertipe *object*.
           - Melakukan  _drop_  kolom pada kolom ID.
           - Melakukan pembagian dataset menjadi dua bagian dengan rasio 80% untuk data latih dan 20% untuk data uji.
           - Melakukan  _Standard Scaler_.
           
2. Pembuatan model dipilih penggunaan model dengan algoritma Random Forest dan K-Nearest Neighbor. Algoritma itu dipilih karena mudah digunakan dan juga cocok untuk kasus ini. Berikut cara kerja kelebihan dan kekurangan algoritma Random Forest dan K-Nearest Neighbor:

   Cara kerja Algoritma Random Forest[5]:
   
        - Diawali dengan pemilihan k pada sampel dataset yang diambil secara acak dengan pengembalian
        - Menggunakan dataset untuk membangun  _decision tree_  ke-i
        - Mengulang langkah kedua langkah diatas sebanyak k.
        
     Kelebihan dan kekurangan Algoritma Random Forest[6]:
         - Kekurangan pada algoritma Random Forest yaitu interpretasi yang sulit dan membutuhkan tuning model yang tepat untuk data.
         - Kelebihannya yaitu dapat mengatasi  _noise_  dan  _missing value_  serta dapat mengatasi data dalam jumlah yang besar.
         
      Cara kerja Algoritma K-Nearest Neighbor [7]:
      
        - Menentukan jumlah tetangga terdekat K.
        - Menghitung jarak dokumen  _testing_  ke dokumen  _training_
        - Mengurutkan data berdasarkan data yang mempunyai jarak Euclidean terkecil.
        - Menentukan kelompok testing berdasarkan label pada K.
        
       Kelebihan dan kekurangan Algoritma K-Nearest Neighbor [8]: 
    
         - Kekurangan pada algoritma KKN yaitu perlu menentukan nilai dari parameter K (jumlah dari tetangga terdekat), Pembelajaran berdasarkan jarak tidak jelas mengenai jenis jarak apa yang harus digunakan dan atribut mana yang harus digunakan untuk mendapatkan hasil yang terbaik dan Biaya komputasi cukup tinggi karena diperlukan perhitungan dari jarak tiap sample uji pada keseluruhan sample latih.
         - KNN memiliki beberapa kelebihan yaitu bahwa algoritmanya tangguh terhadap  _training_  data yang  _noisy_  dan efektif apabila data latihnya besar.
         
## DATA UNDERSTANDING

![WhatsApp Image 2022-09-24 at 14 41 30](https://user-images.githubusercontent.com/111127023/192123841-bdaefced-5909-44ed-a212-7377dcd4c0ac.jpeg)


Data pada project ini menggunakan data yang bersumber pada sebuah situs kaggle, dimana fokus pada data tersebut menjelaskan faktor-faktor yang akan mempengaruhi sebuah penyakit kanker payudara bersifat ganas dan jinak. Informasi dataset dapat dilihat pada tabel dibawah ini :

| Jenis  | Keterangan |
| ----- | --- |
| Lisensi  | CC0: Public Domain  |
| Sumber | https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset  |
| Kategori  | Cancer, Women, Healthcare |
| Jenis dan Ukuran Berkas | CSV (124.57 kB) |

Pada berkas yang diunduh yakni cancer-breast.csv berisi 569 rows × 32 columns. Kolom-kolom tersebut terdiri dari 1 buah kolom bertipe objek dan 31 buah kolom bertipe numerik (tipe data float64). Dimana, penjelasan mengenai variabel-variable pada dataset cancer breast ini terdiri dari:

- **diagnosis** merupakan fitur target pada dataset ini, bertipe object yang terdiri dari (M,B). Dimana data tersebut menjelaskan diagnosis kanker bersifat Ganas (M) atau Jinak (B)  
- **radius_mean** merupakan fitur yg merepresentasikan nilai rata-rata jarak dari pusat ke titik pada keliling sekitar payudara/benjolan
- **texture_mean** merupakan fitur yg merepresentasikan standar deviasi nilai skala abu-abu atau rata-rata Tekstur Permukaan
- **perimeter_mean** merupakan rata-rata keliling.
- **id** merupakan parameter bernilai unique. Parameter ini tidak penting untuk dimasukkan kedalam model, oleh karena itu parameter ini di drop.
-   **symmetry_mean**  merupakan fitur yg merepresentasikan rata-rata Simetri
-   **fractal_dimension_mean**  merupakan fitur yg merepresentasikan rata-rata dimensi fraktal atau "_coastline approximation_  — 1"
-   **radius_se**  merupakan fitur yg merepresentasikan radius standard error
-  **area_mean**  merupakan fitur yg merepresentasikan Rata-rata Luas Lobes
-   **smoothness_mean**  merupakan fitur yg merepresentasikan Rata-rata Tingkat Kehalusan
-   **compactness_mean**  merupakan fitur yg merepresentasikan Rata-rata Kekompakan atau keliling² / luas — 1.0
-   **concavity_mean**  merupakan fitur yg merepresentasikan rata-rata kecekungan atau keparahan bagian cekung dari contour
-   **concave points_mean**  merupakan fitur yg merepresentasikan rata-rata titik cekung atau jumlah bagian cekung dari contour
-  **texture_se**  merupakan fitur yg merepresentasikan texture standard error
-   **perimeter_se**  merupakan fitur yg merepresentasikan perimeter standard error
-   **area_se**  merupakan fitur yg merepresentasikan luas standar error
-   **smoothness_se**  merupakan fitur yg merepresentasikan smoothness standard error
-   **compactness_se**  merupakan fitur yg merepresentasikan compactness standard error
-   **concavity_se**  merupakan fitur yg merepresentasikan concavity standard error
- **area_worst**  merupakan fitur yg merepresentasikan area terendah
-   **smoothness_worst**  merupakan fitur yg merepresentasikan tingkat kehalusan terendah
-   **compactness_worst**  merupakan fitur yg merepresentasikan compactness terendah
-   **concavity_worst**  merupakan fitur yg merepresentasikan kecekungan terendah
-   **concave points_worst**  merupakan fitur yg merepresentasikan titik cekung terendah
-   **symmetry_worst**  merupakan fitur yg merepresentasikan symmetry terendah
- **concave points_se**  merupakan fitur yg merepresentasikan titik cekung standard error
-   **symmetry_se**  merupakan fitur yg merepresentasikan symmetry standard error
-   **fractal_dimension_se**  merupakan fitur yg merepresentasikan fractal dimension standard error
-   **radius_worst**  merupakan fitur yg merepresentasikan radius terendah
-   **texture_worst**  merupakan fitur yg merepresentasikan texture terendah
-   **perimeter_worst**  merupakan fitur yg merepresentasikan perimeter terendah
- **fractal_dimension_worst**  merupakan fitur yg merepresentasikan fractional dimensi terendah

Berikut ini tahapan sebelum visualisasi data pada data preparation sebagai berikut:

-   Meload Dataset ke dalam sebuah Dataframe menggunakan pandas
-   `df.info()`  digunakan untuk mengecek tipe kolom pada dataset.
-   `df.isna().sum()`  digunakan untuk mengecek apakah ada kolom yang kosong, pada dataset ini nilai kosong tidak ditemukan.
-   `df.describe()`  digunakan untuk mendapatkan info mengenai dataset pada nilai rata-rata, median, banyaknya data, nilai Q1 sampai Q3 dan lain-lain.

Berikut ini tahapan visualisasi data pada data preparation:

-   Membagi dataset kedalam 2 bentuk variable, yaitu variable untuk kolom tipe numerik dan variable kolom untuk tipe object
-   Lalu, melakukan visualisasi distribusi categorial, dimana ini digunakan untuk menghitung jumlah sample Kanker Ganas atau positif (M) dan kanker Jinak atau negatif (B). pada project ini terdapat 357 jumlah data sampel kanker jinak (B) dan 212 data sample kanker ganas (M).

![download (1)](https://user-images.githubusercontent.com/111127023/192125476-80085b3d-e4c8-4616-8829-b8211e1d5c5c.png)

- Kemudian, melakukan visualisasi distribusi numerik yang dapat dilihat lebih rinci sebagai berikut:
![download (2)](https://user-images.githubusercontent.com/111127023/192125506-4eae92e0-c5b2-4009-b0eb-b2fad0b694a3.png)

- Lalu, visualisasi dilakukan untuk mengetahui korelasi antar fitur yg terdapat pada dataset sebagai berikut:
![download (3)](https://user-images.githubusercontent.com/111127023/192125529-9870c661-ed48-4a0c-8221-6919b67269ba.png)

# DATA PREPARATION
-- --
Berikut adalah tahapan-tahapan dalam melakukan pra-pemrosesan data:

- Melakukan pengecekan terhadap kolom diagnosis (fitur target) yang bertipe object. dimana kategori B merupakan sample Kanker Jinak dan M merupakan sample Kanker Ganas. fitur ini mengindintikasikan bahwa dari sample terdapat kategori kanker yang bersifat jinak dan kanker yang bersifat ganas. inilah fitur target yg ingin coba di prediksi pada project ini.

- OneHotEncoder, salah satu teknik untuk mengubah data kategorik menjadi data numerik adalah dengan menggunakan One Hot Encoding atau yang juga dikenal sebagai dummy variables. One Hot Encoding mengubah data kategorik dengan membuat kolom baru untuk setiap kategori. 

![WhatsApp Image 2022-09-25 at 09 33 12](https://user-images.githubusercontent.com/111127023/192156476-8818ed8c-db59-42b8-83f9-fa89bd0a9692.jpeg)

-  Melakukan mapping pada kolom diagnosis dari type object ke numerik agar bisa dibaca mesin. Dimana kanker jinak diubah ke nilai 0 dan kanker ganas diubah ke nilai 1.

![WhatsApp Image 2022-09-25 at 09 37 46](https://user-images.githubusercontent.com/111127023/192156531-8add6dec-79f6-43e5-8b10-a2ab74a5e775.jpeg)

- Melakukan perhitungan jumlah baris terhadap kolom target.

![WhatsApp Image 2022-09-25 at 09 40 28](https://user-images.githubusercontent.com/111127023/192156571-f69145e1-9e5f-41b8-930d-728c0568ed9f.jpeg)

- Melakukan pembagian dataset menjadi dengan 80% untuk data latih dan 20% untuk data uji Setelah melakukan pra-pemrosesan ke dataset, Data latih adalah data yang hanya digunakan untuk melatih model, sedangkan data uji adalah data yang hanya digunakan sebagai ujicoba model. Pembagian dataset ini menggunakan modul train_test_split dari scikit-learn.

Untuk menggunakannya, kita perlu mengimport Scikit-Learn terlebih dahulu, kemudian setelah itu kita dapat menggunakan fungsi train_test_split(). Setelah itu kita definisikan data yang menjadi source-nya (X)  dan juga data targetnya (y). Misalnya data source-nya adalah semua kolom kecuali kolom terakhir yang di ujung sebelah kanan dataset df, sedangkan data targetnya adalah kolom paling ujung kanan dengan nama kolom “Class”. Setelah didefinisikan, kita dapat langsung mengimplementasikan train/test split.

X_train: Untuk menampung data source yang akan dilatih.

X_test: Untuk menampung data target yang akan dilatih.

y_train: Untuk menampung data source yang akan digunakan untuk testing.

y_test: Untuk menampung data target yang akan digunakan untuk testing.

X dan y adalah nama variabel yang digunakan saat mendefinisikan data source dan data target. Parameter test_size digunakan untuk mendefinisikan ukuran data testing. Dalam contoh di atas, test_size=0.2 berarti data yang digunakan sebagai data testing adalah sebesar 20% dari keseluruhan dataset. Selanjutnya, kita dapat menggunakannya untuk pemodelan dengan algoritma tertentu misalnya disini menggunakan Linear Regression. LinearRegression() ialah fungsi untuk mengimplementasikan algoritma Linear Regression di Python. Fungsi fit() digunakan untuk melatih model, predict() digunakan untuk memprediksi hasil model. 

![WhatsApp Image 2022-09-25 at 09 41 54](https://user-images.githubusercontent.com/111127023/192156617-563173c8-39c3-49ce-87b7-988a471f4fa0.jpeg)

- Melakukan standardisasi data pada semua fitur data. Tahap terakhir yaitu melakukan standarisasi data. Hal ini dilakukan untuk membuat semua fitur berada dalam skala data yang sama yaitu dengan range 0-1. Strandadisasi data ini menggunakan fungsi StandardScaler dengan rumus:

![rumus](https://user-images.githubusercontent.com/111127023/192156722-8fee18db-d739-4a02-ab30-fa61ad93d384.png)

# MODELING
-- --

Setiap algortima ini memiliki parameter dan nilai n_neighbors, k   dst ini memiliki nilai berapa nilai dari masing-masing parameter tersebut yang digunakan di laporan ini? jelaskan paramater beserta nilainya apa saja yang digunakan setiap algortima. Nilai nya nol dan satu pada algooritma random forest dan k-nearest neighbor. Untuk parameternya tidak ada tambahan. Algoritma random forest memiliki nilai akurasi 0.973684, f1-score, recall dan precision sedikit lebih tinggi dibanding dengan algoritma K-Nearest Neighbor. Kemudian, algoritma k-nearest neighbor mempunyai nilai akurasi 0.964912.
Kemudian, setelah selesai dilakukan pra-pemrosesan pada dataset. Selanjutnya, modeling terhadap data. Pada tahap ini menggunakan 2 algoritma yaitu Random Forest dan K-Nearest Neighbor dengan tanpa parameter tambahan. Pertama-tama kedua model ini dilatih menggunakan data latih. Setelah itu kedua model akan diuji dengan data uji. Terakhir kedua model akan diukur nilai akurasinya. Perbandingan Hasil dari kedua seperti:

|   |   |  0 |   |   | 1 |  |  |
| ----- | --- | ---- | --- | ---- | ---| ---- | --- | 
|   | accuracy  | f1-score | precision | recall | f1-score | precision | recall |
|  RFC | 0.973684  | 0.977778 | 0.956522 | 1.0 | 0.967742 | 1.0	 | 0.937500 |
|  KNNT | 0.964912  | 0.970588 | 0.942857 | 1.0 | 0.956522 | 1.0 | 0.916667 |



![WhatsApp Image 2022-09-25 at 09 47 51](https://user-images.githubusercontent.com/111127023/192156817-adbd527d-9bfc-4a74-b16b-74d6dfe0571d.jpeg)

Pada model dengan algoritma Random Forest memiliki nilai akurasi, f1-score, recall dan precision sedikit lebih tinggi dibanding dengan algoritma K-Nearest Neighbor. Untuk membuktikannya, kedua model tersebut diuji pada data uji dan di visualisasikan pada confussion matrix seperti:

- Confussion Matrix Algoritma Random Forest
 Algoritma dibawah menjelaskan bahwa bagian atas kiri merepresentasikan TN (True negatif) yaitu data negatif yg diprediksi benar, dan bagian bawah kanan merupakan data positif yg di prediksi benar, selain itu merupakan data false negatif (atas kanan) dan false positif (bawah kiri), dimana hasil itu merupakan data negatif namun diprediksi positif maupun sebaliknya.

![WhatsApp Image 2022-09-25 at 09 48 35](https://user-images.githubusercontent.com/111127023/192156846-aeac6e26-d055-45a7-9788-508b137e413d.jpeg)

- Confussion Matrix Algoritma K-Nearest Neighbor
 Pada algoritma K-NN tidak jauh berbeda dengan algoritma random forest dimana bagian atas kiri merepresentasikan TN (True Negatif) yaitu data negatif yg diprediksi benar, dan bagian bawah kanan merupakan data positif yg di prediksi benar, selain itu merupakan data false negatif (atas kanan) dan false positif (bawah kiri), dimana hasil itu merupakan data negatif namun diprediksi positif maupun sebaliknya.
 
Dengan hasil diatas dimana algoritma random forest menghasilkan nilai akurasi yg sedikit lebih tinggi, maka model dengan algoritma Random Forest merupakan model yang dipilih untuk digunakan pada project ini.

![WhatsApp Image 2022-09-25 at 09 49 16](https://user-images.githubusercontent.com/111127023/192156851-c1bc4c1c-c4ad-4b6a-81d4-bdf4c70bec6f.jpeg)

# EVALUATION
-- --
Pada proyek ini, model yang dikembangkan adalah kasus klasifikasi dan menggunakan metriks akurasi, f1-score, recall dan precision. Berikut hasil pengukuran model yang dipilih yaitu model yang menggunakan algoritma Random Forest metriks akurasi, f1-score, recall dan precision.

|   |  precision | recall | f1-score  | support | 
| ----- | --- | ---- | --- | ---- | 
|  0 | 0.942857  | 1.000000 | 0.970588 | 66.000000 | 
|  1 | 1.000000  | 0.916667 | 0.956522 | 48.000000 |
| accuracy  | 0.964912 |  0.964912 |  0.964912 | 0.964912 | 
|  macro avg | 0.971429 | 0.958333 | 0.963555 | 114.000000 |
| weighted avg  | 0.966917 | 0.964912 | 0.964666 | 114.000000 |


![WhatsApp Image 2022-09-25 at 09 50 45](https://user-images.githubusercontent.com/111127023/192157025-326eb93c-9f99-4535-95a6-6379dd5614fb.jpeg)

Akurasi, ialah metrik untuk menghitung persentase dari total data yang diidentifikasi dan dinilai benar dengan rumus:

![rumus1](https://user-images.githubusercontent.com/111127023/192157163-b38d0145-902b-4d8f-a53a-f4f7431dc4e9.png)

- True Positive (TP): Kasus dimana model merupakan data positif yang diprediksi benar. Contohnya, pasien menderita kanker (class 1) dan dari model yang dibuat memprediksi pasien tersebut menderita kanker (class 1).
- True Negative (TN): Kasus dimana model merupakan data negatif yang diprediksi benar. Contohnya, pasien tidak menderita kanker (class 2) dan dari model yang dibuat memprediksi pasien tersebut tidak menderita kanker (class 2).
- False Positive (FP) - Type I Error : Kasus dimana model merupakan data negatif namun diprediksi sebagai data positif. Contohnya, pasien tidak menderita kanker (class 2) tetapi dari model yang telah memprediksi pasien tersebut menderita kanker (class 1).
- False Negative (FN) - Type II Error : Kasus dimana model merupakan data negatif namun diprediksi sebagai data positif. Contohnya, pasien tidak menderita kanker (class 2) tetapi dari model yang telah memprediksi pasien tersebut menderita kanker (class 1).

- Precision, merupakan metrik untuk memprediksi benar positif dari keseluruhan hasil yang diprediksi positf. Rumus precision seperti:

Precission = (TP) / (TP + FP)

- Recall, merupakan metrik untuk memprediksi benar positif dibandingkan dengan keseluruhan data yang benar positif. Rumus precision:

Recall = (TP) / (TP + FN)

- f1-score f1-score merupakan metrik untuk perbandingan rata-rata precision dan recall yang dibobotkan. Rumus f1-score

F1 Score = 2 * (Recall*Precission) / (Recall+Precission)

# REFERENSI
-- --

[1] Prahartiwi, L. I., & Dari, W. (2021). Komparasi Algoritma Naive Bayes, Decision Tree dan Support Vector Machine untuk Prediksi Penyakit Kanker Payudara, 51.https://ejournal.bsi.ac.id/ejurnal/index.php/jtk/article/view/9191/pdf.

[2,3] Wibisono, G., & Hermawan, A. (2019). Faktor-Faktor Penentu Gejala Penyakit Kanker Payudara Dengan Pendekatan Jaringan Saraf Tiruan. JASIEK (Jurnal Aplikasi Sains, Informasi, Elektronika dan Komputer), 1(1), 2.https://www.jurnal.unmer.ac.id/index.php/jasiek/article/view/3098.

[4] Maziida, S. R. (2018). KLASIFIKASI PENYAKIT DIABETES MELLITUS DENGAN MENGGUNAKAN PERBANDINGAN ALGORITMA J48 DAN RANDOM FOREST (STUDI KASUS: RUMAH SAKIT MUHAMMADIYAH LAMONGAN) (Doctoral dissertation, University of Muhammadiyah Malang). https://eprints.umm.ac.id/39299/.

[5] Haristu, R. A., & Rosa, P. H. P. (2019). Penerapan Metode Random Forest Untuk Prediksi Win Ratio Pemain Player Unknown Battleground. MEANS (Media Informasi Analisa dan Sistem), 120-128. https://repository.usd.ac.id/35513/.

[6] Maziida, S. R. (2018). KLASIFIKASI PENYAKIT DIABETES MELLITUS DENGAN MENGGUNAKAN PERBANDINGAN ALGORITMA J48 DAN RANDOM FOREST (STUDI KASUS: RUMAH SAKIT MUHAMMADIYAH LAMONGAN) (Doctoral dissertation, University of Muhammadiyah Malang). https://eprints.umm.ac.id/39299/.

[7] Sani, R. R., Zeniarja, J., & Luthfiarta, A. (2016). Penerapan algoritma K-Nearest Neighbor pada information retrieval dalam penentuan topik referensi tugas akhir. Journal of Applied Intelligent System, 1(2), 123-133. https://publikasi.dinus.ac.id/index.php/jais/article/view/1189/.

[8] Penyelenggara PS. Teknik Informa ka, Jurusan Ilmu Komputer FMIPA - Universitas Udayana Kampus Bukit Jimbaran. PROSIDING ISSN : X SEMINAR NASIONAL TEKNOLOGI INFORMASI & APLIKASINYA 2015 INOVASI TEKNOLOGI INFORMASI DAN KOMUNIKASI DALAM MENUNJANG TECHNOPRENEURSHIP. Universitas Udayana (2015). https://simdos.unud.ac.id/uploads/file_penelitian_1_dir/721bdb509a6f0bb9ccca6d7374b86759.pdf.

--- **Ini adalah bagian akhir laporan** ---

