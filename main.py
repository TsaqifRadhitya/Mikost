import os
import function as fn
from tabulate import tabulate

os.system("cls")

def main(access_token):
    sesion_end = False
    while access_token:
        print("="*100)
        print("WELCOME TO MIKOST".center(100))
        print("="*100)
        print("[1] Masuk Sebagai User\n[2] Masuk Sebagai Admin\n[3] Masuk Sebagai Owner\n[4] Exit")
        opsi = input("Pilihan : ")
        os.system("cls")
        match opsi:
            case "1":
                parameter = True
                while parameter:
                    print("="*100)
                    print("WELCOME TO MIKOST".center(100))
                    print("="*100)
                    print("[1] Login\n[2] Register\n[3] Exit")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    match opsi:
                        case "1":
                            print("="*100)
                            print("Login".center(100))
                            print("="*100)
                            username = input("Username : ")
                            password = input("Password : ")
                            os.system("cls")
                            if fn.login_user(username, password)[0]:
                                os.system("cls")
                                main_user(True,fn.login_user(username, password)[1])
                                sesion_end = True
                                parameter = False
                            else:
                                while True:
                                    print("="*100)
                                    print("Login".center(100))
                                    print("="*100)
                                    print("Password Salah".center(100))
                                    print("[1] Retry\n[2] Exit")
                                    opsi = input("Pilihan : ")
                                    os.system("cls")
                                    match opsi:
                                        case "1":
                                            break
                                        case "2":
                                            access_token = False
                                            parameter = False
                                            break
                        case "2":
                            while True:
                                print("="*100)
                                print("Register".center(100))
                                print("="*100)
                                username = input("Username : ")
                                password = input("Password : ")
                                email = input("Email : ")
                                nama = input("Nama : ")
                                nomer_hp = input("Nomer HP : ")
                                asal = input("Asal : ")
                                print("Tekan Enter Untuk Mengisi Ulang Data")
                                print("[1] Confirm \n[2] Cancel")
                                opsi = input("Pilihan : ")
                                os.system("cls")
                                match opsi:
                                    case "1":
                                        if fn.register_user(username,password,email,nama,nomer_hp,asal):
                                            print("="*100)
                                            print("REGISTER BERHASIl".center(100))
                                            print("="*100)
                                            input("Tekan Enter Untuk Kembali")
                                            os.system("cls")
                                            break
                                        else:
                                            print("="*100)
                                            print("REGISTER GAGAL".center(100))
                                            print("="*100)
                                            input("Tekan Enter Untuk Kembali")
                                            os.system("cls")
                                            break
                                    case "2":
                                        break


                        case "3":
                            access_token = False
                            break
            case "2":
                parameter = True
                while parameter:
                    print("="*100)
                    print("WELCOME TO MIKOST".center(100))
                    print("="*100)
                    print("[1] Login\n[2] Exit")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    match opsi:
                        case "1":
                            print("="*100)
                            print("Login".center(100))
                            print("="*100)
                            username = input("Username : ")
                            password = input("Password : ")
                            os.system("cls")
                            if fn.login_admin(username, password)[0]:
                                os.system("cls")
                                main_admin(True,fn.login_admin(username, password)[1])
                                sesion_end = True
                                parameter = False
                            else:
                                while True:
                                    print("="*100)
                                    print("Login".center(100))
                                    print("="*100)
                                    print("Password Salah".center(100))
                                    print("[1] Retry\n[2] Exit")
                                    opsi = input("Pilihan : ")
                                    os.system("cls")
                                    match opsi:
                                        case "1":
                                            break
                                        case "2":
                                            access_token = False
                                            parameter = False
                                            break
                        case "2" :
                            access_token = False
                            break
            case "3":
                parameter = True
                while parameter:
                    print("="*100)
                    print("Login".center(100))
                    print("="*100)
                    username = input("Username : ")
                    password = input("Password : ")
                    os.system("cls")
                    if fn.login_owner(username, password)[0]:
                        os.system("cls")
                        main_owner(True,fn.login_owner(username, password)[1])
                        sesion_end = True
                        parameter = False
                    else:
                        while True:
                            print("="*100)
                            print("Login".center(100))
                            print("="*100)
                            print("Password Salah".center(100))
                            print("[1] Retry\n[2] Exit")
                            opsi = input("Pilihan : ")
                            os.system("cls")
                            match opsi:
                                case "1":
                                    break
                                case "2":
                                    access_token = False
                                    parameter = False
                                    break
            case "4":
                access_token = False
        if sesion_end:
            break
    else:
        print("="*100)
        print("TERIMA KASIH TELAH MENGGUNAKAN MIKOST".center(100))
        print("="*100)
        input("Tekan Enter Untuk lanjut ")
        os.system("cls")
