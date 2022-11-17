from function import *
dataTeacher = [
{
    'id'       : 'TEACHER_1',
    'nama'     : 'James Arthur',
    'password' : '123',
    'count'    : 0
},
]

dataStudent = [
    {
        'id'       : 'STUDENT_1',
        'nama'     : 'Billie',
        'password' : '123',
        'uharian1' : 80,
        'uharian2' : 80,
        'uharian3' : 80,
        'uas'      : 95
    },
    {
        'id'       : 'STUDENT_2',
        'nama'     : 'Eilish',
        'password' : '123',
        'uharian1' : 80,
        'uharian2' : 80,
        'uharian3' : 80,
        'uas'      : 70
    },
    {
        'id'       : 'STUDENT_3',
        'nama'     : 'Anne Marie',
        'password' : '123',
        'uharian1' : 80,
        'uharian2' : 80,
        'uharian3' : 80,
        'uas'      : 95
    },
]

a = True
while(a):
    print("\n|--------------------------|")
    print("|       Login Sebagai      |")
    print("|--------------------------|")
    print("| 1. Teacher               |")
    print("| 2. Siswa                 |")
    print("|--------------------------|")

    pilihan = int(input("| Masukkan Pilihan Anda : "))
    print("|--------------------------------")
    id = input("| Masukkan ID : ")
    pw = input("| Masukkan PW : ")

    id = str.upper(id)

    if pilihan == 1:
        cek = login(id, pw, dataTeacher)
    elif pilihan == 2:
        cek = login(id, pw, dataStudent)

    a = cek

    if a:
        loginFailed()
    else:
        if pilihan == 1:
            x = True
            while (x):
                print("\n|--------------------------|")
                print("|        Opsi Teacher      |")
                print("|--------------------------|")
                print("| 1. Input Data Siswa Baru |")
                print("| 2. Tampil Data Siswa     |")
                print("| 3. Edit Nilai Siswa      |")
                print("| 4. Edit Akun Siswa       |")
                print("| 5. Hapus Nilai Siswa     |")
                print("| 6. Hapus Akun Siswa      |")
                print("| 7. Adakan Ulangan Harian |")
                print("| 8. Ganti Hari            |")
                print("| 9. Tampilkan Nama Siswa  |")
                print("| 10. Tampilkan Uas KKM    |")
                print("| 11. Logout               |")
                print("| 12. Exit                 |")
                print("|--------------------------|")

                pilihan = int(input("| Masukkan Pilihan Anda : "))
                match pilihan:
                    case 1:
                        print("\n|----------------------------------|")
                        print("|    Masukkan Data Siswa Baru      |")
                        print("|----------------------------------|")
                        nama    = str(input("| Nama          : "))
                        pw      = str(input("| Password      : "))

                        temp = inputStudent(dataStudent)
                        temp(nama, pw)

                    case 2:
                        showStudent(dataStudent)
                    case 3:
                        showStudent(dataStudent)
                        y = True
                        while (y):
                            temp = str(input("| Masukkan ID Siswa : "))
                            idSiswa = 'STUDENT_' + temp
                            cek = isEmpty(idSiswa, dataStudent)

                            if cek:
                                break
                            else:
                                uharian1 = int(input("| Masukkan Nilai Ulangan Harian 1 Baru : "))
                                uharian2 = int(input("| Masukkan Nilai Ulangan Harian 2 Baru : "))
                                uharian3 = int(input("| Masukkan Nilai Ulangan Harian 3 Baru : "))
                                nilaiUas = int(input("| Masukkan Nilai UAS Baru              : "))
                                editNilai(dataStudent, idSiswa, uharian1, uharian2, uharian1, nilaiUas)
                                successMessage()
                                break
                    case 4:
                        showStudent(dataStudent)
                        z = True
                        while (z):
                            temp = str(input("| Masukkan ID Siswa : "))
                            idSiswa = 'STUDENT_' + temp
                            cek = isEmpty(idSiswa, dataStudent)

                            if cek:
                                break
                            else:
                                nama        = str(input("| Masukkan Nama Siswa Baru     : "))
                                password    = str(input("| Masukkan Password Siswa Baru : "))
                                editAkun(dataStudent, idSiswa, nama, password)
                                successMessage()
                                break
                    case 5:
                        showStudent(dataStudent)
                        temp = str(input("| Masukkan ID Siswa : "))
                        idSiswa = 'STUDENT_' + temp
                        cek = isEmpty(idSiswa, dataStudent)

                        if cek:
                            break
                        else:
                            hapusNilai(dataStudent, idSiswa)
                    case 6:
                        showStudent(dataStudent)
                        temp = str(input("| Masukkan ID Siswa : "))
                        idSiswa = 'STUDENT_' + temp
                        cek = isEmpty(idSiswa, dataStudent)

                        if cek:
                            break
                        else:
                            hapusAkun(dataStudent, idSiswa)
                    case 7:
                        ulanganHarian(id, dataTeacher, dataStudent)
                    case 8:
                        nextDay(dataTeacher, id)
                    case 9:
                        daftarNama = namaSiswa(dataStudent)
                        for dataStudent in daftarNama:
                            print(dataStudent)
                    case 10:
                        kkm = filterNilai(dataStudent)
                        for dataStudent in kkm:
                            print("|--------------------------")
                            print("| " + dataStudent['nama'])
                            print("| " + str(dataStudent['uas']))
                    case 11:
                        x = False
                        a = True
                    case 12:
                        exit(0)
                    case _:
                        errorMessage()
        elif pilihan == 2:
            l = True
            while (l):
                print("\n|---------------------------|")
                print("|        Opsi Student       |")
                print("|---------------------------|")
                print("| 1. Tampil Seluruh Nilai   |")
                print("| 2. Logout                 |")
                print("| 3. Keluar                 |")
                print("|---------------------------|")

                pilihan = int(input("| Masukkan Pilihan Anda : "))
                match pilihan:
                    case 1:
                        rata_rata = average(dataStudent, id)
                        infoStudent = studentInfo(dataStudent, id)
                        print("\n|----------------------------------")
                        print("| Berikut Ingfo Mengenai Anda " + infoStudent['nama'])
                        print("|----------------------------------")
                        print("| Nilai Ulangan Harian 1   : " + str(infoStudent['uh1']))
                        print("| Nilai Ulangan Harian 2   : " + str(infoStudent['uh2']))
                        print("| Nilai Ulangan Harian 3   : " + str(infoStudent['uh3']))
                        print("| Nilai UAS                : " + str(infoStudent['uas']))
                        print("| Nilai Akhir              : " + str(((((infoStudent['uh1'] + infoStudent['uh2'] +infoStudent['uh3']) / 3) + infoStudent['uas']) / 2)))
                        print("| Nilai Rata - Rata        : " + str(rata_rata))
                    case 2:
                        l = False
                        a = True
                    case 3:
                        exit(0)
                    case _:
                        errorMessage()