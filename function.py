import psycopg2

host_name = 'localhost'
data_base = 'backup'
username = 'postgres'
pw = ''
port = 5432

def login_user(user,password):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"select u.user_id,a.username,a.password from akun a Join Pelanggan u ON a.akun_id = u.akun_akun_id where a.username= '{user}'"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    if data == []:
        return False,None
    else:
        data = [x for x in data[0]]
        if password == data[2] :
            return True,data[0]
        else:
            return False,None
        
def login_admin(user,password):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"select u.admin_id,a.username,a.password from akun a Join Admin u ON a.akun_id = u.akun_akun_id where a.username= '{user}'"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    if data == []:
        return False,None
    else:
        data = [x for x in data[0]]
        if password == data[2] :
            return True,data[0]
        else:
            return False,None
def login_owner(user,password):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"select u.owner_id,a.username,a.password from akun a Join Owner u ON a.akun_id = u.akun_akun_id where a.username= '{user}'"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    if data == []:
        return False,None
    else:
        data = [x for x in data[0]]
        if password == data[2] :
            return True,data[0]
        else:
            return False,None
def register_user(user, password,email,nama,Nomer_HP,Asal,jenis_akun='User'):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    try:
        sql = f"INSERT INTO akun(username,password,jenis_akun) VALUES ('{user}', '{password}','{jenis_akun}')"
        navigate.execute(sql)
        open_db.commit()
        sql = "select akun_id from akun order by akun_id DESC limit 1"
        navigate.execute(sql)
        id_akun = int(navigate.fetchall()[0][0])
        try:
            sql = f"INSERT INTO Pelanggan(email,nama,nomer_hp,asal,akun_akun_id) VALUES ('{email}', '{nama}','{Nomer_HP}','{Asal}',{id_akun})"
            navigate.execute(sql)
            open_db.commit()
            open_db.close()
            return True
        except:
            sql = f"DELETE FROM Akun WHERE akun_id = {id_akun}"
            navigate.execute(sql)
            open_db.commit()
            open_db.close()
            return False
    except:
        open_db.close()
        return False

def tambah_admin(user,password,nama,Nomer_HP,jenis_akun='Admin'):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    try:
        sql = f"INSERT INTO akun(username,password,jenis_akun) VALUES ('{user}', '{password}','{jenis_akun}')"
        navigate.execute(sql)
        open_db.commit()
        sql = "select akun_id from akun order by akun_id DESC limit 1"
        navigate.execute(sql)
        id_akun = int(navigate.fetchall()[0][0])
        try:
            sql = f"INSERT INTO Admin(nama,no_telp,akun_akun_id) VALUES ('{nama}','{Nomer_HP}',{id_akun})"
            navigate.execute(sql)
            open_db.commit()
            open_db.close()
            return True
        except:
            sql = f"DELETE FROM Akun WHERE akun_id = {id_akun}"
            navigate.execute(sql)
            open_db.commit()
            open_db.close()
            return False
    except:
        open_db.close()
        return False

def kamar_tersedia():
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"SELECT kamar_id as nomer_kamar,nama_kamar as kamar FROM kamar WHERE status_kamar = 'Kosong'"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    data = [[x for x in x] for x in data]
    if kamar_tersedia == []:
        return data,False
    else:
        return [data,True]

def tampilkan_feedback():
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql_1 = "SELECT TO_CHAR(f.tanggal,'dd-mm-yyyy') as Tanggal,f.isi_feedback,P.nama FROM Feedback f Join Pelanggan P ON f.user_user_id = P.user_id order by f.tanggal DESC"
    navigate.execute(sql_1)
    data = navigate.fetchall()
    open_db.close()
    data = [[x for x in x] for x in data]
    return data

def daftar_karyawan(sebagai):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    if sebagai == "Admin":
        sql = "SELECT nama,no_telp,alamat FROM karyawan"
    else:
        sql = 'select k.nama,k.no_telp,k.alamat,a.nama as "Penambah Karyawan" from karyawan k JOIN admin a ON a.admin_id = k.admin_admin_id'
    navigate.execute(sql)
    data = [[x for x in x] for x in navigate.fetchall()]
    open_db.close()
    return data

