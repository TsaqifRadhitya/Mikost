CREATE TABLE admin (
    admin_id     SERIAL PRIMARY KEY,
    nama         VARCHAR(50) NOT NULL,
    no_telp      VARCHAR(12) NOT NULL,
	status_akun Boolean NOT NULL,
    akun_akun_id INTEGER NOT NULL,
    CONSTRAINT admin_no_telp_un UNIQUE (no_telp)
);
CREATE TABLE akun (
    akun_id    SERIAL PRIMARY KEY,
    username   VARCHAR(12) NOT NULL,
    password   VARCHAR(8) NOT NULL,
    jenis_akun VARCHAR(50) NOT NULL,
    CONSTRAINT akun_username_un UNIQUE (username)
);

CREATE TABLE bank (
    bank_id   SERIAL PRIMARY KEY,
    nama_bank VARCHAR(25) NOT NULL
);

CREATE TABLE detail_kamar (
    detail_kamar_id        SERIAL PRIMARY KEY,
    perabotan_perabotan_id INTEGER NOT NULL,
    kamar_kamar_id         INTEGER NOT NULL
);

CREATE TABLE "e-wallet" (
    "e-wallet_ID"   SERIAL PRIMARY KEY,
    "nama_e-wallet" VARCHAR(25) NOT NULL
);

CREATE TABLE feedback (
    feedback_id  SERIAL PRIMARY KEY,
    tanggal      DATE NOT NULL,
    isi_feedback VARCHAR(1000) NOT NULL,
    user_user_id INTEGER NOT NULL
);

CREATE TABLE kamar (
    kamar_id     SERIAL PRIMARY KEY,
    nama_kamar   VARCHAR(50) NOT NULL,
    lantai       VARCHAR(50) NOT NULL,
harga INT NOT NULL,
    status_kamar VARCHAR(10) NOT NULL
);

CREATE TABLE karyawan (
    karyawan_id    SERIAL PRIMARY KEY,
    nama           VARCHAR(50) NOT NULL,
    no_telp        CHAR(12) NOT NULL,
    alamat         VARCHAR(50) NOT NULL,
    admin_admin_id INTEGER NOT NULL,
    CONSTRAINT karyawan_no_telp_un UNIQUE (no_telp)
);

CREATE TABLE metode_pembayaran (
    metode_pembayaran_id    SERIAL PRIMARY KEY,
    jenis_metode_pembayaran VARCHAR(10) NOT NULL,
    transaksi_transaksi_id  INTEGER NOT NULL
);

CREATE TABLE owner (
    owner_id     SERIAL PRIMARY KEY,
    akun_akun_id INTEGER NOT NULL
);

CREATE TABLE pembayaran_bank (
    pembayaran_bank_id   SERIAL PRIMARY KEY,
    no_rekening          VARCHAR(25) NOT NULL,
    nama_pemilik         VARCHAR(25) NOT NULL,
    metode_pembayaran_id INTEGER NOT NULL,
    bank_id              INTEGER NOT NULL,
    CONSTRAINT pembayaran_bank_id_un UNIQUE (pembayaran_bank_id)
);

CREATE TABLE "pembayaran_e-wallet" (
    "pembayaran_e-wallet_ID" SERIAL PRIMARY KEY,
    "Nomor_E-Wallet"         VARCHAR(25) NOT NULL,
    nama_pemilik             VARCHAR(25) NOT NULL,
    metode_pembayaran_id     INTEGER NOT NULL,
    "e-wallet_ID"            INTEGER NOT NULL,
    CONSTRAINT pembayaran_e_wallet_id_un UNIQUE ("pembayaran_e-wallet_ID")
);

CREATE TABLE pengeluaran (
    pengeluaran_id      SERIAL PRIMARY KEY,
    tanggal             DATE NOT NULL,
    pengeluaran_air     INTEGER NOT NULL,
    pengeluaran_listrik INTEGER NOT NULL,
    pengeluaran_wifi    INTEGER NOT NULL,
    admin_admin_id      INTEGER NOT NULL
);

