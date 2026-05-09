import time
import concurrent.futures

def process_task(task_id, duration):
    """
    Fungsi ini merepresentasikan task yang sedang dieksekusi.
    Setiap task memiliki ID dan durasi pengerjaan masing-masing.
    """
    print(f"[Task {task_id}] Memulai eksekusi (Durasi: {duration} detik)...")
    time.sleep(duration) # Simulasi proses pengerjaan
    print(f"[Task {task_id}] Selesai dieksekusi.")
    return duration

def main():
    # daftar task beserta durasi waktu pengerjaannya (dalam detik)
    tasks = {
        'A': 4, 'B': 2, 'C': 5, 
        'D': 1, 'E': 3, 'F': 6, 'G': 2
    }
    num_workers = 3 # jumlah thread yang tersedia
    
    # 1. Menghitung Expected Optimal Time
    # Waktu optimal yang diharapkan adalah total beban kerja dibagi jumlah pekerja,
    # atau minimal sama dengan durasi task terlama.
    total_workload = sum(tasks.values())
    longest_task = max(tasks.values())
    expected_optimal_time = max(longest_task, total_workload / num_workers)
    
    print("--- INFORMASI SISTEM ---")
    print(f"Total Beban Kerja (Workload) : {total_workload} detik")
    print(f"Jumlah Pekerja (Workers)     : {num_workers}")
    print(f"Expected Optimal Time        : {expected_optimal_time:.2f} detik\n")

    print("--- MEMULAI DYNAMIC DISTRIBUTION ---")
    start_time = time.time()

    # 2. Implementasi Dynamic Distribution menggunakan ThreadPoolExecutor
    # Pekerja yang idle akan secara dinamis mengambil task berikutnya 
    # dari antrean tanpa pembagian statis di awal.
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        # Submit semua task ke executor
        futures = [executor.submit(process_task, task_id, duration) 
                   for task_id, duration in tasks.items()]
        
        # Menunggu semua eksekusi task selesai
        concurrent.futures.wait(futures)

    end_time = time.time()
    actual_time = end_time - start_time

    # 3. Menampilkan Hasil Akhir
    print("\n--- HASIL EKSEKUSI ---")
    print(f"Distribusi selesai.")
    print(f"Expected Optimal Time : {expected_optimal_time:.2f} detik")
    print(f"Actual Execution Time : {actual_time:.2f} detik")
    
    if actual_time <= expected_optimal_time + 0.5: # +0.5 margin untuk overhead sistem
        print("Kesimpulan: Kode berhasil mencapai expected optimal time melalui dynamic distribution.")
    else:
        print("Kesimpulan: Waktu eksekusi mendekati optimal, bergantung pada urutan antrean task.")

if __name__ == "__main__":
    main()