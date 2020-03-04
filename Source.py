# Class
class Karyawan():
    Divisi = "Engineering"
    __Nilai = 0  # Private

    def __init__(self, input_nama, input_nik):
        self.nama = input_nama  # public
        self.nik = input_nik  # public

    def Pelatihan1(self, input_nilai):
        self.__Nilai += input_nilai

    def Pelatihan2(self, input_nilai):
        self.__Nilai += input_nilai

    def CekStatus(self):
        if self.__Nilai <= 50:
            print(self.nama, 'Tidak Lolos')
        else:
            print(self.nama, 'Lolos')

#Main Program

Karyawan1 = Karyawan("Rizky Khapidsyah", 64376284)
Karyawan2 = Karyawan("Muhammad Fahrozi", 73593463)

Karyawan1.Pelatihan1(40)
Karyawan1.Pelatihan2(84)
Karyawan1.CekStatus()

Karyawan2.Pelatihan1(40)
Karyawan2.Pelatihan2(84)
Karyawan2.CekStatus()