CREATE TABLE perabotan (
    perabotan_id SERIAL PRIMARY KEY,
    perabotan    VARCHAR(50) NOT NULL
);

CREATE TABLE transaksi (
    transaksi_id         SERIAL PRIMARY KEY,
    tanggal              DATE NOT NULL,
    nominal              INTEGER NOT NULL,
    status_pembayaran    VARCHAR(50) NOT NULL,
    metode_pembayaran_id INTEGER NOT NULL,
    kamar_kamar_id       INTEGER NOT NULL,
    user_user_id         INTEGER NOT NULL
);

CREATE TABLE "User" (
    user_id      SERIAL PRIMARY KEY,
    email        VARCHAR(50) NOT NULL,
    nama         VARCHAR(50) NOT NULL,
    nomer_hp     CHAR(12) NOT NULL,
    asal         VARCHAR(50) NOT NULL,
    akun_akun_id INTEGER NOT NULL,
    CONSTRAINT user_email_nomer_hp_un UNIQUE (email, nomer_hp)
);

ALTER TABLE admin
    ADD CONSTRAINT admin_akun_fk FOREIGN KEY (akun_akun_id)
        REFERENCES akun (akun_id);

ALTER TABLE detail_kamar
    ADD CONSTRAINT detail_kamar_kamar_fk FOREIGN KEY (kamar_kamar_id)
        REFERENCES kamar (kamar_id);

ALTER TABLE detail_kamar
    ADD CONSTRAINT detail_kamar_perabotan_fk FOREIGN KEY (perabotan_perabotan_id)
        REFERENCES perabotan (perabotan_id);

ALTER TABLE "pembayaran_e-wallet"
    ADD CONSTRAINT "e-wallet_FK" FOREIGN KEY ("e-wallet_ID")
        REFERENCES "e-wallet" ("e-wallet_ID");

ALTER TABLE feedback
    ADD CONSTRAINT feedback_user_fk FOREIGN KEY (user_user_id)
        REFERENCES "User" (user_id);

ALTER TABLE karyawan
    ADD CONSTRAINT karyawan_admin_fk FOREIGN KEY (admin_admin_id)
        REFERENCES admin (admin_id);

ALTER TABLE pembayaran_bank
    ADD CONSTRAINT metode_pembayaran_fk FOREIGN KEY (metode_pembayaran_id)
        REFERENCES metode_pembayaran (metode_pembayaran_id);

ALTER TABLE "pembayaran_e-wallet"
    ADD CONSTRAINT metode_pembayaran_fkv2 FOREIGN KEY (metode_pembayaran_id)
        REFERENCES metode_pembayaran (metode_pembayaran_id);

ALTER TABLE metode_pembayaran
    ADD CONSTRAINT metode_pembayaran_transaksi_fk FOREIGN KEY (transaksi_transaksi_id)
        REFERENCES transaksi (transaksi_id);

ALTER TABLE owner
    ADD CONSTRAINT owner_akun_fk FOREIGN KEY (akun_akun_id)
        REFERENCES akun (akun_id);

ALTER TABLE pembayaran_bank
    ADD CONSTRAINT pembayaran_bank_bank_fk FOREIGN KEY (bank_id)
        REFERENCES bank (bank_id);

ALTER TABLE pengeluaran
    ADD CONSTRAINT pengeluaran_admin_fk FOREIGN KEY (admin_admin_id)
        REFERENCES admin (admin_id);

ALTER TABLE transaksi
    ADD CONSTRAINT transaksi_kamar_fk FOREIGN KEY (kamar_kamar_id)
        REFERENCES kamar (kamar_id);

ALTER TABLE transaksi
    ADD CONSTRAINT transaksi_metode_pembayaran_fk FOREIGN KEY (metode_pembayaran_id)
        REFERENCES metode_pembayaran (metode_pembayaran_id);

