import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Fungsi untuk menampilkan loading screen
def show_loading():
    loading_window = tk.Toplevel()
    loading_window.title("Kalkulator IMT by Nurul Kumala")
    
    width = 500
    height = 300
    screen_width = loading_window.winfo_screenwidth()
    screen_height = loading_window.winfo_screenheight()

    position_top = int(screen_height / 2 - height / 2)
    position_left = int(screen_width / 2 - width / 2)
    loading_window.geometry(f'{width}x{height}+{position_left}+{position_top}')
    loading_window.config(bg="#ff80ab")

    frame_center = tk.Frame(loading_window, bg="#ff80ab")
    frame_center.place(relx=0.5, rely=0.5, anchor='center')

    label_loading = tk.Label(frame_center, text="Loading...", font=("Arial", 16), fg="white", bg="#ff80ab")
    label_loading.pack(pady=5)

    progress_bar = ttk.Progressbar(frame_center, length=300, mode='determinate', maximum=100)
    progress_bar.pack(pady=5)
    
    # Fungsi untuk memperbarui progress bar (PERULANGAN/LOOP)
    def update_progress(progress):
        progress_bar['value'] = progress
        if progress < 100:
            loading_window.after(50, update_progress, progress + 2)
        else:
            loading_window.destroy()
            root.deiconify()
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            position_top = int(screen_height / 2 - 600 / 2)
            position_left = int(screen_width / 2 - 900 / 2) 
            root.geometry(f"900x600+{position_left}+{position_top}")
            
    update_progress(0)

# Membuat window Tkinter utama
root = tk.Tk()
root.title("Kalkulator IMT by Nurul Kumala")
root.withdraw()
show_loading()
root.geometry("900x600")
root.config(bg="#fce4ec")

# Judul Aplikasi
frame_judul = tk.Frame(root, bg="#ff80ab", pady=10)
frame_judul.pack(fill="x")
label_judul = tk.Label(frame_judul, text="KALKULATOR IMT (Indeks Massa Tubuh)", font=("Hobo Std", 31, "bold"), fg="white", bg="#ff80ab", relief="raised", bd=5)
label_judul.pack()
label_subjudul = tk.Label(frame_judul, text="Silahkan masukkan detail informasi pada kolom yang tersedia.", font=("Internet Friends", 18), fg="white", bg="#ff80ab")
label_subjudul.pack(pady=10)

# Input dan output
frame_main = tk.Frame(root, bg="#fce4ec")
frame_main.pack(pady=20, padx=40, fill="both", expand=True)

frame_input = tk.Frame(frame_main, bg="#fce4ec")
frame_input.pack(side="left", padx=20, fill="y", expand=True)

