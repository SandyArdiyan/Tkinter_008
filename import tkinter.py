import tkinter as tk
from tkinter import messagebox

# Fungsi untuk hasil prediksi
def hasil_prediksi():
    try:
        # Memeriksa setiap nilai input
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100")
        
        # Menampilkan hasil prediksi
        hasil_label.config(text="Prediksi prodi: Teknologi Informasi")
    
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")  # Ukuran window
root.configure(bg="#f0f0f0")

# Label judul
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16), bg="#f0f0f0")
title_label.pack(pady=10)

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

# Membuat daftar input nilai mata pelajaran
entries = []
for i in range(10):
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

# Tombol untuk hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=10)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="Hasil Prediksi:", font=("Arial", 12), bg="#f0f0f0")
hasil_label.pack(pady=20)

# Menjalankan loop utama aplikasi
root.mainloop()