def main_user(acces,id_user):
    while acces:
        print("="*100)
        print("MAIN MENU".center(100))
        print("="*100)
        print("[1] Tentang Kost Q-TA\n[2] Pesan Kamar\n[3] daftar Transaksi\n[4] Feedback\n[5] Exit")
        opsi = input("Pilih Menu : ")
        os.system("cls")
        match opsi:
            case "1":
                print("="*100)
                print("Tentang KOST Q-TA".center(100))
                print("="*100)
                print('''Tentukan destinasi impian Anda dengan aplikasi kami yang menyediakan kos-kosan tebaik untuk anda.
Dengan fasilitas-fasilitas modern seperti kamar yang nyaman, dapur bersama,
dan akses internet yang cepat, kami memastikan Anda mendapatkan pengalaman tinggal yang menyenangkan.
Temukan kos-kosan yang sesuai dengan preferensi Anda dengan fitur pencarian yang canggih,
lalu pesan dengan mudah melalui platform kami.''')
                print("")
                input("Tekan Enter untuk kembali ke menu awal ")
                os.system("cls")
            case "2":
                if fn.kepemilikan_kamar_user(id_user)[0]:
                    print(f"{'='*100}\n{f'ANDA TELAN MENYEWA {fn.kepemilikan_kamar_user(id_user)[1].upper()}'.center(100)}\n{'='*100}")
                    input("Tekan Enter Untuk lanjut ")
                    os.system("cls")
                else:
                    kamar = True
                    while kamar:
                        print("="*100)
                        print("Pilih Kamar".center(100))
                        print("="*100)
                        if fn.kamar_tersedia()[1]:
                            data = fn.kamar_tersedia()[0]
                            print(tabulate(data,headers=["Nomer Kamar","Nama Kamar"],tablefmt="double_grid"))
                            print("Tekan Enter Untuk Kembali")
                            opsi = input("Pilih Nomor Kamar : ")
                            os.system("cls")
                            if opsi.isnumeric():
                                if int(opsi) in [x[0] for x in data]:
                                    opsi_kamar = True
                                    while opsi_kamar:
                                        print(f"{'='*100}\n{fn.nama_kamar(int(opsi))[0].center(100)}\n{'='*100}")
                                        biodata_kamar = [x for x in fn.detail_kamar(int(opsi))]
                                        print(f"Lokasi Kamar : Lantai {biodata_kamar[1][1]}\nHarga Sewa Perbulan : Rp{biodata_kamar[1][2]}")
                                        print("Fasilitas Kamar : ")
                                        for x in biodata_kamar[0]:
                                            print(f"-{x}")
                                        fk_kamar = int(opsi)
                                        harga = int(biodata_kamar[1][2])
                                        print("[1] Pesan Kamar \n[2] Exit")
                                        ops = input("Pilihan : ")
                                        os.system("cls")
                                        match ops:
                                            case "1":
                                                jenis_pembayaran_loop = True
                                                while jenis_pembayaran_loop:
                                                    print(f"{'='*100}\n{'Jenis Pembayaran'.center(100)}\n{'='*100}")
                                                    print("[1] Transfer Bank\n[2] E-Wallet\n[3] Exit")
                                                    opsi = input("Pilihan : ")
                                                    os.system("cls")
                                                    match opsi:
                                                        case "1":
                                                            bank_session = True
                                                            while bank_session:
                                                                print(f"{'='*100}\n{'Metode Transfer Bank'.center(100)}\n{'='*100}")
                                                                print(tabulate(fn.bank(),headers=["Nomor Bank","Bank"],tablefmt="double_grid"))
                                                                print("Tekan Enter Untuk Kembali")
                                                                opsi = input("Pilihan : ")
                                                                os.system("cls")
                                                                if opsi.isnumeric():
                                                                    if int(opsi) in [x[0] for x in fn.bank()]:
                                                                        fk_bank = int(opsi)
                                                                        nama_bank = [x[1] for x in fn.bank() if x[0] == fk_bank][0]
                                                                        Biodata_session = True
                                                                        while Biodata_session:
                                                                            print(f"{'='*100}\n{f'Biodata Metode Pembayaran {nama_bank}'.center(100)}\n{'='*100}")
                                                                            nama = input(f"Nama Pemilik Akun {nama_bank} : ")
                                                                            nomor = input(f"Nomor {nama_bank} : ")
                                                                            print("Tekan Enter Untuk Mengisi Ulang Data")
                                                                            print("[1] Lanjutkan Transaksi\n[2] Batalkan Transaksi")
                                                                            opsi = input("Pilihan : ")
                                                                            os.system("cls")
                                                                            match opsi:
                                                                                case "1":
                                                                                    invoices = True
                                                                                    while invoices:
                                                                                        print(f"{'='*100}\n{'DETAIL TRANSAKSI'.center(100)}\n{'='*100}")
                                                                                        print(f"Kamar yang disewa : {fn.nama_kamar(fk_kamar)[0]}\nMetode Pembayaran : {nama_bank}\nNomor Rekening : {nomor}\nNama Pemilik Rekening : {nama}\nHarga : {harga}")
                                                                                        print("[1] Lanjutkan Transaksi\n[2] Batalkan Transaksi")
                                                                                        opsi = input("Pilihan : ")
                                                                                        os.system("cls")
                                                                                        match opsi:
                                                                                            case "1":
                                                                                                if fn.transaksi_bank(id_user,fk_bank,fk_kamar,harga,nomor,nama):
                                                                                                    print(f"{'='*100}\n{'TRANSAKSI BERHASIL'.center(100)}\n{'='*100}")
                                                                                                else:
                                                                                                    print(f"{'='*100}\n{'TRANSAKSI GAGAL'.center(100)}\n{'='*100}")
                                                                                                input("Tekan Enter Untuk Kembali")
                                                                                                os.system("cls")
                                                                                                kamar,opsi_kamar,bank_session,Biodata_session,jenis_pembayaran_loop = False,False, False, False,False
                                                                                                break
                                                                                            case "2":
                                                                                                kamar,opsi_kamar,bank_session,Biodata_session,jenis_pembayaran_loop = False,False, False, False,False
                                                                                                break

                                                                                case "2":
                                                                                    kamar,opsi_kamar,bank_session,Biodata_session,jenis_pembayaran_loop = False,False, False, False,False
                                                                else:
                                                                    kamar,opsi_kamar,bank_session,jenis_pembayaran_loop = False, False, False,False
                                                        case "2":
                                                            E_wallet_Session = True
                                                            while E_wallet_Session:
                                                                print(f"{'='*100}\n{'Metode E-Wallet'.center(100)}\n{'='*100}")
                                                                print(tabulate(fn.E_wallet(),headers=["Nomor E-Wallet","E-Wallet"],tablefmt="double_grid"))
                                                                print("Tekan Enter Untuk Kembali")
                                                                opsi = input("Pilihan : ")
                                                                os.system("cls")
                                                                if opsi.isnumeric():
                                                                    if int(opsi) in [x[0] for x in fn.E_wallet()]:
                                                                        fk_E_wallet = int(opsi)
                                                                        nama_E_wallet = [x[1] for x in fn.E_wallet() if x[0] == fk_E_wallet][0]
                                                                        Biodata_session = True
                                                                        while Biodata_session:
                                                                            print(f"{'='*100}\n{f'Biodata Metode Pembayaran {nama_E_wallet}'.center(100)}\n{'='*100}")
                                                                            nama = input(f"Nama Pemilik Akun {nama_E_wallet} : ")
                                                                            nomor = input(f"Nomor {nama_E_wallet} : ")
                                                                            print("Tekan Enter Untuk Mengisi Ulang Data")
                                                                            print("[1] Lanjutkan Transaksi\n[2] Batalkan Transaksi")
                                                                            opsi = input("Pilihan : ")
                                                                            os.system("cls")
                                                                            match opsi:
                                                                                case "1":
                                                                                    invoices = True
                                                                                    while invoices:
                                                                                        print(f"{'='*100}\n{'DETAIL TRANSAKSI'.center(100)}\n{'='*100}")
                                                                                        print(f"Kamar yang disewa : {fn.nama_kamar(fk_kamar)[0]}\nMetode Pembayaran : {nama_E_wallet}\nNomor {nama_E_wallet} : {nomor}\nNama Pemilik {nama_E_wallet} : {nama}\nHarga : {harga}")
                                                                                        print("[1] Lanjutkan Transaksi\n[2] Batalkan Transaksi")
                                                                                        opsi = input("Pilihan : ")
                                                                                        os.system("cls")
                                                                                        match opsi:
                                                                                            case "1":
                                                                                                if fn.transaksi_e_wallet(id_user,fk_E_wallet,fk_kamar,harga,nomor,nama):
                                                                                                    print(f"{'='*100}\n{'TRANSAKSI BERHASIL'.center(100)}\n{'='*100}")
                                                                                                else:
                                                                                                    print(f"{'='*100}\n{'TRANSAKSI GAGAL'.center(100)}\n{'='*100}")
                                                                                                input("Tekan Enter Untuk Kembali")
                                                                                                os.system("cls")
                                                                                                kamar,opsi_kamar,E_wallet_Session,Biodata_session,jenis_pembayaran_loop = False,False, False, False,False
                                                                                                break
                                                                                            case "2":
                                                                                                kamar,opsi_kamar,E_wallet_Session,Biodata_session,jenis_pembayaran_loop = False,False, False, False,False

                                                                                case "2":
                                                                                    kamar,opsi_kamar,E_wallet_Session,Biodata_session,jenis_pembayaran_loop = False,False, False, False,False
                                                                else:
                                                                    kamar,opsi_kamar,E_wallet_Session ,jenis_pembayaran_loop= False, False, False,False
                                                        case "3":
                                                            jenis_pembayaran_loop = False
                                                            opsi_kamar = False
                                                            kamar = False
                                            case "2":
                                                opsi_kamar = False
                                                kamar = False
                                else:
                                    print("="*100)
                                    print("Kamar Tidak Tersedia".center(100))
                                    print("="*100)
                                    input("Tekan Enter Untuk Kembali")
                                    os.system("cls")
                            else:
                                if opsi == "":
                                    kamar = False
                                else:
                                    print("="*100)
                                    print("Masukkan Nomor Kamar dengan Benar".center(100))
                                    print("="*100)
                                    input("Tekan Enter Untuk Kembali")
                                    os.system("cls")
            case "3":
                print(f"{'='*100}\n{'DAFTAR TRANSAKSI'.center(100)}\n{'='*100}")
                print(tabulate(fn.daftar_transaksi_user(id_user),headers=["Tanggal","Kamar","Nominal","Status Pembayaran"],tablefmt="double_grid"))
                input("Tekan Enter untuk kembali ke menu awal")
                os.system("cls")
            case "4":
                print(f"{'='*100}\n{'FEEDBACK'.center(100)}\n{'='*100}")
                print("Tekan Enter Untuk Kembali")
                feed_back = input("Isi Feedback : ")
                os.system("cls")
                if feed_back == "":
                    pass
                else:
                    while True:
                        print(f"{'='*100}\n{'FEEDBACK'.center(100)}\n{'='*100}")
                        print(f"Isi Feedback : {feed_back}")
                        print("[1] Kirim Feedback\n[2] Batalkan")
                        opsi = input("Pilihan : ")
                        os.system("cls")
                        match opsi:
                            case "1":
                                if fn.tambah_feedback(id_user,feed_back):
                                    print(f"{'='*100}\n{'FEEDBACK BERHASIL DIKIRIM'.center(100)}\n{'='*100}")
                                    input("Tekan Enter Untuk Kembali")
                                    os.system("cls")
                                    break
                                else:
                                    print(f"{'='*100}\n{'FEEDBACK GAGAL DIKIRIM'.center(100)}\n{'='*100}")
                                    input("Tekan Enter Untuk Kembali")
                                    os.system("cls")
                                    break
                            case "2":
                                break
                os.system("cls")
            case "5":
                acces = False
    else:
        print("="*100)
        print("TERIMA KASIH TELAH MENGGUNAKAN MIKOST".center(100))
        print("="*100)
        input("Tekan Enter Untuk lanjut ")
        os.system("cls")

