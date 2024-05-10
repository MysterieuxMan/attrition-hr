# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

### Permasalahan Bisnis
Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut.

### Cakupan Proyek
Dalam proyek ini, cakupan proyeknya adalah sebagai berikut:

1. Mengidentifikasi faktor-faktor yang mempengaruhi attrition rate karyawan.
2. Membuat business dashboard untuk membantu memonitori faktor-faktor tersebut.
3. Membuat prototype sistem machine learning untuk memprediksi attrition karyawan.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:
```
!pip install pandas numpy matplotlib seaborn scikit-learn imblearn category_encoder
```

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

Pada dashboard yang telah dibuat terdapat beberapa filter search untuk memmpermudah menampilkan data mana saja yang ditampilkan. Pada dashboard juga hanya menampilkan data-data yang berhubungan dengan attrition rate saja

Link Dashboard: 
https://lookerstudio.google.com/reporting/a3441456-8fda-46c7-8566-948fd684e614

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```
Prototype dapat digunakan dengan cara mengatur berbagai macam attributes yang dapat digunakan untuk menentukan apakah karyawan dari perusahaan tersebut akan keluar atau tidak berdasarkan variabel yang telah diatur. Hasilnya nanti akan terdapat 3 kondisi, yaitu:
1. Weak: Karyawan kemungkinan kecil akan keluar
2. Medium: Karyawan kemungkinan akan keluar
3. Strong: Karyawan Kemungkinan besar akan keluar

Link Prototype:
https://attrition-hr-ilham.streamlit.app/
```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

Berdasarkan analisis, tingkat keluar masuk (attrition rate) karyawan adalah 16,9%, dan karyawan laki-laki memiliki tingkat keluar masuk yang lebih tinggi dibandingkan karyawan perempuan. Pada tahun-tahun awal bekerja di perusahaan, tingkat keluar masuk lebih tinggi. Puncak dari total keluarnya karyawan adalah pada thun pertamanya bekerja. Namun dengan seiring bertambahnya tahun, tingkat keluar karyawan menurun. Karyawan yang memiliki Job Satisfaction rendah dan environtment satisfaction rendah memiliki tingkat keluar masuk tertinggi. Karyawan yang sering bepergian memiliki tingkat keluar masuk tertinggi. Jabatan karyawan dengan tingkat keluar masuk tertinggi adalah Sales Representative dan Laboratory Technician.
### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Overtime. Perusahaan harus membatasi jam kerja lembur untuk para karyawan. Apabila karyawan harus terpaksa lembur, maka perusahaan harus memberikan kompensasi yang sesuai.
- Stock Option Level. Perlu mempertimbangkan tingkat stock option terhadapt karyawan dengan jabatan yang berbeda.
- Job Role. Sebanyak 75% karyawan dengan jabatan sales representative keluar. Perusahaan perlu mengevaluasi jabatan tersebut agar mengurangi hal ini. Evaluasi dapat dilakukan dengan cara seperti, analisis beban kerja dan kompensansi dan tunjangan apakah sudah sesuai atau belum. 
"# attrition-hr" 
