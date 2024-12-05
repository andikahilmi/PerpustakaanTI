'''import streamlit as st

# Daftar 21 buku
books = [
    {"Nomor": 1, "Judul": "Langkah Mudah Belajar Analisis Data dengan Python untuk Pemula", "Penulis": "Randi Adrika Putra", "Tahun": 2024, "Penerbit": "PT. Anak Hebat Indonesia", "Jumlah": 206, "ISBN": "978-623-164-617-0"},
    {"Nomor": 2, "Judul": "HTML, PHP & MySQL untuk Pemula", "Penulis": "Jubilee Enterprise", "Tahun": 2018, "Penerbit": "PT Elex Media Komputindo", "Jumlah": 200, "ISBN": "978-602-048-622-2"},
    # Tambahkan buku lainnya sesuai kebutuhan
    {"Nomor": 21, "Judul": "Panduan Mudah Membuat Diskless System", "Penulis": "Rusmanto, R. Kresno Aji", "Tahun": 2024, "Penerbit": "Dian Rakyat", "Jumlah": 189, "ISBN": "979-523-645-8"}
]

# Fungsi utama Streamlit
def main():
    # Judul aplikasi
    st.title("Perpustakaan Elektro -
             Teknik Informatika")
    st.subheader("Selamat datang di sistem pencarian buku!")

    # Menu utama
    menu = ["Cari Buku", "Tampilkan Semua Buku", "Tentang"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Cari Buku":
        st.subheader("Pencarian Buku")
        query = st.text_input("Masukkan judul buku:")
        if query:
            results = [book for book in books if query.lower() in book["Judul"].lower()]
            if results:
                st.write(f"Menemukan {len(results)} hasil:")
                for book in results:
                    st.write(f"""
                    **Judul**: {book['Judul']}
                    **Penulis**: {book['Penulis']}
                    **Tahun**: {book['Tahun']}
                    **Penerbit**: {book['Penerbit']}
                    **Jumlah Halaman**: {book['Jumlah']}
                    **ISBN**: {book['ISBN']}
                    """)
            else:
                st.warning("Buku tidak ditemukan.")

    elif choice == "Tampilkan Semua Buku":
        st.subheader("Daftar Semua Buku")
        for book in books:
            st.write(f"""
            **Nomor**: {book['Nomor']}
            **Judul**: {book['Judul']}
            **Penulis**: {book['Penulis']}
            **Tahun**: {book['Tahun']}
            **Penerbit**: {book['Penerbit']}
            **Jumlah Halaman**: {book['Jumlah']}
            **ISBN**: {book['ISBN']}
            """)
    
    elif choice == "Tentang":
        st.subheader("Tentang Aplikasi")
        st.write("Aplikasi ini dibuat untuk membantu pencarian buku di Perpustakaan Elektro - Teknik Informatika.")

if __name__ == "__main__":
    main()'''

import streamlit as st
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
    main()

