from abc import ABC, abstractmethod

# Abstract Class
class LibraryItem(ABC):
    def __init__(self, id_buku, judul, tahun, penulis):
        self._id_buku = id_buku
        self._judul = judul
        self._tahun = tahun
        self._penulis = penulis

    @abstractmethod
    def info(self):
        pass

    @property
    def judul(self):
        return self._judul

    def get_id(self):
        return self._id_buku


class Book(LibraryItem):
    def __init__(self, id_buku, judul, tahun, penulis, genre):
        super().__init__(id_buku, judul, tahun, penulis)
        self._genre = genre

    def info(self):
        return f"[BUKU] {self._judul} oleh {self._penulis} ({self._tahun}) - Genre: {self._genre}"


class Magazine(LibraryItem):
    def __init__(self, id_buku, judul, tahun, penulis, edisi):
        super().__init__(id_buku, judul, tahun, penulis)
        self._edisi = edisi

    def info(self):
        return f"[MAJALAH] {self._judul} oleh {self._penulis} ({self._tahun}) - Edisi: {self._edisi}"


class Library:
    def __init__(self):
        self.__items = []

    def tambah_item(self, item: LibraryItem):
        self.__items.append(item)

    def tampilkan_semua_item(self):
        print("\n📚 Daftar Koleksi:")
        for item in self.__items:
            print(item.info())

    def cari_item(self, keyword):
        print(f"\n🔍 Hasil pencarian untuk '{keyword}':")
        ditemukan = False
        for item in self.__items:
            if keyword.lower() in item.judul.lower() or keyword == item.get_id():
                print(item.info())
                ditemukan = True
        if not ditemukan:
            print("Item tidak ditemukan.")

    def input_item_baru(self):
        print("\n➕ Tambah Item Baru")
        jenis = input("Jenis item (buku/majalah): ").strip().lower()
        id_buku = input("ID Buku: ")
        judul = input("Judul: ")
        tahun = int(input("Tahun: "))
        penulis = input("Penulis: ")

        if jenis == "buku":
            genre = input("Genre: ")
            item = Book(id_buku, judul, tahun, penulis, genre)
        elif jenis == "majalah":
            edisi = input("Edisi: ")
            item = Magazine(id_buku, judul, tahun, penulis, edisi)
        else:
            print("Jenis item tidak dikenal!")
            return

        self.tambah_item(item)
        print("✅ Item berhasil ditambahkan!")


# Main Program
if __name__ == "__main__":
    perpustakaan = Library()

    while True:
        print("\n=== Sistem Manajemen Perpustakaan ===")
        print("1. Tambah item")
        print("2. Tampilkan semua item")
        print("3. Cari item")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            perpustakaan.input_item_baru()
        elif pilihan == "2":
            perpustakaan.tampilkan_semua_item()
        elif pilihan == "3":
            keyword = input("Masukkan judul atau ID: ")
            perpustakaan.cari_item(keyword)
        elif pilihan == "4":
            print("👋 Keluar dari program. Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")
