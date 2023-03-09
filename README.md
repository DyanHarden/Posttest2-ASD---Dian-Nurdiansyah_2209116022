# Dokumentasi Algoritma dan Struktur Data (Posttest2)
Nama: Muhammad Dian Nurdiansyah

Nim: 2209116022

# Fibonnacci Search
Program fibonacci search merupakan implementasi dari algoritma Fibonacci Search yang digunakan untuk mencari indeks suatu elemen pada array. Pada program ini, algoritma Fibonacci Search digunakan untuk mencari indeks dari sebuah elemen pada sebuah list.

# Cara Kerja Program
1. Pertama-tama, program akan melakukan inisialisasi angka fibonacci pertama dan kedua. 
2. Kemudian, program akan menghitung nilai angka fibonacci selanjutnya dengan cara menjumlahkan angka fibonacci pertama dan kedua. 
3. Program akan terus menghitung nilai angka fibonacci selanjutnya sampai nilai angka fibonacci terakhir lebih besar atau sama dengan panjang list. 
4. Selanjutnya, program akan melakukan loop sampai angka fibonacci pertama sama dengan 0. 
5. Pada setiap iterasi loop, program akan mengambil indeks dari list yang akan dicek. Indeks ini dihitung dengan cara mengambil nilai minimum dari offset ditambah angka fibonacci kedua dan panjang list dikurangi 1. 
6. Program akan membandingkan nilai elemen pada indeks yang telah diambil dengan nilai yang dicari. Jika nilai elemen pada indeks tersebut lebih kecil dari nilai yang dicari, maka program akan menggeser jarak pencarian ke depan sebesar angka fibonacci kedua. 
7. Jika nilai elemen pada indeks tersebut lebih besar dari nilai yang dicari, maka program akan menggeser jarak pencarian ke depan sebesar angka fibonacci pertama. 
8. Jika nilai elemen pada indeks tersebut sama dengan nilai yang dicari, maka program akan mengembalikan indeks dari elemen tersebut. 
9. Jika nilai yang dicari tidak ditemukan pada list, maka program akan mengembalikan nilai -1.

# Fungsionalitas Program
Program ini dapat mencari indeks suatu elemen pada list. Program juga dapat mencari elemen pada indeks yang berada di dalam list yang lain.

#Elemen yang Digunakan dalam Program 
1. Fungsi fibonacci_search: Ini adalah fungsi yang digunakan untuk mencari nilai x pada array arr. Fungsi ini menggunakan algoritma pencarian Fibonacci.
2. Array (list): my_list adalah array (list) yang diberikan dan berisi beberapa nilai.
3. Variabel x: Variabel ini berisi nilai yang akan dicari di dalam array.
4. Variabel n: Variabel ini digunakan untuk menyimpan panjang array.
5. Variabel fib, fib1, fib2: Variabel ini digunakan untuk menyimpan nilai dari bilangan Fibonacci yang dihasilkan dalam pencarian.
6. Variabel offset: Variabel ini digunakan untuk menyimpan indeks awal pencarian.
7. While loops: Digunakan untuk melakukan perulangan pada saat pencarian.
8. If statements: Digunakan untuk melakukan pengecekan apakah nilai yang dicari lebih besar, lebih kecil atau sama dengan nilai pada indeks array tertentu.
9. Return statements: Digunakan untuk mengembalikan nilai indeks saat data yang dicari ditemukan, dan mengembalikan -1 saat data tidak ditemukan.

# Penjelasan dari Tiap Baris Source Code
![Screenshot 2023-03-09 165828](https://user-images.githubusercontent.com/94899238/223971582-b6d3a0ff-08f8-47b2-b74a-8dd8aaf007a3.png)
1. Menginisialisasi angka fibonacci pertama dan kedua

![Screenshot 2023-03-09 171856](https://user-images.githubusercontent.com/94899238/223976740-73b4ac1c-4a06-4964-89ee-291dbe03bd58.png)

2. Menghitung panjang array yang akan dicari.

![Screenshot 2023-03-09 172119](https://user-images.githubusercontent.com/94899238/223977327-af91b66c-ec4f-4ff7-a0b2-bc889d87501b.png)

3. Loop sampai angka fibonacci terakhir lebih besar atau sama dengan panjang array. Setiap kali loop berjalan, nilai angka fibonacci terakhir dihitung sebagai penjumlahan dua angka fibonacci sebelumnya.

![Screenshot 2023-03-09 172455](https://user-images.githubusercontent.com/94899238/223978190-d3faed81-90e9-469c-b52a-2750a685132a.png)

4. Loop while pertama untuk mencari angka fibonacci terbesar yang kurang dari atau sama dengan panjang array. Variabel fib2, fib1, dan fib adalah angka fibonacci yang digunakan dalam loop. Loop terus berjalan hingga angka fibonacci terakhir lebih besar atau sama dengan panjang array.

![Screenshot 2023-03-09 175213](https://user-images.githubusercontent.com/94899238/223985331-4dd9b36f-5610-469d-bda7-fcef92282f3a.png)

Jika data yang dicari lebih besar dari isi array pada indeks ke-i, maka jarak pencarian di depan menjadi lebih jauh sebesar angka fibonacci kedua. Nilai angka fibonacci pertama dihitung sebagai selisih antara angka fibonacci terakhir dan angka fibonacci kedua. Nilai offset diupdate menjadi i.

![Screenshot 2023-03-09 201502](https://user-images.githubusercontent.com/94899238/224020319-20a726dc-5777-46a8-8f87-f6e9f32d4fd0.png)

Setelah loop while kedua selesai, dilakukan pengecekan apakah data yang dicari ada pada indeks offset+1, dan apakah angka fibonacci pertama masih lebih besar dari 0. Jika ya, maka data tersebut ditemukan pada indeks offset+1 dan indeks tersebut dikembalikan sebagai hasil pencarian.
 
![Screenshot 2023-03-09 201550](https://user-images.githubusercontent.com/94899238/224020724-482a91c4-ac09-4ae7-95da-b910c33f0064.png)

Jika data yang dicari tidak ditemukan dalam array, maka -1 dikembalikan sebagai hasil pencarian.

![Screenshot 2023-03-09 201817](https://user-images.githubusercontent.com/94899238/224020986-cf41f39b-9113-48c8-91c6-5bc39209b201.png)

Jika data yang dicari tidak ditemukan di dalam array, maka fungsi mengembalikan nilai -1.

![Screenshot 2023-03-09 202013](https://user-images.githubusercontent.com/94899238/224021425-f312f5b0-7a65-446b-ac2c-c289f5990f5d.png)

Mendefinisikan list yang akan dicari.

![Screenshot 2023-03-09 202024](https://user-images.githubusercontent.com/94899238/224021591-2a899243-7d8d-4948-a399-b610278e3929.png)

Mencari indeks dari elemen-elemen pada list dalam list yang telah didefinisikan menggunakan fungsi fibonacci_search.