def main_admin(access,id_admin):
    while access:
        print("="*100)
        print("MAIN MENU".center(100))
        print("="*100)
        print("[1] Biaya Perawatan\n[2] Kelola Kamar\n[3] Transaksi\n[4] Feedback\n[5] Karyawan\n[6] Exit")
        opsi = input("Pilih Menu : ")
        os.system("cls")
        match opsi:
            case "1":
                Keuangan = True
                while Keuangan:
                    print(f"{'='*100}\n{'PENGELUARAN BULANA KOST Q-TA'.center(100)}\n{'='*100}")
                    print(tabulate(fn.keuangan_admin("Bulanan"),headers=["Tanggal","Tagihan Air","Tagihan Listrik","Tagihan Wifi","Total"],tablefmt="double_grid"))
                    print("[1] Tambah Pengeluaran Baru\n[2] Exit")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    match opsi:
                        case "1":
                            while True:
                                print(f"{'='*100}\n{'MASUKKAN PENGELUARAN BULAN INI'.center(100)}\n{'='*100}")
                                air = input("Tagihan Air : ")
                                listrik = input("Tagihan Listrik : ")
                                wifi = input("Tagihan Wifi : ")
                                print("Tekan Enter Untuk Batalkan")
                                print("[1] Kirim Data\n[2] Ulangi Pengisian Data")
                                opsi = input("Pilihan : ")
                                os.system("cls")
                                match opsi:
                                    case "1":
                                        if fn.tambah_biaya_bulanan(id_admin,air,listrik,wifi):
                                            print(f"{'='*100}\n{'INPUT DATA PENGELUARAN BULANAN BERHASIL'.center(100)}\n{'='*100}")
                                            input("Tekan Enter Untuk Batalkan")
                                            os.system("cls")
                                            break
                                        else:
                                            print(f"{'='*100}\n{'INPUT DATA PENGELUARAN BULANAN GAGAL'.center(100)}\n{'='*100}")
                                            input("Tekan Enter Untuk Batalkan")
                                            os.system("cls")
                                            break
                                    case "2":
                                        pass
                                    case default:
                                        break
                                os.system("cls")
                        case "2":
                            Keuangan = False
            case "2":
                data_penghuni =True
                while data_penghuni:
                    print("="*100)
                    print("KAMAR KOST Q-TA".center(100))
                    print("="*100)
                    data = fn.semua_kamar()
                    print(tabulate(data,headers=["Nomor Kamar","Nama Kamar","Lantai"],tablefmt="double_grid"))
                    print("Tekan Enter Untuk Kembali")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    if opsi.isnumeric():
                        if int(opsi) in [x[0] for x in data]:
                            penghuni = [x for x in fn.daftar_penghuni_owner(int(opsi))]
                            fk_kamar = int(opsi)
                            nama_kamar = [x[1] for x in data if x[0] == fk_kamar][0]
                            status_kamar = fn.status_kamar(int(opsi))
                            if status_kamar == "Terisi":
                                status_kamar = "Tidak Muncul di Marketplace"
                                kamar_sessions = True
                                while kamar_sessions:
                                    if penghuni[0]:
                                        header = f"DATA PENGHUNI {penghuni[1][3].upper()}"
                                        print(f"{'='*100}\n{header.center(100)}\n{'='*100}")
                                        print(f"Nama : {penghuni[1][0]}\nNomer HP : {penghuni[1][1]}\nAsal : {penghuni[1][2]}")
                                        print(f"Status Kamar : {status_kamar}")
                                        print("[1] Munculkan diMarket Place\n[2] Exit")
                                        opsi = input("Pilihan")
                                        os.system("cls")
                                        match opsi:
                                            case "1":
                                                fn.update_status_kamar(fk_kamar)
                                                print(f"{'='*100}\n{f'{nama_kamar} BERHASIL DIMUNCULKAN DI MARKETPLACE'.center(100)}\n{'='*100}")
                                                input("Tekan Enter Untuk Kembali ")
                                                os.system("cls")
                                                kamar_sessions,data_penghuni = False,False
                                            case "2":
                                                kamar_sessions,data_penghuni = False,False
                                    else:
                                        header = f"DATA PENGHUNI {fn.nama_kamar(int(opsi))[0].upper()}"
                                        print(f"{'='*100}\n{header.center(100)}\n{'='*100}\nBelum ada Penghuni")
                                        print(f"Status Kamar : {status_kamar}")
                                        print("[1] Munculkan diMarket Place\n[2] Exit")
                                        opsi = input("Pilihan")
                                        os.system("cls")
                                        match opsi:
                                            case "1":
                                                fn.update_status_kamar(fk_kamar)
                                                print(f"{'='*100}\n{f'{nama_kamar} BERHASIL DIMUNCULKAN DI MARKETPLACE'.center(100)}\n{'='*100}")
                                                input("Tekan Enter Untuk Kembali ")
                                                os.system("cls")
                                                kamar_sessions,data_penghuni = False,False
                                            case "2":
                                                kamar_sessions,data_penghuni = False,False
                            else:
                                status_kamar = "Muncul di Market Place"
                                if penghuni[0]:
                                    header = f"DATA PENGHUNI {penghuni[1][3].upper()}"
                                    print(f"{'='*100}\n{header.center(100)}\n{'='*100}")
                                    print(f"Nama : {penghuni[1][0]}\nNomer HP : {penghuni[1][1]}\nAsal : {penghuni[1][2]}")
                                    print(f"Status Kamar : {status_kamar}")
                                    input("Tekan Enter Untuk Kembali")
                                    os.system("cls")
                                else:
                                    header = f"DATA PENGHUNI {fn.nama_kamar(int(opsi))[0].upper()}"
                                    print(f"{'='*100}\n{header.center(100)}\n{'='*100}\nBelum ada Penghuni")
                                    print(f"Status Kamar : {status_kamar}")
                                    input("Tekan Enter Untuk Kembali")
                                    os.system("cls")
                    else:
                        if opsi == "":
                            data_penghuni = False
            case "3":
                transaksi_session = True
                while transaksi_session:
                    print(f"{'='*100}\n{'DAFTAR TRANSAKSI MIKOST'.center(100)}\n{'='*100}")
                    print(tabulate(fn.transaksi_owner(),headers=["Nomor Transaksi","Tanggal","Nama","Kamar","Nominal","Metode Pembayaran"],tablefmt="double_grid"))
                    print("[1] Verifikasi Pembayaran\n[2] Exit")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    match opsi:
                        case "1":
                            data_transaksi_baru = [x for x in fn.transaksi_baru()]
                            if data_transaksi_baru[0]:
                                verifikasi_session = True
                                while verifikasi_session:
                                    print(f"{'='*100}\n{'VERIFIKASI TRANSAKSI'.center(100)}\n{'='*100}")
                                    print(tabulate(data_transaksi_baru[1],headers=["Nomor Transaksi","Tanggal","Nama","Kamar","Nominal","Metode Pembayaran"],tablefmt="double_grid"))
                                    print("Tekan Enter Untuk Kembali")
                                    opsi = input("Masukkan Nomor Transaksi : ")
                                    os.system("cls")
                                    if opsi.isnumeric():
                                        if int(opsi) in [x[0] for x in data_transaksi_baru[1]]:
                                            if [x[5] for x in data_transaksi_baru[1] if x[0] == int(opsi)][0] == "Bank":
                                                data_transaksi = fn.keuangan_owner("BANK",int(opsi))
                                            else:
                                                data_transaksi = fn.keuangan_owner("E-Wallet",int(opsi))
                                            detail_session = True
                                            fk_transaksi = int(opsi)
                                            while detail_session:
                                                print(f"{'='*100}\n{'DETAIL TRANSAKSI'.center(100)}\n{'='*100}")
                                                print(f"Tanggal Transaksi : {data_transaksi[0]}\nNama : {data_transaksi[1]}\nKamar yang disewa : {data_transaksi[2]}\nNominal Pembayarana : {data_transaksi[3]}\nMetode Pembayaran : {data_transaksi[4]}\nNama Pemilik : {data_transaksi[5]}\nNomor {data_transaksi[4]} : {data_transaksi[6]}")
                                                print("[1] Konfirmasi Transaksi\n[2] Batalkan Transaksi\n[3] Exit")
                                                opsi = input("Pilihan : ")
                                                os.system("cls")
                                                match opsi:
                                                    case "1":
                                                        fn.acc_transaksi(fk_transaksi,data_transaksi[2])
                                                        print(f"{'='*100}\n{'KONFIRMASI TRANSAKSI BERHASIL'.center(100)}\n{'='*100}")
                                                        input("Tekan Enter Untuk Kembali ")
                                                        os.system("cls")
                                                        detail_session,verifikasi_session,transaksi_session = False,False,False
                                                    case "2":
                                                        fn.tolak_transaksi(fk_transaksi)
                                                        print(f"{'='*100}\n{'PEMBATALAN TRANSAKSI BERHASIL'.center(100)}\n{'='*100}")
                                                        input("Tekan Enter Untuk Kembali ")
                                                        os.system("cls")
                                                        detail_session,verifikasi_session,transaksi_session = False,False,False
                                                    case "3":
                                                        detail_session,verifikasi_session,transaksi_session = False,False,False
                                                        
                                                
                                    else:
                                        if opsi == "":
                                            verifikasi_session = False

                            else:
                                print(f"{'='*100}\n{'BELUM ADA TRANSAKSI BARU'.center(100)}\n{'='*100}")
                                input("Tekan Enter Untuk Kembali")
                                os.system("cls")
                        case "2":
                            transaksi_session = False
            case "4":
                print("="*100)
                print("Feedback Penghuni KOST Q-TA".center(100))
                print("="*100)
                print(tabulate(fn.tampilkan_feedback(),headers=["Tanggal","Feedback","Nama Pengirim"],tablefmt="double_grid"))
                input("Tekan Enter Untuk Kembali")
                os.system("cls")
            case "5":
                fitur = True
                while fitur:
                    print("="*100)
                    print("Karyawan".center(100))
                    print("="*100)
                    data_karyawan = fn.daftar_karyawan("Admin")
                    print(tabulate(data_karyawan,headers=["Nomer Karyawan","Nama Karyawan","Nomer HP","Alamat"],tablefmt="double_grid"))
                    print("[1] Tambah Karyawan\n[2] Hapus Karyawan\n[3] Kembali")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    match opsi:
                        case "1":
                            while True: 
                                print(f"{'='*100}\n{'TAMBAH KARYAWAN BARU'.center(100)}\n{'='*100}")
                                nama = input("Nama Karyawan : ")
                                HP = input("Nomor HP : ")
                                alamat = input("Alamat : ")
                                print("Tekan Enter Untuk Mengisi Ulang Data")
                                print("[1] Confirm \n[2] Cancel")
                                opsi = input("Pilihan : ")
                                os.system("cls")
                                match opsi:
                                    case "1":
                                        if fn.tambah_karyawan(id_admin,nama,HP,alamat):
                                            print("="*100)
                                            print("PENAMBAHAN KARYAWAN BERHASIl".center(100))
                                            print("="*100)
                                            input("Tekan Enter Untuk Kembali")
                                            os.system("cls")
                                            break
                                        else:
                                            print("="*100)
                                            print("PENAMBAHAN KARYAWAN GAGAL".center(100))
                                            print("="*100)
                                            input("Tekan Enter Untuk Kembali")
                                            os.system("cls")
                                            break
                                    case "2":
                                        break
                        case "2":
                            while True:
                                print(f"{'='*100}\n{'HAPUS DATA KARYAWAN'.center(100)}\n{'='*100}")
                                print(tabulate(data_karyawan,headers=["Nomer Karyawan","Nama Karyawan","Nomer HP","Alamat"],tablefmt="double_grid"))
                                print("Tekan Enter Untuk Kembali")
                                opsi = input("Nomor Karyawan : ")
                                os.system("cls")
                                if opsi.isnumeric():
                                    if int(opsi) in [x[0] for x in data_karyawan]:
                                        nama_karyawan = [x[1] for x in data_karyawan if x[0] == int(opsi)][0]
                                        fn.hapus_karyawan(int(opsi))
                                        print(f"{'='*100}\n{f'{nama_karyawan} BERHASIL DIHAPUS DARI DAFTAR KARYAWAN'.center(100)}\n{'='*100}")
                                        input("Tekan Enter Untuk Kembali")
                                        os.system("cls")
                                        break

                                else:
                                    if opsi == "":
                                        break
                        case "3":
                            fitur = False
            case "6":
                access = False
    else:
        print("="*100)
        print("TERIMA KASIH TELAH MENGGUNAKAN MIKOST".center(100))
        print("="*100)
        input("Tekan Enter Untuk lanjut ")
        os.system("cls")

