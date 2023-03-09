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
