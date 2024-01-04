import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

jenis_hewan = 'Mamalia'
cursor.execute(f"DELETE FROM HEWAN WHERE jenis = ?", (jenis_hewan,))
conn.commit()

if cursor.rowcount > 0:
    print(f"Data hewan dengan jenis {jenis_hewan} berhasil dihapus.")
else:
    print(f"Tidak ada data hewan dengan jenis {jenis_hewan}.")

conn.close()
