# Kelas Mahasiswa
class Mahasiswa:
    def _init_(self):
        self.daftar_mahasiswa = []

    def tambah(self, nama):
        self.daftar_mahasiswa.append(nama)
        print(f"Berhasil menambahkan {nama} ke daftar mahasiswa.")

    def tampilkan(self):
        print("Daftar Mahasiswa:")
        for nama in self.daftar_mahasiswa:
            print(f"- {nama}")

    def hapus(self, nama):
        if nama in self.daftar_mahasiswa:
            self.daftar_mahasiswa.remove(nama)
            print(f"Berhasil menghapus {nama} dari daftar mahasiswa.")
        else:
            print(f"{nama} tidak ditemukan dalam daftar mahasiswa.")

    def ubah(self, nama_lama, nama_baru):
        if nama_lama in self.daftar_mahasiswa:
            index = self.daftar_mahasiswa.index(nama_lama)
            self.daftar_mahasiswa[index] = nama_baru
            print(f"Berhasil mengubah {nama_lama} menjadi {nama_baru}.")
        else:
            print(f"{nama_lama} tidak ditemukan dalam daftar mahasiswa.")

# Contoh penggunaan
mahasiswa = Mahasiswa()
mahasiswa.tambah("John Doe")
mahasiswa.tambah("Jane Smith")
mahasiswa.tampilkan()
mahasiswa.hapus("Jane Smith")
mahasiswa.ubah("John Doe", "John Wick")
mahasiswa.tampilkan()
