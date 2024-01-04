# Koneksi DB
import sqlite3
conn = sqlite3.connect('database_hewan.db')
# Buat Database dan Table Hewan
conn.execute('''
                CREATE TABLE HEWAN(
                 id_hewan INTEGER PRIMARY KEY AUTOINCREMENT,
                 nama_hewan VARCHAR(50),
                 jenis VARCHAR(50),
                 asal VARCHAR(50),
                 jml_skrng INTEGER(10),
                 thn_ditemukan INTEGER(10)
                )
                ''')
conn.close()