def main_owner(access,id_owner):
    while access:
        print("="*100)
        print("MAIN MENU".center(100))
        print("="*100)
        print("[1] Keuangan\n[2] Karyawan\n[3] Penghuni Kamar\n[4] Feedback\n[5] Admin\n[6] Exit")
        opsi = input("Pilih Menu : ")
        os.system("cls")
        match opsi:
            case "1":
                fitur = True
                while fitur:
                    print("="*100)
                    print("KEUANGAN MIKOST".center(100))
                    print("="*100)
                    print("[1] Daftar Transaksi\n[2] Daftar Pengeluaran Bulanan\n[3] Harga Sewa Kamar\n[4] Kembali")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    match opsi:
                        case "1":
                            while True:
                                print("="*100)
                                print("Daftar Transaksi MIKOST".center(100))
                                print("="*100)
                                data = fn.transaksi_owner()
                                print(tabulate(data,headers=["Nomor Transaksi","Tanggal","Nama","Kamar","Nominal","Metode Pembayaran"],tablefmt="double_grid"))
                                print("Tekan Enter Untuk Kembali")
                                opsi = input("Nomor Transaksi : ")
                                os.system("cls")
                                if opsi.isnumeric():
                                    if int(opsi) in [x[0] for x in data]:
                                        if [x[-1] for x in data if x[0] == int(opsi)][0] == "Bank":
                                            detail = fn.keuangan_owner("BANK",int(opsi))
                                            print("="*100)
                                            print("Detail Transaksi".center(100))
                                            print("="*100)
                                            print(f"Tanggal Transaksi : {detail[0]}\nNama Penghuni : {detail[1]}\nKamar yang disewa : {detail[2]}\nMetode Pembayaran : {detail[4]}\nRekening Bank {detail[4]} : {detail[-1]}\nNama Pemilik Rekening : {detail[5]}\nNominal : {detail[3]}")
                                            input("Tekan Enter Untuk Kembali")
                                            os.system("cls")
                                        else:
                                            detail = fn.keuangan_owner("E-Wallet",int(opsi))
                                            print("="*100)
                                            print("Detail Transaksi".center(100))
                                            print("="*100)
                                            print(f"Tanggal Transaksi : {detail[0]}\nNama Penghuni : {detail[1]}\nKamar yang disewa : {detail[2]}\nMetode Pembayaran : {detail[4]}\nNomor {detail[4]} : {detail[-1]}\nNama Pemilik {detail[4]} : {detail[5]}\nNominal : {detail[3]}")
                                            input("Tekan Enter Untuk Kembali")
                                            os.system("cls")
                                else:
                                    if opsi == "":
                                        break

                        case "2":
                            print("="*100)
                            print("Daftar Pengeluaran Bulanan MIKOST".center(100))
                            print("="*100)
                            print(tabulate(fn.keuangan_owner("Pegeluaran"),headers=["Penanggung Jawab","Tanggal","Tagihan Air","Tagihan Listrik","Tagihan WIFI","Total Tagihan"],tablefmt="double_grid"))
                            input("Tekan Enter Untuk Kembali")
                            os.system("cls")
                        case "3":
                            cek_harga = True
                            while cek_harga:
                                print(f"{'='*100}\n{'HARGA SEWA KAMAR KOST Q-TA'.center(100)}\n{'='*100}\nHarga Sewa : {fn.kelola_harga_kamar('lihat')}")
                                print("[1] Rubah Harga\n[2] Exit")
                                opsi = input("Pilihan : ")
                                os.system("cls")
                                match opsi:
                                    case "1":
                                        print(f"{'='*100}\n{'MASUKKAN HARGA SEWA BARU'.center(100)}\n{'='*100}")
                                        harga = input("Harga : ")
                                        os.system("cls")
                                        if fn.kelola_harga_kamar("edit",harga):
                                            print(f"{'='*100}\n{'BERHASIL MEMPERBARUI HARGA SEWA'.center(100)}\n{'='*100}")
                                            input("Enter Untuk Kembali ")
                                            os.system("cls")
                                        else:
                                            print(f"{'='*100}\n{'GAGAL MEMPERBARUI HARGA SEWA'.center(100)}\n{'='*100}")
                                            input("Enter Untuk Kembali ")
                                            os.system("cls")
                                    case "2":
                                        cek_harga = False
                        case "4":
                            fitur = False
            case "2":
                print("="*100)
                print("Karyawan KOST Q-TA".center(100))
                print("="*100)
                print(tabulate(fn.daftar_karyawan("Owner"),headers=["Nama Karyawan","Nomer HP","Alamat","Penambah Karyawan"],tablefmt="double_grid"))
                input("Tekan Enter Untuk Kembali")
                os.system("cls")
            case "3":
                data_penghuni =True
                while data_penghuni:
                    print("="*100)
                    print("KAMAR KOST Q-TA".center(100))
                    print("="*100)
                    data = fn.semua_kamar()
                    print(tabulate(data,headers=["Nomor Kamar","Nama Kamar","Lantai"],tablefmt="double_grid"))
                    print("Tekan Enter Untuk Kembali")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    if opsi.isnumeric():
                        if int(opsi) in [x[0] for x in data]:
                            penghuni = [x for x in fn.daftar_penghuni_owner(int(opsi))]
                            if penghuni[0]:
                                header = f"DATA PENGHUNI {penghuni[1][3].upper()}"
                                print(f"{'='*100}\n{header.center(100)}\n{'='*100}")
                                print(f"Nama : {penghuni[1][0]}\nNomer HP : {penghuni[1][1]}\nAsal : {penghuni[1][2]}")
                                input("Tekan Enter Untuk Kembali")
                                os.system("cls")
                            else:
                                header = f"DATA PENGHUNI {fn.nama_kamar(int(opsi))[0].upper()}"
                                print(f"{'='*100}\n{header.center(100)}\n{'='*100}\nBelum ada Penghuni")
                                input("Tekan Enter Untuk Kembali")
                                os.system("cls")
                    else:
                        if opsi == "":
                            data_penghuni = False
            case "4":
                print("="*100)
                print("Feedback Penghuni KOST Q-TA".center(100))
                print("="*100)
                print(tabulate(fn.tampilkan_feedback(),headers=["Tanggal","Feedback","Nama Pengirim"],tablefmt="double_grid"))
                input("Tekan Enter Untuk Kembali")
                os.system("cls")
            case "5":
                admin = True
                while admin:
                    print("="*100)
                    print("Admin MIKOST".center(100))
                    print("="*100)
                    data_admin = fn.daftar_admin()
                    print(tabulate(data_admin,headers=["Nomor Admin","Nama","Nomor Telepon","Status Admin"],tablefmt="double_grid"))
                    print("[1] Tambah Admin\n[2] Nonaktifkan Akun Admin\n[3] Exit")
                    opsi = input("Pilihan : ")
                    os.system("cls")
                    match opsi:
                        case "1":
                            register = True
                            while register:
                                print(f"{'='*100}\n{'TAMBAH ADMIN'.center(100)}\n{'='*100}")
                                username = input("Username : ")
                                password = input("Password : ")
                                nama = input("Nama : ")
                                hp = input("Nomer HP : ")
                                print("Tekan Enter Untuk Mengulangi Pengisian")
                                print("[1] Proses\n[2] Batalkan")
                                opsi = input("Pilihan : ")
                                os.system("cls")
                                match opsi: 
                                    case "":
                                        pass
                                    case "1":
                                        if fn.tambah_admin(username,password,nama,hp):
                                            print(f"{'='*100}\n{'PENAMBAHAN ADMIN BERHASIL'.center(100)}\n{'='*100}")
                                            input("Tekan Enter Untuk Kembali")
                                            os.system("cls")
                                            register = False
                                        else:
                                            print(f"{'='*100}\n{'PENAMBAHAN ADMIN GAGAL'.center(100)}\n{'='*100}")
                                            input("Tekan Enter Untuk Kembali")
                                            os.system("cls")
                                            register = False
                                    case "2":
                                        register = False
                        case "2":
                            while True:
                                print(f"{'='*100}\n{'NONAKTIFKAN AKUN ADMIN'.center(100)}\n{'='*100}")
                                print(tabulate(data_admin,headers=["Nomor Admin","Nama","Nomor Telepon","Status Admin"],tablefmt="double_grid"))
                                print("Tekan Enter Untuk Kembali")
                                opsi = input("Nomor Akun : ")
                                os.system("cls")
                                if opsi.isnumeric():
                                    if int(opsi) in [x[0] for x in data_admin]:
                                        fn.non_aktifkan_admin(int(opsi))
                                        nama_admin = [x[1] for x in data_admin if x[0] == int(opsi)][0]
                                        print(f"{'='*100}\n{f'AKUN {nama_admin} BERHASIL DINONAKTIFKAN'.center(100)}\n{'='*100}")
                                        input("Tekan Enter Untuk Kembali")
                                        os.system("cls")
                                        break
                                else:
                                    if opsi == "":
                                        break
                                        
                        case "3":
                            admin = False
            case "6":
                access = False
    else:
        print("="*100)
        print("TERIMA KASIH TELAH MENGGUNAKAN MIKOST".center(100))
        print("="*100)
        input("Tekan Enter Untuk lanjut ")
        os.system("cls")
main(True)