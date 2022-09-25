# Predictive-Analystics
# LAPORAN PROYEK PREDICTIVE ANALYTICS - PUTRI WULANDARI

**Domain Proyek** 

	 Domain proyek yang saya pilih ialah tema kesehatan dengan judul proyek "Prediksi Penyakit Kanker Payudara pada Manusia atau Wanita".
**Latar Belakang**

Kanker payudara merupakan kanker paling umum pada wanita di seluruh dunia dengan menyumbang 25,4% dari total jumlah kasus baru yang didiagnosis pada tahun 2018. Kanker adalah sekelompok besar penyakit yang dapat dimulai di hampir semua organ atau jaringan tubuh ketika sel abnormal tumbuh tak terkendali, melampaui batas biasanya untuk menyerang bagian tubuh yang berdekatan dan atau menyebar ke organ lain. Merujuk data yang dipaparkan Kemenkes per 31 Januari 2019, terdapat angka kanker payudara 42,1 per 100.000 penduduk dengan rata-rata kematian 17 per 100.000 penduduk[3]. Penyakit ini merupakan salah satu penyakit yang menjadi momok bagi kaum wanita walaupun tidak menutup kemungkinan pria juga bisa terkena penyakit ini. Dimana, menjadi momok bagi kaum wanita karena penyakit ini menyerang bagian tubuh yang menjadi salah satu ciri khas kaum wanita. Kanker payudara merupakan penyakit yang tidak menular yang cenderung terus meningkat setiap tahunnya, sehingga dapat dikatakan bahwa beban yang harus ditanggung dunia akibat penyakit tersebut semakin meningkat[4]. Mulai dari tahun 2008 terdapat 12,7 juta kasus kanker di dunia dan terus menerus mengalami peningkatan hingga tahun 2018 menjadi 18,1 juta kasus kanker. Kematian yang disebabkan oleh kanker juga mengalami peningkatan dari 7,6 juta pada tahun 2008 menjadi 9,6 juta pada tahun 2018. IARC menyatakan bahwa terjadi peningkatan kasus kanker payudara yang menyerang wanita dengan tingkat kematian sebesar 627.000 di seluruh dunia. Berdasarkan data dari Riset Kesehatan Dasar (RISKESDAS) tahun 2018 jumlah kejadian kanker payudara yang menyerang wanita adalah sebesar 42,1 per 100.000 penduduk dengan rata-rata kematian 17 per 100.000 penduduk dan data pada tahun 2012 sebesar 12,1 per 100.000 penduduk dengan jumlah kematian secara keseluruhan adalah 522.000[5]. 
Dengan demikian, data tersebut menunjukkan setiap tahunnya terjadi peningkatan kejadian kanker payudara di Indonesia. Oleh karena itu, dibutuhkan simpati dan empati setiap orang karena masalah ini ialah masalah yang serius yang dialami oleh seorang wanita atau ibu menyusui. Untuk itu, dibuatlah sebuah model machine learning yang bertujuan memprediksi apakah seseorang yang menderita penyakit kanker payudara dengan diagnosis kanker ganas atau jinak. Dengan adanya model machine learning ini diharapkan sebagai salah satu solusi pekerjaan dokter dalam mengindentifikasi penyakit kanker lebih awal.

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

   Cara kerja Algoritma Random Forest
   
        - Diawali dengan pemilihan k pada sampel dataset yang diambil secara acak dengan pengembalian
        - Menggunakan dataset untuk membangun  _decision tree_  ke-i
        - Mengulang langkah kedua langkah diatas sebanyak k.
        
     Kelebihan dan kekurangan Algoritma Random Forest:
         - Kekurangan pada algoritma Random Forest yaitu interpretasi yang sulit dan membutuhkan tuning model yang tepat untuk data.
         - Kelebihannya yaitu dapat mengatasi  _noise_  dan  _missing value_  serta dapat mengatasi data dalam jumlah yang besar.
         
      Cara kerja Algoritma K-Nearest Neighbor:
      
        - Menentukan jumlah tetangga terdekat K.
        - Menghitung jarak dokumen  _testing_  ke dokumen  _training_
        - Mengurutkan data berdasarkan data yang mempunyai jarak Euclidean terkecil.
        - Menentukan kelompok testing berdasarkan label pada K.
        
       Kelebihan dan kekurangan Algoritma K-Nearest Neighbor:
    
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
- 
