Tugas 2 Praktikum PEMWEB RB 
Personal Dashboard

Personal Dashboard adalah aplikasi web sederhana berbasis HTML, CSS, dan JavaScript (ES6+) yang membantu pengguna mengatur aktivitas harian mereka, seperti mencatat memo, jadwal kuliah, tugas, dan daftar to-do secara terstruktur dan tersimpan secara lokal di browser.

---

Fitur Utama

- Memo (Catatan Singkat)  
  Tambahkan dan hapus memo dengan tampilan grid yang rapi.

- Jadwal Kuliah  
  Simpan jadwal kuliah dengan tampilan daftar.

- Daftar Tugas & To-Do List  
  Tambah, edit, dan hapus tugas atau to-do list harian.

- Penyimpanan Otomatis  
  Semua data tersimpan di `localStorage`, jadi tidak akan hilang meskipun halaman direfresh.

---

 Screenshot Aplikasi

> Berikut tampilan aplikasi ketika berjalan:

![image](https://github.com/user-attachments/assets/6ec3c3fc-4112-4382-848a-0e069b1d5542)

---

Fitur Modern (ES6+) yang Digunakan

- Class-based OOP  
  Menggunakan class `ListManager` dan `NoteApp` untuk modularitas.
-  Arrow Function  
  Menghindari penggunaan `function` klasik, semua fungsi ditulis dengan arrow function (`=>`).
-  Destructuring & Template Literals  
  Penggunaan backticks dan `${}` untuk string dinamis pada HTML injection.
-  Local Storage API  
  Menggunakan `localStorage` untuk persistensi data tanpa backend.
-  Modularisasi dan DRY Code  
  Pemanfaatan class untuk menghindari pengulangan kode dalam pembuatan daftar (task, schedule, etc.).
