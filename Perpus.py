import streamlit as st
import json
import pandas as pd

# Fungsi untuk membaca data dari file JSON
def load_books():
    try:
        with open("buku.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("File buku.json tidak ditemukan.")
        return []
    except json.JSONDecodeError:
        st.error("Format file JSON tidak valid.")
        return []

#new
# Fungsi untuk menyimpan buku baru ke file JSON
def save_book(new_book):
    books = load_books()
    books.append(new_book)
    with open("buku.json", "w") as file:
        json.dump(books, file, indent=4)
    st.success("Buku berhasil ditambahkan!")
    
# Fungsi untuk menampilkan informasi buku dengan format rapi
def display_book(book):
    st.write(f"**Judul**: {book.get('Judul', 'N/A')}")
    st.write(f"**Penulis**: {book.get('Penulis', 'N/A')}")
    st.write(f"**Tahun**: {book.get('Tahun', 'N/A')}")
    st.write(f"**Penerbit**: {book.get('Penerbit', 'N/A')}")
    st.write(f"**Jumlah Halaman**: {book.get('Jumlah Halaman', 'N/A')}")
    st.write(f"**ISBN**: {book.get('ISBN', 'N/A')}")
    st.write(f"**Rak Buku**: {book.get('Rak Buku', 'N/A')}")
    st.write(f"**Nomor Buku**: {book.get('Nomor Buku', 'N/A')}")
    st.write("---")  # Garis pembatas antar buku

# Fungsi login
def login_page():
    st.title("Login Portal Perpustakaan")
    # Inisialisasi session_state untuk menyimpan kredensial
    if "credentials" not in st.session_state:
        st.session_state["credentials"] = {
            "algortima": "algoritma",
            "hilmi": "hilmi",
            "farel": "farel",
            "saskia": "saskia",
            "tanaya": "tanaya",
            "nir": "nir",
        }
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

        # Tombol login
    if st.button("Login"):
        credentials = st.session_state["credentials"]
        if username in credentials and password == credentials[username]:
            st.session_state["logged_in"] = True
            st.success("Login berhasil!")
        else:
            st.error("Username atau password salah.")
    
# Fungsi utama aplikasi Streamlit
def main():
    st.title("--Portal Pencarian Koleksi Buku di  Perpustakaan Jurusan Elektro  Prodi Teknik Informatika--")
    
    # Memuat data buku
    books = load_books()

    # Menu aplikasi
    menu = ["Cari Buku", "Tampilkan Semua Buku","Tambah Buku", "Tentang Aplikasi", "Tim Penyusun"]
    choice = st.sidebar.radio("Pilih Menu", menu)

    search_query = ""
    search_option =""

    if choice == "Cari Buku":
        st.subheader("Cari Buku")

        # Pilihan metode pencarian
        search_option = st.radio("Cari berdasarkan:", ["Judul", "Penulis", "Tahun Terbit"])

        # Input pencarian berdasarkan pilihan
        if search_option:
            search_query = st.text_input(f"Masukkan {search_option}:")
        # Input pencarian tunggal
        if st.button("Cari Buku"):
            if search_query:
            # Pencarian buku berdasarkan opsi
                if search_option == "Judul":
                    results = [book for book in books if search_query.lower() in book["Judul"].lower()]
                elif search_option == "Penulis":
                    results = [book for book in books if search_query.lower() in book["Penulis"].lower()]
                elif search_option == "Tahun Terbit":
                    results = [book for book in books if search_query == str(book["Tahun"])]

            #Menjumlahkan buku yang di temukan    
                total_found = len(results)
                st.write(f"Total buku ditemukan: {total_found}")

                # Menampilkan hasil dalam bentuk tabel jika ada hasil
                if results:
                # Konversi hasil pencarian menjadi DataFrame pandas
                    df = pd.DataFrame(results)

                    # Konversi kolom "Tahun" agar tampil tanpa desimal
                    if "Tahun" in df.columns:
                        df["Tahun"] = pd.to_numeric(df["Tahun"], errors="coerce").fillna(0).astype(str).replace(0, "")
                    elif "Jumlah Halaman" in df.columns:
                        df["Jumlah Halaman"] = pd.to_numeric(df["Jumlah Halaman"], errors="coerce").fillna(0).astype(int).replace(0, "")
                    elif "Nomor Buku" in df.columns:
                        df["Nomor Buku"] = pd.to_numeric(df["Nomor Buku"], errors="coerce").fillna(0).astype(int).replace(0, "")

                    st.table(df)  # Menampilkan dalam bentuk tabel
                else:
                    st.warning("Buku tidak ditemukan.")

                #if results:
                #    for book in results:
                #        display_book(book)
                #else:
                #    st.warning("Buku tidak ditemukan.")

    elif choice == "Tampilkan Semua Buku":
        st.subheader("Semua Buku")
        if books:
            for book in books:
                display_book(book)
        else:
            st.warning("Tidak ada data buku yang tersedia.")
    #new
    elif choice == "Tambah Buku":
        st.subheader("Tambah Buku Baru")

        judul = st.text_input("Judul")
        penulis = st.text_input("Penulis")
        tahun = st.text_input("Tahun Terbit")
        penerbit = st.text_input("Penerbit")
        jumlah_halaman = st.number_input("Jumlah Halaman", min_value=1)
        isbn = st.text_input("ISBN")
        rak_buku = st.text_input("Rak Buku")
        nomor = st.text_input("Nomor")
    
        if st.button("Simpan Buku"):
            if judul and penulis and tahun and penerbit:
                new_book = {
                    "Judul": judul,
                    "Penulis": penulis,
                    "Tahun": tahun,
                    "Penerbit": penerbit,
                    "Jumlah Halaman": jumlah_halaman,
                    "ISBN": isbn,
                    "Rak Buku": rak_buku,
                    "Nomor": nomor,
                }
                save_book(new_book)
            else:
                st.error("Mohon isi semua kolom yang diperlukan.")
    
    elif choice == "Tentang Aplikasi":
        st.subheader("Tentang Aplikasi")
        st.write("""
        Aplikasi ini adalah portal pencarian koleksi buku di perpustakaan Jurusan Elektro - Prodi Teknik Informatika.
        Anda dapat mencari buku berdasarkan judul, penulis, atau tahun terbit, serta menampilkan semua koleksi buku yang tersedia.
        """)

    elif choice == "Tim Penyusun":
        st.subheader("Tim Penyusun")
        st.markdown("""
        Aplikasi ini merupakan tugas dari kelompok 3 mata kuliah algoritma 
        yang berisikan 5 orang yaitu :
        - Hilmi Andika
        - Muhammad Farel 
        - Siang Nir
        - Saskia Rafina Putri
        - Tanaya Dzakiyya Isnania
        """)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    main ()
else:
    login_page()