tk.Label(frame_input, text="Usia (tahun):", bg="#fce4ec", font=("Arial", 18, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_usia = tk.Entry(frame_input, width=30, font=("Arial", 18))
entry_usia.grid(row=0, column=1, padx=10, pady=15)

tk.Label(frame_input, text="Jenis Kelamin:", bg="#fce4ec", font=("Arial", 18, "bold")).grid(row=1, column=0, padx=10, pady=15, sticky="w")
gender_var = tk.StringVar(value="Laki-laki")
tk.Radiobutton(frame_input, text="Laki-laki", variable=gender_var, value="Laki-laki", bg="#fce4ec", font=("Arial", 18)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
tk.Radiobutton(frame_input, text="Perempuan", variable=gender_var, value="Perempuan", bg="#fce4ec", font=("Arial", 18)).grid(row=2, column=1, padx=10, pady=10, sticky="w")

tk.Label(frame_input, text="Berat Badan (kg):", bg="#fce4ec", font=("Arial", 18, "bold")).grid(row=3, column=0, padx=10, pady=15, sticky="w")
entry_berat = tk.Entry(frame_input, width=30, font=("Arial", 18))
entry_berat.grid(row=3, column=1, padx=10, pady=15)

tk.Label(frame_input, text="Tinggi Badan (cm):", bg="#fce4ec", font=("Arial", 18, "bold")).grid(row=4, column=0, padx=10, pady=15, sticky="w")
entry_tinggi = tk.Entry(frame_input, width=30, font=("Arial", 18))
entry_tinggi.grid(row=4, column=1, padx=10, pady=15)

# Fungsi untuk menghitung IMT dan menampilkan grafik (FUNCTION DAN METHOD)
def hitung_imt():
    try:
        # Validasi input usia (hanya angka)
        usia = entry_usia.get()
        if not usia.isdigit():
            messagebox.showerror("Error", "Input hanya boleh berisi angka!")
            return
        usia = int(usia)

        # Validasi input berat badan (hanya angka)
        berat_badan = entry_berat.get()
        if not berat_badan.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Input hanya boleh berisi angka!")
            return
        berat_badan = float(berat_badan)

        # Validasi input tinggi badan (hanya angka)
        tinggi_badan_cm = entry_tinggi.get()
        if not tinggi_badan_cm.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Input hanya boleh berisi angka!")
            return
        tinggi_badan_cm = float(tinggi_badan_cm)  # Tinggi badan dalam cm

        gender = gender_var.get()

        # Validasi tinggi badan
        if tinggi_badan_cm <= 0:
            messagebox.showerror("Input Tidak Valid", "Tinggi badan harus lebih besar dari 0!")
            return
        # Mengonversi tinggi badan dari cm ke meter
        tinggi_badan = tinggi_badan_cm / 100

        # Menghitung IMT
        imt = berat_badan / (tinggi_badan ** 2)

        # Menentukan kategori IMT (PENGKONDISIAN)
        if imt < 18.5:
            kategori = "Kurang Berat Badan"
        elif 18.5 <= imt < 24.9:
            kategori = "Normal"
        elif 25 <= imt < 29.9:
            kategori = "Kelebihan Berat Badan"
        else:
            kategori = "Obesitas"

        # Menampilkan hasil IMT dan kategori
        label_hasil.config(text=f"IMT Anda: {imt:.2f}")
        label_kategori.config(text=f"Kategori: {kategori}")

        # Menampilkan grafik IMT (FUNCTION DAN METHOD)
        tampilkan_grafik(imt, kategori)

    except ValueError:
        messagebox.showerror("Input Salah", "Mohon masukkan angka yang valid!")

# Fungsi untuk menampilkan grafik IMT dalam GUI (FUNCTION DAN METHOD)
def tampilkan_grafik(imt, kategori): 
    kategori_labels = ['Kurang Berat Badan', 'Normal', 'Kelebihan Berat Badan', 'Obesitas']
    kategori_values = [18.5, 24.9, 29.9, 40]  # Rentang kategori IMT

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(kategori_labels, kategori_values, color=['blue', 'green', 'orange', 'red'], alpha=0.7)
    ax.axvline(x=kategori_labels.index(kategori), color='black', linestyle='--', label=f'IMT Anda ({imt:.2f})')

    ax.set_title('Kategori IMT')
    ax.set_xlabel('Kategori')
    ax.set_ylabel('Batas IMT')
    ax.legend()
    ax.set_xticklabels(kategori_labels, fontsize=8)
    
    # Membersihkan canvas sebelumnya
    for widget in frame_grafik.winfo_children():
        widget.destroy()

    # Menampilkan grafik di dalam GUI menggunakan Canvas
    canvas = FigureCanvasTkAgg(fig, master=frame_grafik)  
    canvas.draw()
    canvas.get_tk_widget().pack(side="top", padx=20)  

# Fungsi untuk mereset form dan hasil
def reset_form():
    # Mengosongkan kolom input
    entry_usia.delete(0, tk.END)
    entry_berat.delete(0, tk.END)
    entry_tinggi.delete(0, tk.END)

    # Mengembalikan pilihan jenis kelamin ke default (SETTER)
    gender_var.set("Laki-laki")

    # Menghapus hasil IMT dan kategori
    label_hasil.config(text="Hasil IMT akan ditampilkan di sini")
    label_kategori.config(text="Kategori akan ditampilkan di sini")

    # Menghapus grafik
    for widget in frame_grafik.winfo_children():
        widget.destroy()

# Fungsi untuk keluar dari aplikasi
def exit_app():
    root.quit()

# Tombol untuk menghitung IMT
btn_hitung = tk.Button(frame_input, text="Hitung IMT", command=hitung_imt, bg="#ff80ab", font=("Arial", 17, "bold"), relief="raised", bd=6, width=15)
btn_hitung.grid(row=5, column=0, columnspan=2, pady=40)

# Tombol Reset dan Exit
btn_reset = tk.Button(frame_input, text="Reset", command=reset_form, bg="#ff80ab", font=("Arial", 17, "bold"), relief="raised", bd=6, width=10)
btn_reset.grid(row=6, column=0, pady=5)

btn_exit = tk.Button(frame_input, text="Exit", command=exit_app, bg="#ff80ab", font=("Arial", 17, "bold"), relief="raised", bd=6, width=10)
btn_exit.grid(row=6, column=1, padx=5, pady=5)

# Frame untuk menampilkan hasil analisis IMT dan grafik
frame_output = tk.Frame(frame_main, bg="#fce4ec")
frame_output.pack(side="left", padx=20, fill="both", expand=True)

# Frame untuk hasil analisis IMT
frame_analisis = tk.Frame(frame_output, bg="#fce4ec")
frame_analisis.pack(side="top", fill="both", expand=True, padx=20)

# Label untuk menampilkan hasil IMT dan kategori
label_hasil = tk.Label(frame_analisis, text="Hasil IMT akan ditampilkan di sini", font=("Arial", 18), bg="#fce4ec", relief="groove", bd=3, padx=10, pady=10)
label_hasil.pack(pady=15)

label_kategori = tk.Label(frame_analisis, text="Kategori akan ditampilkan di sini", font=("Arial", 18), bg="#fce4ec", relief="groove", bd=3, padx=10, pady=10)
label_kategori.pack(pady=15)

# Frame untuk grafik IMT
frame_grafik = tk.Frame(frame_output, bg="#fce4ec")
frame_grafik.pack(side="bottom", fill="both", expand=True)

# Menjalankan aplikasi
root.mainloop()