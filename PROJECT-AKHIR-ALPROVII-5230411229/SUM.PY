import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

# Menjalankan query SUM
cursor.execute("SELECT SUM(jml_skrng) FROM HEWAN")
total_hewan = cursor.fetchone()[0]

print(f"Total Jumlah Hewan Saat Ini Adalah: {total_hewan}")

# Menutup koneksi
conn.close()