def daftar_admin():
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = "SELECT nama,no_telp FROM Admin"
    navigate.execute(sql)
    data = [[x for x in x ] for x in navigate.fetchall()]
    open_db.close()
    return data

def keuangan_owner(jenis,id=None):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    if jenis == "BANK":
        sql = f"select to_char(t.tanggal,'dd-mm-yyyy'),P.nama,K.nama_kamar,T.nominal,B.nama_bank,PB.nama_pemilik,PB.no_rekening from Pelanggan P JOIN Transaksi T ON P.user_id = T.user_user_id JOIN kamar k ON k.kamar_id = T.kamar_kamar_id JOIN metode_pembayaran M ON t.metode_pembayaran_id = M.metode_pembayaran_id JOIN pembayaran_bank PB ON M.metode_pembayaran_id = PB.metode_pembayaran_id JOIN bank B ON B.bank_id = PB.bank_id where t.transaksi_id = {id}"
        navigate.execute(sql)
        data = [x for x in navigate.fetchall()[0]]
    elif jenis == "E-Wallet":
        sql = f"select to_char(t.tanggal,'dd-mm-yyyy'),P.nama,K.nama_kamar,T.nominal,e.nama_ewallet,pe.nama_pemilik,Pe.nomor_ewallet from Pelanggan P JOIN Transaksi T ON P.user_id = T.user_user_id JOIN kamar k ON k.kamar_id = T.kamar_kamar_id JOIN metode_pembayaran M ON t.metode_pembayaran_id = M.metode_pembayaran_id JOIN pembayaran_ewallet Pe ON M.metode_pembayaran_id = Pe.metode_pembayaran_id JOIN ewallet e ON e.ewallet_id = pe.ewallet_id where t.transaksi_id = {id} "
        navigate.execute(sql)
        data = [x for x in navigate.fetchall()[0]]
    else:
        sql = "select a.nama,to_char(p.tanggal,'dd-mm-yyyy'),p.pengeluaran_air,p.pengeluaran_listrik,p.pengeluaran_wifi,(p.pengeluaran_air+p.pengeluaran_listrik+p.pengeluaran_wifi) as Total from pengeluaran p JOIN admin a ON a.admin_id = p.admin_admin_id order by p.tanggal DESC"
        navigate.execute(sql)
        data = [[x for x in x ] for x in navigate.fetchall()]
    open_db.close()
    return data

print(keuangan_owner("E-Wallet",5))

def keuangan_admin(jenis):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    if jenis == "Bulanan":
        sql = "select to_char(tanggal,'dd-mm-yyy'),pengeluaran_air,pengeluaran_listrik,pengeluaran_wifi,(pengeluaran_air + pengeluaran_listrik + pengeluaran_wifi) as Total from pengeluaran order by tanggal DESC"
    elif jenis == "E-Wallet":
        pass
    elif jenis == "Bank":
        pass
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    return data

def daftar_penghuni_owner(id_kamar):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql =  f"select P.nama,P.nomer_hp,P.asal,K.nama_kamar from Pelanggan P join Transaksi T ON P.user_id = T.user_user_id JOIN Kamar K ON K.kamar_id = T.kamar_kamar_id where k.status_kamar = 'Terisi' and extract(month from age(now(),T.tanggal)) < 1 and k.kamar_id = {id_kamar} order by t.tanggal DESC limit 1"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    data = [[x for x in x] for x in data]
    if data == []:
        return False,None
    else:
        return True,data[0]

def semua_kamar():
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = "SELECT kamar_id as nomer_kamar,nama_kamar as kamar, lantai FROM kamar order by kamar_id"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    return data

def nama_kamar(id_kamar):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"SELECT nama_kamar FROM kamar where kamar_id = {id_kamar}"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    return [x for x in data[0]]

