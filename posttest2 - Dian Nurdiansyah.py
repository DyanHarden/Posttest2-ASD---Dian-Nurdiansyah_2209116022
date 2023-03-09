def fibonacci_search(arr, x):
    # Inisialisasi angka fibonacci pertama dan kedua
    fib2 = 0
    fib1 = 1
    fib = fib2 + fib1
 
    n = len(arr)
 
    # Loop sampai angka fibonacci terakhir lebih besar atau sama dengan panjang array
    while (fib < n):
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
 
    # Indeks awal
    offset = -1
 
    # Loop sampai angka fibonacci pertama sama dengan 0
    while (fib > 1):
        # Indeks dari array yang akan dicek
        i = min(offset+fib2, n-1)
 
        # Jika data yang dicari lebih besar dari isi array pada indeks ke-i,
        # maka jarak pencarian di depan menjadi lebih jauh sebesar angka fibonacci kedua
        if (arr[i] < x):
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
 
        # Jika data yang dicari lebih kecil dari isi array pada indeks ke-i,
        # maka jarak pencarian di depan menjadi lebih jauh sebesar angka fibonacci pertama
        elif (arr[i] > x):
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
 
        # Jika data yang dicari sama dengan isi array pada indeks ke-i,
        # maka data tersebut ditemukan
        else:
            return i
 
    # Jika data yang dicari tidak ditemukan
    if(fib1 and arr[offset+1] == x):
        return offset+1
 
    # Jika data yang dicari tidak ada di dalam array
    return -1

# List yang diberikan
my_list = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# 1. Mencari data pada indeks tertentu
print("1. Data pada indeks:")
print("Arsel di index", fibonacci_search(my_list, "Arsel"))
print("Avivah di index", fibonacci_search(my_list, "Avivah"))
print("Daiva di index", fibonacci_search(my_list, "Daiva"))
print("="*50)
print()

# 2. Mencari data pada indeks di dalam list dalam list
print("2. Data pada indeks [3][0]:")
print("Wahyu di index", fibonacci_search(my_list[3], "Wahyu"))
print("="*50)
print()

# 3. Mencari data pada indeks di dalam list dalam list
print("3. Data pada indeks [3][1]:")
print("Wibi di index", fibonacci_search(my_list[3], "Wibi"))
print("="*50)
print()