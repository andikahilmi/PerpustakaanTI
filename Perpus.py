'''import streamlit as st
import json

# Fungsi untuk membaca data dari file JSON
def load_books():
    with open("buku.json", "r") as file:
        return json.load(file)

# Fungsi utama aplikasi Streamlit
def main():
    st.title("- Perpustakaan Jurusan Elektro - Prodi Teknik Informatika")
    
    # Memuat data buku
    books = load_books()

    # Menu aplikasi
    menu = ["Cari Buku", "Tampilkan Semua Buku"]
    choice = st.sidebar.selectbox("Pilih Menu", menu)

    if choice == "Cari Buku":
        st.subheader("Cari Buku")
        search_query = st.text_input("Masukkan Judul Buku:")
        if search_query:
            # Pencarian buku
            results = [book for book in books if search_query.lower() in book["Judul"].lower()]
            if results:
                for book in results:
                    st.write(book)
            else:
                st.warning("Buku tidak ditemukan.")

    elif choice == "Tampilkan Semua Buku":
        st.subheader("Semua Buku")
        for book in books:
            st.write(book)

# Menjalankan aplikasi
if __name__ == "__main__":
    main()'''

import streamlit as st
import json

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

# Fungsi untuk menampilkan informasi buku dengan format rapi
def display_book(book):
    #st.write(f"**Nomor**: {book.get('Nomor', 'N/A')}")
    st.write(f"**Judul**: {book.get('Judul', 'N/A')}")
    st.write(f"**Penulis**: {book.get('Penulis', 'N/A')}")
    st.write(f"**Tahun**: {book.get('Tahun', 'N/A')}")
    st.write(f"**Penerbit**: {book.get('Penerbit', 'N/A')}")
    st.write(f"**Jumlah Halaman**: {book.get('Jumlah Halaman', 'N/A')}")
    st.write(f"**ISBN**: {book.get('ISBN', 'N/A')}")
    st.write("---")  # Garis pembatas antar buku

# Fungsi login
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Verifikasi username dan password
        if username == "admin" and password == "admin":
            st.session_state["logged_in"] = True
            st.success("Login berhasil!")
        else:
            st.error("Username atau password salah.")

# Fungsi utama aplikasi Streamlit
def main():
    st.title("- Perpustakaan Jurusan Elektro - Prodi Teknik Informatika")
    # Menambahkan gambar di atas judul
    st.image("gambar.png", caption="Logo Perpustakaan", use_container_width=True)
    
    # Memuat data buku
    books = load_books()

    # Menu aplikasi
    menu = ["Cari Buku", "Tampilkan Semua Buku"]
    choice = st.sidebar.selectbox("Pilih Menu", menu)

    if choice == "Cari Buku":
        st.subheader("Cari Buku")

        # Input pencarian tunggal
    search_query = st.text_input("Masukkan kata kunci (Judul, Penulis, atau Tahun Terbit):")

    if search_query:
        # Pencarian buku
        results = [
            book for book in books
            if search_query.lower() in book["Judul"].lower() or
               search_query.lower() in book["Penulis"].lower() or
               search_query == str(book["Tahun"])
        ]

        if results:
            for book in results:
                display_book(book)
        else:
            st.warning("Buku tidak ditemukan.")

    elif choice == "Tampilkan Semua Buku":
        st.subheader("Semua Buku")
        if books:
            for book in books:
                display_book(book)
        else:
            st.warning("Tidak ada data buku yang tersedia.")

# Menjalankan aplikasi
#if __name__ == "__main__":
#    main()
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    main ()
else:
    login_page()