def kelola_harga_kamar(mode,harga=None):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    if mode == "lihat":
        sql = "SELECT harga From kamar limit 1"
        navigate.execute(sql)
        data = navigate.fetchall()
        open_db.close()
        return [x for x in data[0]][0]
    if mode == "edit":
        try:
            sql = f"UPDATE kamar set harga = {int(harga)}"
            navigate.execute(sql)
            open_db.commit()
            open_db.close()
            return True
        except:
            open_db.close()
            return False
def tambah_feedback(id_user,feedback):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"INSERT INTO feedback(isi_feedback,user_user_id) VALUES ('{feedback}',{id_user})"
    navigate.execute(sql)
    open_db.commit()
    open_db.close()
    return True

def daftar_transaksi_user(user_id):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"select to_char(t.tanggal,'dd-mm-yyy'),k.nama_kamar,t.nominal,t.status_pembayaran from transaksi t join kamar k on t.kamar_kamar_id = k.kamar_id where t.user_user_id = {user_id}"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    return data

def tambah_karyawan(id_admin,nama,no_telp,alamat):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    try:
        sql = f"INSERT INTO karyawan(nama,no_telp,alamat,admin_admin_id) VALUES ('{nama}','{no_telp}','{alamat}',{id_admin})"
        navigate.execute(sql)
        open_db.commit()
        open_db.close()
        return True
    except:
        open_db.close()
        return False
    
def hapus_karyawan(id_karyawan):
    pass

def tambah_biaya_bulanan(id_admin,tagihan_air,tagihan_listrik,tagihan_wifi):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    try:
        sql = f"INSERT INTO pengeluaran(pengeluaran_air,pengeluaran_listrik,pengeluaran_wifi,admin_admin_id) VALUES ({int(tagihan_air)},{int(tagihan_listrik)},{int(tagihan_wifi)},{id_admin})"
        navigate.execute(sql)
        open_db.commit()
        open_db.close()
        return True
    except:
        open_db.close()
        return False

def detail_kamar(kamar_id):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"select p.perabotan from perabotan p join detail_kamar dk on p.perabotan_id = dk.perabotan_perabotan_id join kamar k on k.kamar_id = dk.kamar_kamar_id where k.kamar_id = {kamar_id}"
    navigate.execute(sql)
    perabotan = [x[0] for x in navigate.fetchall()]
    sql = f"Select nama_kamar,lantai,harga from kamar where kamar_id = {kamar_id} "
    navigate.execute(sql)
    data_kamar = [x for x in navigate.fetchall()[0]]
    open_db.close()
    return perabotan,data_kamar

def transaksi_bank(user_id,fk_bank,fk_kamar,nominal,no_rek,nama,jenis="Bank",status="Menunggu Verifikasi"):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    try:
        sql = f"INSERT INTO metode_pembayaran(jenis_metode_pembayaran) VALUES ('{jenis}')"
        navigate.execute(sql)
        open_db.commit()
        sql = "SELECT metode_pembayaran_id FROM metode_pembayaran order by metode_pembayaran_id DESC limit 1"
        navigate.execute(sql)
        fk_metode = int(navigate.fetchall()[0][0])
        sql = f"INSERT INTO pembayaran_bank(no_rekening,nama_pemilik,metode_pembayaran_id,bank_id) VALUES ('{no_rek}','{nama}',{fk_metode},{int(fk_bank)})"
        navigate.execute(sql)
        open_db.commit()
        sql = f"INSERT INTO Transaksi(nominal,status_pembayaran,metode_pembayaran_id,kamar_kamar_id,user_user_id) VALUES ({nominal},'{status}',{fk_metode},{int(fk_kamar)},{int(user_id)})"
        navigate.execute(sql)
        open_db.commit()
        open_db.close()
        return True
    except:
        open_db.close()
        return False

