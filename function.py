from functools import reduce

#pesan id tidak ditemukan
def emptyMessage():
    print("\n*------------------------------*")
    print("| ID yang dicari tidak ada !!! |")
    print("*------------------------------*\n")

#pesan perintah berhasil
def successMessage():
    print("\n*------------------------------*")
    print("| Perintah Berhasil Dilakukan  |")
    print("*------------------------------*\n")
    
#pesan gagal login
def loginFailed():
    print("\n*--------------------------------*")
    print("| Login Gagal Id Tidak Ditemukan |")
    print("*--------------------------------*\n")

#pesan error / kesalahan
def errorMessage():
    print("\n*------------------------------*")
    print("| Inputan Anda Tidak Valid !!! |")
    print("*------------------------------*\n")

#fungsi cek id kosong atau tidak
def isEmpty(param1, param2):
    cek = True
    for i in param2:
        if i['id'] == param1:
            cek = False
            break
    if cek:
        emptyMessage()

    return cek

#fungsi untuk login
def login(param, param1, param2):
    param = str.upper(param)
    cek = True

    for i in param2:
        if i['id'] == param and i['password'] == param1: 
            cek = False # berhasil login
            break
        else: 
            cek = True # tidak berhasil login
    
    return cek

#fungsi untuk menambahkan data siswa (penerapan high order function)
def inputStudent(param):
    def put_in(param1, param2):
        newStudent = {
        'id'       : 'STUDENT_' + str(len(param) + 1),
        'nama'     : param1,
        'pw'       : param2,
        'uharian1' : 0,
        'uharian2' : 0,
        'uharian3' : 0,
        'uas'      : 0
    }

        return param.append(newStudent)
    return put_in

#fungsi untuk menampilkan data siswa
def showStudent(param):
    print("\n|----- Daftar Siswa -------")
    for i in param:
        print("| ID                       : " + str(i['id']))
        print("| Nama                     : " + str(i['nama']))
        print("| Nilai Ulangan Harian 1   : " + str(i['uharian1']))
        print("| Nilai Ulangan Harian 2   : " + str(i['uharian2']))
        print("| Nilai Ulangan Harian 3   : " + str(i['uharian3']))
        print("| Nilai UAS                : " + str(i['uas']))
        print("| Nilai Akhir              : " + str(((((i['uharian1'] + i['uharian2'] + i['uharian3']) / 3) + i['uas']) / 2)) + "\n")

#fungsi untuk mengubah nilai siswa
def editNilai(param, param1, param2, param3, param4, param5):
    for i in param:
        if i['id'] == param1:
            i['uharian1'] = param2
            i['uharian2'] = param3
            i['uharian3'] = param4
            i['uas']      = param5

#fungsi untuk mengubah data siswa
def editAkun(param, param1, param2, param3):
    for i in param:
        if i['id'] == param1:
            i['nama']     = param2
            i['password'] = param3

#fungsi untuk menghapus nilai siswa
def hapusNilai(param, param1):
    for i in param:
        if i['id'] == param1:
            i['uharian1'] = 0
            i['uharian2'] = 0
            i['uharian3'] = 0
            i['uas']      = 0

#fungsi untuk menghapus data siswa
def hapusAkun(param, param1):
    for i in param:
        if i['id'] == param1:
            param.remove(i)

#fungsi untuk mengadakan untuk
def ulanganHarian(param, param1, param2):
    for i in param1:
        if i['id'] == param:
            if i['count'] <= 2:
                hitung = i['count'] + 1
                for x in param2:
                    print("| Untuk " + x['id'])
                    nilai       = int(input("| Masukkan Nilai Ulangan Harian " + str(hitung) + " : "))
                    teksuh      = 'uharian' + str(hitung)
                    x[teksuh]   = nilai
            else:
                print("| Ulangan Harian Hari Ini Sudah 3 kali :)")
        else:
            print("hiya gamasuk")
        if i['id'] == param:
            now = i['count']
            i['count'] = now + 1

#fungsi untuk mereset kesempatan ulangan harian guru
def nextDay(param, param1):
    for i in param:
        if i['id'] == param1:
            i['count'] = 0

#fungsi untuk menampilkan semua nama siswa (penerapan map dan lambda)
def namaSiswa(param):
    nama_nih = map(lambda i: str('| Nama Siswa : ') + i['nama'], param)

    return nama_nih

#fungsi untuk memfilter nilai siswa diatas 80 (penerapan filter dan lambda)
def filterNilai(param):
    kkm = filter(lambda i: i['uas'] > 80, param)

    return kkm

#fungsi untuk menampilkan data siswa berdasarkan Id
def studentInfo(param, param1):
    for i in range(len(param)):
        if param[i]['id'] == param1:
            nama = param[i]['nama']
            uh1  = param[i]['uharian1']
            uh2  = param[i]['uharian2']
            uh3  = param[i]['uharian3']
            uas  = param[i]['uas']
            break

    infoStudent = {
        'nama'  : nama,
        'uh1'   : uh1,
        'uh2'   : uh2,
        'uh3'   : uh3,
        'uas'   : uas
    }

    return infoStudent

def average(param, param1):
    for i in param:
        if i['id'] == param1:
            temp = [i['uharian1'], i['uharian2'], i['uharian3'], i['uas']]
            total = reduce(lambda x, y: x + y, temp)
    total = total / 4

    return total