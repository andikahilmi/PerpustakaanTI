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
    #st.write(f"**Sampul Buku**: {book.get('Sampul', 'N/A')}")
    # Menambahkan link setelah Nomor Buku menggunakan Markdown
    # Mengambil link
    link = book.get('Link', '')
    if link:
        # Menampilkan link menggunakan HTML dalam Markdown
        st.markdown(f"**Link Detail**: <a href='{link}' target='_blank' style='color: blue;'>Klik di sini</a>", unsafe_allow_html=True)
      
    st.write("---")  # Garis pembatas antar buku
   
# Fungsi untuk menghapus buku dari file JSON
def delete_book(book_title):
    books = load_books()  # Memuat data buku
    book_to_delete = None
    for book in books:
        if book['Judul'].lower() == book_title.lower():  # Mencocokkan Judul
            book_to_delete = book
            break

    if book_to_delete:
        books.remove(book_to_delete)  # Menghapus buku yang ditemukan
        with open("buku.json", "w") as file:
            json.dump(books, file, indent=4)  # Menyimpan perubahan ke file
        st.success(f"Buku '{book_to_delete['Judul']}' berhasil dihapus.")
    else:
        st.error(f"Buku dengan judul '{book_title}' tidak ditemukan.")

# Fungsi login
def login_page():
        # CSS untuk menambahkan background
    page_bg_img = '''
    <style>
    /* Atur background halaman */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/andikahilmi/PerpustakaanTI/main/img/bgg.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        height: auto;
    }
    
    </style>
    '''
        # Memasukkan CSS ke dalam aplikasi Streamlit
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.title("Digital Library")
    st.write("Portal Pencarian Koleksi Buku di Perpustakaan Jurusan Teknik Elektro Politeknik Negeri Pontianak")
    st.markdown("Panduan Penggunaan Portal Digital Library Klik [disini](https://www.google.com)")
    st.write("")
    st.write("Silahkan Login")

    if "credentials" not in st.session_state:
        st.session_state["credentials"] = {
            "admin": "hilmi123",
            "algoritma": "algoritma",
            "hilmi": "hilmi",
            "farel": "farel",
            "saskia": "saskia",
            "tanaya": "tanaya",
            "nir": "nir",
        }
    username = st.text_input("Nama Pengguna")
    password = st.text_input("Kata Sandi", type="password")

        # Tombol login
    if st.button("Masuk"):
        credentials = st.session_state["credentials"]
        if username in credentials and password == credentials[username]:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username#
            st.session_state["is_admin"] = (username == "admin")#
            st.success("Login berhasil!")
        else:
            st.error("Nama Pengguna atau Kata Sandi salah.")
    
