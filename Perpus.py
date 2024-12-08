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
if __name__ == "__main__":
    main()