ALTER TABLE transaksi
    ADD CONSTRAINT transaksi_user_fk FOREIGN KEY (user_user_id)
        REFERENCES "User" (user_id);

ALTER TABLE "User"
    ADD CONSTRAINT user_akun_fk FOREIGN KEY (akun_akun_id)
        REFERENCES akun (akun_id);
CREATE TYPE Enum_jenis_akun AS ENUM ('Admin', 'Owner', 'User');
CREATE TYPE Enum_metode_pembayaran AS ENUM ('Bank', 'E-Wallet');
CREATE TYPE Enum_status_pembayaran AS ENUM ('Menunggu Verifikasi','Berhasil','Dibatalkan');
CREATE TYPE Enum_status_kamar AS ENUM ('Kosong','Terisi');
CREATE TYPE Enum_lantai AS ENUM ('1','2','3');

ALTER TABLE akun
ALTER COLUMN jenis_akun TYPE Enum_jenis_akun
USING jenis_akun::Enum_jenis_akun;

ALTER TABLE metode_pembayaran
ALTER COLUMN jenis_metode_pembayaran TYPE Enum_metode_pembayaran
USING jenis_metode_pembayaran::Enum_metode_pembayaran;

ALTER TABLE transaksi
ALTER COLUMN status_pembayaran TYPE Enum_status_pembayaran
USING status_pembayaran::Enum_status_pembayaran;

ALTER TABLE kamar
ALTER COLUMN lantai TYPE Enum_lantai
USING lantai::Enum_lantai;

ALTER TABLE kamar
ALTER COLUMN status_kamar TYPE Enum_status_kamar
USING status_kamar::Enum_status_kamar;
ALTER TABLE pengeluaran
ALTER COLUMN Tanggal SET DEFAULT CURRENT_DATE;

ALTER TABLE feedback
ALTER COLUMN Tanggal SET DEFAULT CURRENT_DATE;

ALTER TABLE Transaksi
ALTER COLUMN Tanggal SET DEFAULT CURRENT_DATE;
ALTER TABLE akun
ALTER COLUMN password TYPE VARCHAR(20)
USING password::VARCHAR(20	);

ALTER TABLE admin 
ALTER COLUMN no_telp TYPE VARCHAR(20)
USING no_telp::VARCHAR(20);

ALTER TABLE "User"
ALTER COLUMN nomer_hp TYPE VARCHAR(20)
USING nomer_hp::VARCHAR(20);
ALTER TABLE "User" RENAME TO Pelanggan;
ALTER TABLE pembayaran_bank
ALTER COLUMN nama_pemilik TYPE VARCHAR(50);
ALTER TABLE "pembayaran_e-wallet" RENAME TO Pembayaran_ewallet;
ALTER TABLE pembayaran_ewallet RENAME COLUMN "Nomor_E-Wallet" TO Nomor_EWallet;
ALTER TABLE pembayaran_ewallet RENAME COLUMN "e-wallet_ID" TO ewallet_ID;
ALTER TABLE pembayaran_ewallet ALTER COLUMN nama_pemilik TYPE VARCHAR(50);
ALTER TABLE "e-wallet" RENAME TO ewallet;
ALTER TABLE ewallet
RENAME COLUMN "e-wallet_ID" TO ewallet_id;
ALTER TABLE ewallet
RENAME COLUMN "nama_e-wallet" TO nama_ewallet;
ALTER TABLE karyawan
ALTER COLUMN no_telp TYPE VARCHAR(20)
USING no_telp::VARCHAR(20);
alter table metode_pembayaran
drop column transaksi_transaksi_id;
alter table Pelanggan
add constraint unik UNIQUE(nomer_hp);
alter table Admin
add constraint unik_nomer UNIQUE(no_telp);
alter table Pelanggan
add constraint emaiL_unik UNIQUE(email);