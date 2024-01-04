import sqlite3

conn = sqlite3.connect('database_hewan.db')
cursor = conn.cursor()

id_hewan = 1
id_hewan2 = 3
jumlah_baru = 900
asal_baru = 'Nusa Tenggara Timur'

cursor.execute(f"UPDATE HEWAN SET jml_skrng = ? WHERE id_hewan = ?", (jumlah_baru, id_hewan))
cursor.execute(f"UPDATE HEWAN SET asal = ? WHERE id_hewan = ?", (asal_baru, id_hewan2))
conn.commit()

if cursor.rowcount > 0:
    print(f"Data hewan dengan ID {id_hewan} berhasil diupdate.")
    print(f"Data hewan dengan ID {id_hewan2} berhasil diupdate.")
else:
    print(f"Tidak ada data hewan dengan ID {id_hewan}.")
    print(f"Tidak ada data hewan dengan ID {id_hewan2}.")

