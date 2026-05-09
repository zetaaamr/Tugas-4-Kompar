# Tugas 4 – Komputasi Paralel & Sistem Terdistribusi

Tugas ini dibuat untuk memenuhi Tugas 4 mata kuliah Komputasi Paralel & Sistem Terdistribusi (IFB 206). Fokus tugas ini adalah implementasi distribusi beban kerja secara dinamis (Load Balancing).

## Identitas Mahasiswa
Nama  : Zeta Mardhotillah Ronny  
NRP   : 15-2024-047  
Kelas : CC – Komputasi Paralel & Sistem Terdistribusi  

## Deskripsi Tugas
Repository ini berisi implementasi konsep **Dynamic Distribution** (Distribusi Dinamis) yang dikerjakan berdasarkan ketentuan digit terakhir NRP (Ganjil). 

Fitur utama dalam kode ini:
- **Dynamic Load Balancing**: Menggunakan `ThreadPoolExecutor` untuk mendistribusikan tugas secara otomatis kepada pekerja (*worker*) yang sedang menganggur (*idle*).
- **Optimization Analysis**: Menampilkan perbandingan antara *Expected Optimal Time* (waktu optimal teoritis) dengan *Actual Execution Time* (waktu eksekusi nyata).
- **Task Simulation**: Simulasi pengerjaan berbagai tugas dengan durasi yang bervariasi untuk menunjukkan efisiensi distribusi dinamis.