def transaksi_e_wallet(user_id,fk_e_wallet,fk_kamar,nominal,no_e_wallet,nama,jenis="E-Wallet",status="Menunggu Verifikasi"):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    try:
        sql = f"INSERT INTO metode_pembayaran(jenis_metode_pembayaran) VALUES ('{jenis}')"
        navigate.execute(sql)
        open_db.commit()
        sql = "SELECT metode_pembayaran_id FROM metode_pembayaran order by metode_pembayaran_id DESC limit 1"
        navigate.execute(sql)
        fk_metode = int(navigate.fetchall()[0][0])
        sql = f"INSERT INTO pembayaran_ewallet(nomor_ewallet,nama_pemilik,metode_pembayaran_id,ewallet_id) VALUES ('{no_e_wallet}','{nama}',{fk_metode},{int(fk_e_wallet)})"
        navigate.execute(sql)
        open_db.commit()
        sql = f"INSERT INTO Transaksi(nominal,status_pembayaran,metode_pembayaran_id,kamar_kamar_id,user_user_id) VALUES ({nominal},'{status}',{fk_metode},{int(fk_kamar)},{int(user_id)})"
        navigate.execute(sql)
        open_db.commit()
        open_db.close()
        return True
    except:
        open_db.close()
        return False

def bank():
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = "SELECT bank_id,nama_bank FROM bank"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    return [[x for x in x] for x in data]

def E_wallet():
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = "SELECT ewallet_id,nama_ewallet FROM ewallet"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    return [[x for x in x] for x in data]

def transaksi_owner():
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = "select t.transaksi_id,to_char(t.tanggal,'dd-mm-yyy'),P.nama, K.nama_kamar,T.nominal,m.jenis_metode_pembayaran from Pelanggan P JOIN transaksi t On P.user_id = T.user_user_id JOIN Kamar K ON k.kamar_id = T.kamar_kamar_id JOIN metode_pembayaran m ON m.metode_pembayaran_id = T.metode_pembayaran_id where t.status_pembayaran = 'Berhasil' order by t.transaksi_id DESC"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    return [[x for x in x] for x in data]

def transaksi_baru():
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = "select t.transaksi_id,to_char(t.tanggal,'dd-mm-yyy'),P.nama, K.nama_kamar,T.nominal,m.jenis_metode_pembayaran from Pelanggan P JOIN transaksi t On P.user_id = T.user_user_id JOIN Kamar K ON k.kamar_id = T.kamar_kamar_id JOIN metode_pembayaran m ON m.metode_pembayaran_id = T.metode_pembayaran_id where t.status_pembayaran = 'Menunggu Verifikasi' order by t.transaksi_id DESC"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    if data == []:
        return False,None
    else:
        return True, [[x for x in x] for x in data]

def acc_transaksi(id_transaksi,kamar):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"UPDATE Transaksi set status_pembayaran = 'Berhasil' where transaksi_id = {id_transaksi}"
    navigate.execute(sql)
    open_db.commit()
    sql = f"UPDATE Kamar set status_kamar = 'Terisi' where nama_kamar = '{kamar}'"
    navigate.execute(sql)
    open_db.commit()
    open_db.close()
    return True

def tolak_transaksi(id_transaksi):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"UPDATE Transaksi set status_pembayaran = 'Dibatalkan' where transaksi_id = {id_transaksi}"
    navigate.execute(sql)
    open_db.commit()
    open_db.close()
    return True

def status_kamar(id_kamar):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"SELECT status_kamar from kamar where kamar_id = {id_kamar}"
    navigate.execute(sql)
    data = navigate.fetchall()
    open_db.close()
    return [x[0] for x in data][0]

def update_status_kamar(id_kamar):
    open_db = psycopg2.connect(host=host_name, dbname=data_base,user=username,password=pw,port=port)
    navigate = open_db.cursor()
    sql = f"UPDATE kamar set status_kamar = 'Kosong' where kamar_id = {int(id_kamar)}"
    navigate.execute(sql)
    open_db.commit()
    open_db.close
    return True