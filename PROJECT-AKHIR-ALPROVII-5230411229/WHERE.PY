import sqlite3

koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()
kursor.execute("SELECT * FROM HEWAN WHERE jenis = 'Mamalia'")
baris_table = kursor.fetchall()

print("TABEL HEWAN:")
print("="*105)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID", "NAMA", "JENIS", "ASAL", "JML_SEKARANG", "THN_DITEMUKAN"))
print("-"*105)
for row in baris_table:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<20}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

koneksi.close()
