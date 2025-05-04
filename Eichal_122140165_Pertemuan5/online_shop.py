from abc import ABC, abstractmethod

# Abstract Class: LibraryItem, menjadi dasar bagi semua item di perpustakaan
class LibraryItem(ABC):
    def __init__(self, id_buku, judul, tahun, penulis):
        # Atribut untuk menyimpan informasi dasar
        self._id_buku = id_buku
        self._judul = judul
        self._tahun = tahun
        self._penulis = penulis
    
    # Method abstract yang harus diimplementasikan oleh subclass
    @abstractmethod
    def info(self):
        pass
    
    # Property untuk mengakses judul tanpa menggunakan getter secara eksplisit
    @property
    def judul(self):
        return self._judul

    # Getter untuk mengambil ID buku
    def get_id(self):
        return self._id_buku


# Subclass Book yang mewarisi dari LibraryItem
class Book(LibraryItem):
    # Konstruktor untuk buku, menambahkan atribut genre
    def __init__(self, id_buku, judul, tahun, penulis, genre):
        super().__init__(id_buku, judul, tahun, penulis)
        self._genre = genre

    # Implementasi dari method info untuk buku
    def info(self):
        # Menampilkan informasi buku dengan format tertentu
        return f"[BUKU] {self._judul} oleh {self._penulis} ({self._tahun}) - Genre: {self._genre}"


# Subclass Magazine yang mewarisi dari LibraryItem
class Magazine(LibraryItem):
    # Konstruktor untuk majalah, menambahkan atribut edisi
    def __init__(self, id_buku, judul, tahun, penulis, edisi):
        super().__init__(id_buku, judul, tahun, penulis)
        self._edisi = edisi

    # Implementasi dari method info untuk majalah
    def info(self):
        # Menampilkan informasi majalah dengan format tertentu
        return f"[MAJALAH] {self._judul} oleh {self._penulis} ({self._tahun}) - Edisi: {self._edisi}"


# Kelas Library untuk mengelola koleksi item perpustakaan
class Library:
    def __init__(self):
        # Menggunakan atribut private __items untuk menyimpan koleksi item
        self.__items = []

    # Method untuk menambah item ke dalam koleksi perpustakaan
    def tambah_item(self, item: LibraryItem):
        self.__items.append(item)

    # Method untuk menampilkan semua item yang ada di perpustakaan
    def tampilkan_semua_item(self):
        print("\n📚 Daftar Koleksi:")
        for item in self.__items:
            print(item.info())  # Memanggil method info() dari setiap item

    # Method untuk mencari item berdasarkan judul atau ID
    def cari_item(self, keyword):
        print(f"\n🔍 Hasil pencarian untuk '{keyword}':")
        ditemukan = False
        for item in self.__items:
            # Mencari dengan cara membandingkan keyword dengan judul atau ID
            if keyword.lower() in item.judul.lower() or keyword == item.get_id():
                print(item.info())  # Menampilkan info item yang cocok
                ditemukan = True
        if not ditemukan:
            print("Item tidak ditemukan.")  # Jika tidak ditemukan

    # Method untuk input item baru dari pengguna
    def input_item_baru(self):
        print("\n➕ Tambah Item Baru")
        # Meminta input dari pengguna untuk menentukan jenis item
        jenis = input("Jenis item (buku/majalah): ").strip().lower()
        id_buku = input("ID Buku: ")
        judul = input("Judul: ")
        tahun = int(input("Tahun: "))
        penulis = input("Penulis: ")

        # Menambahkan item berdasarkan jenis (buku atau majalah)
        if jenis == "buku":
            genre = input("Genre: ")
            item = Book(id_buku, judul, tahun, penulis, genre)
        elif jenis == "majalah":
            edisi = input("Edisi: ")
            item = Magazine(id_buku, judul, tahun, penulis, edisi)
        else:
            print("Jenis item tidak dikenal!")
            return

        # Menambah item baru ke dalam koleksi perpustakaan
        self.tambah_item(item)
        print("✅ Item berhasil ditambahkan!")


# Main Program: Menjalankan antarmuka pengguna
if __name__ == "__main__":
    perpustakaan = Library()  # Membuat objek perpustakaan

    # Program utama berjalan dalam loop sampai pengguna memilih keluar
    while True:
        print("\n=== Sistem Manajemen Perpustakaan ===")
        print("1. Tambah item")  # Opsi untuk menambah item
        print("2. Tampilkan semua item")  # Opsi untuk menampilkan daftar item
        print("3. Cari item")  # Opsi untuk mencari item
        print("4. Keluar")  # Opsi untuk keluar dari program

        # Meminta input pilihan dari pengguna
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            perpustakaan.input_item_baru()  # Memanggil fungsi tambah item
        elif pilihan == "2":
            perpustakaan.tampilkan_semua_item()  # Memanggil fungsi tampilkan item
        elif pilihan == "3":
            keyword = input("Masukkan judul atau ID: ")
            perpustakaan.cari_item(keyword)  # Memanggil fungsi cari item
        elif pilihan == "4":
            print("👋 Keluar dari program. Sampai jumpa!")
            break  # Keluar dari program
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")  # Menangani input yang salah