# Fungsi utama aplikasi Streamlit
def main():
    #st.title("Selamat Datang!")
    #st.write("Terimakasih Telah mengunjugi Portal Pencarian Koleksi Buku di Perpustakaan Jurusan Elektro Politeknik Negeri Pontianak. Portal ini hanya menyediakan koleksi buku bidang Komputer dan Informatika.")
    #st.write("")

    # Memuat data buku
    books = load_books()

    # Menu aplikasi
    menu = ["Cari Buku", "Tampilkan Semua Buku", "Tentang Aplikasi", "Tim Penyusun"]
    if st.session_state.get("is_admin"):
        menu.append("Hapus Buku")
        menu.append("Tambah Buku")
        
    choice = st.sidebar.radio("Pilih Menu", menu)

    search_query = ""
    search_option =""

    if choice == "Cari Buku":
        st.title("Selamat Datang!")
        st.write("Terimakasih Telah mengunjugi Portal Pencarian Koleksi Buku di Perpustakaan Jurusan Elektro Politeknik Negeri Pontianak. Portal ini hanya menyediakan koleksi buku bidang Komputer dan Informatika.")
        st.write("")
        st.subheader("Silahkan Pilih Katagori untuk melakukan pencarian buku")
        
        # Pilihan metode pencarian
        search_option = st.radio("Pilih Katagori :", ["Judul", "Penulis", "Tahun Terbit"])
        
        # Input pencarian berdasarkan pilihan
        if search_option:
            search_query = st.text_input(f"Masukkan {search_option}:")
            
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
            st.write(f"Hasil Pencarian Buku ditemukan Sebanyak : {total_found} Judul")

            # Menampilkan hasil dalam bentuk tabel jika ada hasil
            if results:
                # Konversi hasil pencarian menjadi DataFrame pandas
                df = pd.DataFrame(results)

                # Konversi kolom "Tahun" agar tampil tanpa desimal
                if "Tahun" in df.columns:
                    df["Tahun"] = pd.to_numeric(df["Tahun"], errors="coerce").fillna(0).astype(int).replace(0, "")
                elif "Jumlah Halaman" in df.columns:
                    df["Jumlah Halaman"] = pd.to_numeric(df["Jumlah Halaman"], errors="coerce").fillna(0).astype(int).replace(0, "")
                elif "Nomor Buku" in df.columns:
                    df["Nomor Buku"] = pd.to_numeric(df["Nomor Buku"], errors="coerce").fillna(0).astype(int).replace(0, "")

                st.table(df)  # Menampilkan dalam bentuk tabel
            else:
                st.warning("Buku tidak ditemukan.")

    elif choice == "Tampilkan Semua Buku":
        st.subheader("Semua Buku")

        if books:
            total_books = len(books)
            st.write(f"**Total Buku Tersedia: {total_books}**")

            # Konversi list buku menjadi DataFrame pandas
            df_books = pd.DataFrame(books)

            # Jika kolom tertentu ada, lakukan format yang sesuai (misalnya Tahun, Jumlah Halaman, Nomor Buku)
            if "Tahun" in df_books.columns:
                df_books["Tahun"] = pd.to_numeric(df_books["Tahun"], errors="coerce").fillna(0).astype(int).replace(0, "")
            if "Jumlah Halaman" in df_books.columns:
                df_books["Jumlah Halaman"] = pd.to_numeric(df_books["Jumlah Halaman"], errors="coerce").fillna(0).astype(int).replace(0, "")
            if "Nomor Buku" in df_books.columns:
                df_books["Nomor Buku"] = pd.to_numeric(df_books["Nomor Buku"], errors="coerce").fillna(0).astype(int).replace(0, "")

            # Menampilkan DataFrame sebagai tabel
            st.table(df_books)
        else:
            st.warning("Tidak ada data buku yang tersedia.")   
    ###new
    # Form untuk menambahkan buku
    elif choice == "Tambah Buku":
        st.subheader("Tambah Buku Baru")
        
        with st.form("form_tambah_buku"):
            judul = st.text_input("Judul", max_chars=100)
            penulis = st.text_input("Penulis", max_chars=100)
            tahun = st.text_input("Tahun Terbit")
            penerbit = st.text_input("Penerbit", max_chars=100)
            jumlah_halaman = st.number_input("Jumlah Halaman", min_value=1, step=1)
            isbn = st.text_input("ISBN")
            rak_buku = st.text_input("Rak Buku")
            nomor = st.text_input("Nomor Buku", max_chars=20)

            # Tombol submit dalam form
            submitted = st.form_submit_button("Simpan Buku")

            # Validasi semua kolom harus diisi
            if submitted:
                if not all([judul, penulis, tahun, penerbit, isbn, rak_buku, nomor]):
                    st.error("Mohon isi semua kolom sebelum menyimpan buku.")
                elif not tahun.isdigit() or len(tahun) != 4:
                    st.error("Tahun harus berupa angka dengan format 4 digit.")
                else:
                    new_book = {
                        "Judul": judul,
                        "Penulis": penulis,
                        "Tahun": tahun,
                        "Penerbit": penerbit,
                        "Jumlah Halaman": jumlah_halaman,
                        "ISBN": isbn,
                        "Rak Buku": rak_buku,
                        "Nomor Buku": nomor,
                    }
                    save_book(new_book)
                    
    elif choice == "Hapus Buku" and st.session_state.get("is_admin"):
        st.subheader("Hapus Buku Berdasarkan Judul")

        book_title = st.text_input("Masukkan Judul Buku yang ingin dihapus")
    
    # Tombol untuk menghapus buku
        if st.button("Hapus Buku"):
            if book_title:  # Pastikan ada input Judul
                delete_book(book_title)
            else:
                st.error("Mohon masukkan judul buku yang ingin dihapus.")
    
            
    elif choice == "Tentang Aplikasi":
        st.subheader("Tentang Aplikasi")
        st.markdown("""
        Aplikasi ini adalah portal pencarian koleksi buku di perpustakaan Jurusan Elektro - Prodi Teknik Informatika.
        Portal ini Terdiri dari 7 fitur, antara lain : Masuk, Mencari Buku, Tampilkan Semua Buku, Tambah Buku, Tentang Portal, Tim Penyusun, Dan keluar.
        
        Fitur-Fitur Utama Portal :
        1. Masuk :  
        Fitur ini memungkinkan pengguna untuk masuk ke sistem dengan akun terdaftar guna mengakses semua layanan yang tersedia.
        
        2. Mencari Buku :  
        Pengguna dapat mencari buku berdasarkan judul, penulis, atau kata kunci tertentu untuk menemukan koleksi yang diinginkan.
        
        3. Tampilkan Semua Buku :  
        Fitur ini menampilkan daftar lengkap semua buku yang tersedia di perpustakaan dalam bentuk tabel yang rapi dan mudah dibaca.
        
        4. Tambah Buku :  
        Anda dapat menambahkan data buku baru ke dalam sistem dengan informasi lengkap seperti judul, penulis, tahun terbit, dan jumlah halaman.
        
        5. Tentang Portal :  
        Berisi informasi tentang tujuan dan manfaat dari portal ini sebagai layanan pendukung akademik di Jurusan Elektro - Prodi Teknik Informatika.
        
        6. Tim Penyusun :  
        Menampilkan informasi tentang tim pengembang yang telah membuat dan mengelola portal ini.
        
        7. Keluar :  
        Fitur ini digunakan untuk keluar dari portal dengan aman dan mengakhiri sesi pengguna.
        """)

    elif choice == "Tim Penyusun":
        st.subheader("Tim Penyusun")
        st.image("https://raw.githubusercontent.com/andikahilmi/PerpustakaanTI/main/img/WhatsApp%20Image%202025-01-09%20at%2020.33.33_67578581.jpg")


        st.markdown("""
        Aplikasi ini merupakan tugas dari kelompok 3 mata kuliah algoritma 
        yang berisikan 5 orang yaitu :
        - Hilmi Andika
        - Muhammad Farel 
        - Siang Nir
        - Saskia Rafina Fitri
        - Tanaya Dzakiyya Isnania
        """)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    main ()
    if st.sidebar.button("Keluar"):
        st.session_state.clear()  # Reset semua state
else:
    login_page()

