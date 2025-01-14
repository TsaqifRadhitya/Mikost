PGDMP      (                |            backup    16.2    16.2 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    35428    backup    DATABASE     }   CREATE DATABASE backup WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';
    DROP DATABASE backup;
                postgres    false            g           1247    35430    enum_jenis_akun    TYPE     U   CREATE TYPE public.enum_jenis_akun AS ENUM (
    'Admin',
    'Owner',
    'User'
);
 "   DROP TYPE public.enum_jenis_akun;
       public          postgres    false            j           1247    35438    enum_lantai    TYPE     F   CREATE TYPE public.enum_lantai AS ENUM (
    '1',
    '2',
    '3'
);
    DROP TYPE public.enum_lantai;
       public          postgres    false            m           1247    35446    enum_metode_pembayaran    TYPE     R   CREATE TYPE public.enum_metode_pembayaran AS ENUM (
    'Bank',
    'E-Wallet'
);
 )   DROP TYPE public.enum_metode_pembayaran;
       public          postgres    false            p           1247    35452    enum_status_kamar    TYPE     M   CREATE TYPE public.enum_status_kamar AS ENUM (
    'Kosong',
    'Terisi'
);
 $   DROP TYPE public.enum_status_kamar;
       public          postgres    false            s           1247    35458    enum_status_pembayaran    TYPE     s   CREATE TYPE public.enum_status_pembayaran AS ENUM (
    'Menunggu Verifikasi',
    'Berhasil',
    'Dibatalkan'
);
 )   DROP TYPE public.enum_status_pembayaran;
       public          postgres    false            �            1259    35465 	   pelanggan    TABLE       CREATE TABLE public.pelanggan (
    user_id integer NOT NULL,
    email character varying(50) NOT NULL,
    nama character varying(50) NOT NULL,
    nomer_hp character varying(20) NOT NULL,
    asal character varying(50) NOT NULL,
    akun_akun_id integer NOT NULL
);
    DROP TABLE public.pelanggan;
       public         heap    postgres    false            �            1259    35468    User_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public."User_user_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public."User_user_id_seq";
       public          postgres    false    215            �           0    0    User_user_id_seq    SEQUENCE OWNED BY     L   ALTER SEQUENCE public."User_user_id_seq" OWNED BY public.pelanggan.user_id;
          public          postgres    false    216            �            1259    35469    admin    TABLE     �   CREATE TABLE public.admin (
    admin_id integer NOT NULL,
    nama character varying(50) NOT NULL,
    no_telp character varying(20) NOT NULL,
    akun_akun_id integer NOT NULL,
    status_akun boolean NOT NULL
);
    DROP TABLE public.admin;
       public         heap    postgres    false            �            1259    35472    admin_admin_id_seq    SEQUENCE     �   CREATE SEQUENCE public.admin_admin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.admin_admin_id_seq;
       public          postgres    false    217            �           0    0    admin_admin_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.admin_admin_id_seq OWNED BY public.admin.admin_id;
          public          postgres    false    218            �            1259    35473    akun    TABLE     �   CREATE TABLE public.akun (
    akun_id integer NOT NULL,
    username character varying(12) NOT NULL,
    password character varying(20) NOT NULL,
    jenis_akun public.enum_jenis_akun NOT NULL
);
    DROP TABLE public.akun;
       public         heap    postgres    false    871            �            1259    35476    akun_akun_id_seq    SEQUENCE     �   CREATE SEQUENCE public.akun_akun_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.akun_akun_id_seq;
       public          postgres    false    219            �           0    0    akun_akun_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.akun_akun_id_seq OWNED BY public.akun.akun_id;
          public          postgres    false    220            �            1259    35477    bank    TABLE     i   CREATE TABLE public.bank (
    bank_id integer NOT NULL,
    nama_bank character varying(25) NOT NULL
);
    DROP TABLE public.bank;
       public         heap    postgres    false            �            1259    35480    bank_bank_id_seq    SEQUENCE     �   CREATE SEQUENCE public.bank_bank_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.bank_bank_id_seq;
       public          postgres    false    221            �           0    0    bank_bank_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.bank_bank_id_seq OWNED BY public.bank.bank_id;
          public          postgres    false    222            �            1259    35481    detail_kamar    TABLE     �   CREATE TABLE public.detail_kamar (
    detail_kamar_id integer NOT NULL,
    perabotan_perabotan_id integer NOT NULL,
    kamar_kamar_id integer NOT NULL
);
     DROP TABLE public.detail_kamar;
       public         heap    postgres    false            �            1259    35484     detail_kamar_detail_kamar_id_seq    SEQUENCE     �   CREATE SEQUENCE public.detail_kamar_detail_kamar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.detail_kamar_detail_kamar_id_seq;
       public          postgres    false    223            �           0    0     detail_kamar_detail_kamar_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.detail_kamar_detail_kamar_id_seq OWNED BY public.detail_kamar.detail_kamar_id;
          public          postgres    false    224            �            1259    35485    ewallet    TABLE     r   CREATE TABLE public.ewallet (
    ewallet_id integer NOT NULL,
    nama_ewallet character varying(25) NOT NULL
);
    DROP TABLE public.ewallet;
       public         heap    postgres    false            �            1259    35488    e-wallet_e-wallet_ID_seq    SEQUENCE     �   CREATE SEQUENCE public."e-wallet_e-wallet_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public."e-wallet_e-wallet_ID_seq";
       public          postgres    false    225            �           0    0    e-wallet_e-wallet_ID_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public."e-wallet_e-wallet_ID_seq" OWNED BY public.ewallet.ewallet_id;
          public          postgres    false    226            �            1259    35489    feedback    TABLE     �   CREATE TABLE public.feedback (
    feedback_id integer NOT NULL,
    tanggal date DEFAULT CURRENT_DATE NOT NULL,
    isi_feedback character varying(1000) NOT NULL,
    user_user_id integer NOT NULL
);
    DROP TABLE public.feedback;
       public         heap    postgres    false            �            1259    35495    feedback_feedback_id_seq    SEQUENCE     �   CREATE SEQUENCE public.feedback_feedback_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.feedback_feedback_id_seq;
       public          postgres    false    227            �           0    0    feedback_feedback_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.feedback_feedback_id_seq OWNED BY public.feedback.feedback_id;
          public          postgres    false    228            �            1259    35496    kamar    TABLE     �   CREATE TABLE public.kamar (
    kamar_id integer NOT NULL,
    nama_kamar character varying(50) NOT NULL,
    lantai public.enum_lantai NOT NULL,
    status_kamar public.enum_status_kamar NOT NULL,
    harga integer NOT NULL
);
    DROP TABLE public.kamar;
       public         heap    postgres    false    874    880            �            1259    35499    kamar_kamar_id_seq    SEQUENCE     �   CREATE SEQUENCE public.kamar_kamar_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.kamar_kamar_id_seq;
       public          postgres    false    229            �           0    0    kamar_kamar_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.kamar_kamar_id_seq OWNED BY public.kamar.kamar_id;
          public          postgres    false    230            �            1259    35500    karyawan    TABLE     �   CREATE TABLE public.karyawan (
    karyawan_id integer NOT NULL,
    nama character varying(50) NOT NULL,
    no_telp character varying(20) NOT NULL,
    alamat character varying(50) NOT NULL,
    admin_admin_id integer NOT NULL
);
    DROP TABLE public.karyawan;
       public         heap    postgres    false            �            1259    35503    karyawan_karyawan_id_seq    SEQUENCE     �   CREATE SEQUENCE public.karyawan_karyawan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.karyawan_karyawan_id_seq;
       public          postgres    false    231            �           0    0    karyawan_karyawan_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.karyawan_karyawan_id_seq OWNED BY public.karyawan.karyawan_id;
          public          postgres    false    232            �            1259    35504    metode_pembayaran    TABLE     �   CREATE TABLE public.metode_pembayaran (
    metode_pembayaran_id integer NOT NULL,
    jenis_metode_pembayaran public.enum_metode_pembayaran NOT NULL
);
 %   DROP TABLE public.metode_pembayaran;
       public         heap    postgres    false    877            �            1259    35507 *   metode_pembayaran_metode_pembayaran_id_seq    SEQUENCE     �   CREATE SEQUENCE public.metode_pembayaran_metode_pembayaran_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 A   DROP SEQUENCE public.metode_pembayaran_metode_pembayaran_id_seq;
       public          postgres    false    233            �           0    0 *   metode_pembayaran_metode_pembayaran_id_seq    SEQUENCE OWNED BY     y   ALTER SEQUENCE public.metode_pembayaran_metode_pembayaran_id_seq OWNED BY public.metode_pembayaran.metode_pembayaran_id;
          public          postgres    false    234            �            1259    35508    owner    TABLE     `   CREATE TABLE public.owner (
    owner_id integer NOT NULL,
    akun_akun_id integer NOT NULL
);
    DROP TABLE public.owner;
       public         heap    postgres    false            �            1259    35511    owner_owner_id_seq    SEQUENCE     �   CREATE SEQUENCE public.owner_owner_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.owner_owner_id_seq;
       public          postgres    false    235            �           0    0    owner_owner_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.owner_owner_id_seq OWNED BY public.owner.owner_id;
          public          postgres    false    236            �            1259    35512    pembayaran_bank    TABLE     �   CREATE TABLE public.pembayaran_bank (
    pembayaran_bank_id integer NOT NULL,
    no_rekening character varying(25) NOT NULL,
    nama_pemilik character varying(50) NOT NULL,
    metode_pembayaran_id integer NOT NULL,
    bank_id integer NOT NULL
);
 #   DROP TABLE public.pembayaran_bank;
       public         heap    postgres    false            �            1259    35515 &   pembayaran_bank_pembayaran_bank_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pembayaran_bank_pembayaran_bank_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 =   DROP SEQUENCE public.pembayaran_bank_pembayaran_bank_id_seq;
       public          postgres    false    237            �           0    0 &   pembayaran_bank_pembayaran_bank_id_seq    SEQUENCE OWNED BY     q   ALTER SEQUENCE public.pembayaran_bank_pembayaran_bank_id_seq OWNED BY public.pembayaran_bank.pembayaran_bank_id;
          public          postgres    false    238            �            1259    35516    pembayaran_ewallet    TABLE     	  CREATE TABLE public.pembayaran_ewallet (
    "pembayaran_e-wallet_ID" integer NOT NULL,
    nomor_ewallet character varying(25) NOT NULL,
    nama_pemilik character varying(50) NOT NULL,
    metode_pembayaran_id integer NOT NULL,
    ewallet_id integer NOT NULL
);
 &   DROP TABLE public.pembayaran_ewallet;
       public         heap    postgres    false            �            1259    35519 .   pembayaran_e-wallet_pembayaran_e-wallet_ID_seq    SEQUENCE     �   CREATE SEQUENCE public."pembayaran_e-wallet_pembayaran_e-wallet_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 G   DROP SEQUENCE public."pembayaran_e-wallet_pembayaran_e-wallet_ID_seq";
       public          postgres    false    239            �           0    0 .   pembayaran_e-wallet_pembayaran_e-wallet_ID_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public."pembayaran_e-wallet_pembayaran_e-wallet_ID_seq" OWNED BY public.pembayaran_ewallet."pembayaran_e-wallet_ID";
          public          postgres    false    240            �            1259    35520    pengeluaran    TABLE       CREATE TABLE public.pengeluaran (
    pengeluaran_id integer NOT NULL,
    tanggal date DEFAULT CURRENT_DATE NOT NULL,
    pengeluaran_air integer NOT NULL,
    pengeluaran_listrik integer NOT NULL,
    pengeluaran_wifi integer NOT NULL,
    admin_admin_id integer NOT NULL
);
    DROP TABLE public.pengeluaran;
       public         heap    postgres    false            �            1259    35524    pengeluaran_pengeluaran_id_seq    SEQUENCE     �   CREATE SEQUENCE public.pengeluaran_pengeluaran_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.pengeluaran_pengeluaran_id_seq;
       public          postgres    false    241            �           0    0    pengeluaran_pengeluaran_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.pengeluaran_pengeluaran_id_seq OWNED BY public.pengeluaran.pengeluaran_id;
          public          postgres    false    242            �            1259    35525 	   perabotan    TABLE     s   CREATE TABLE public.perabotan (
    perabotan_id integer NOT NULL,
    perabotan character varying(50) NOT NULL
);
    DROP TABLE public.perabotan;
       public         heap    postgres    false            �            1259    35528    perabotan_perabotan_id_seq    SEQUENCE     �   CREATE SEQUENCE public.perabotan_perabotan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.perabotan_perabotan_id_seq;
       public          postgres    false    243            �           0    0    perabotan_perabotan_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.perabotan_perabotan_id_seq OWNED BY public.perabotan.perabotan_id;
          public          postgres    false    244            �            1259    35529 	   transaksi    TABLE     D  CREATE TABLE public.transaksi (
    transaksi_id integer NOT NULL,
    tanggal date DEFAULT CURRENT_DATE NOT NULL,
    nominal integer NOT NULL,
    status_pembayaran public.enum_status_pembayaran NOT NULL,
    metode_pembayaran_id integer NOT NULL,
    kamar_kamar_id integer NOT NULL,
    user_user_id integer NOT NULL
);
    DROP TABLE public.transaksi;
       public         heap    postgres    false    883            �            1259    35533    transaksi_transaksi_id_seq    SEQUENCE     �   CREATE SEQUENCE public.transaksi_transaksi_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.transaksi_transaksi_id_seq;
       public          postgres    false    245            �           0    0    transaksi_transaksi_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.transaksi_transaksi_id_seq OWNED BY public.transaksi.transaksi_id;
          public          postgres    false    246            �           2604    35534    admin admin_id    DEFAULT     p   ALTER TABLE ONLY public.admin ALTER COLUMN admin_id SET DEFAULT nextval('public.admin_admin_id_seq'::regclass);
 =   ALTER TABLE public.admin ALTER COLUMN admin_id DROP DEFAULT;
       public          postgres    false    218    217            �           2604    35535    akun akun_id    DEFAULT     l   ALTER TABLE ONLY public.akun ALTER COLUMN akun_id SET DEFAULT nextval('public.akun_akun_id_seq'::regclass);
 ;   ALTER TABLE public.akun ALTER COLUMN akun_id DROP DEFAULT;
       public          postgres    false    220    219            �           2604    35536    bank bank_id    DEFAULT     l   ALTER TABLE ONLY public.bank ALTER COLUMN bank_id SET DEFAULT nextval('public.bank_bank_id_seq'::regclass);
 ;   ALTER TABLE public.bank ALTER COLUMN bank_id DROP DEFAULT;
       public          postgres    false    222    221            �           2604    35537    detail_kamar detail_kamar_id    DEFAULT     �   ALTER TABLE ONLY public.detail_kamar ALTER COLUMN detail_kamar_id SET DEFAULT nextval('public.detail_kamar_detail_kamar_id_seq'::regclass);
 K   ALTER TABLE public.detail_kamar ALTER COLUMN detail_kamar_id DROP DEFAULT;
       public          postgres    false    224    223            �           2604    35538    ewallet ewallet_id    DEFAULT     |   ALTER TABLE ONLY public.ewallet ALTER COLUMN ewallet_id SET DEFAULT nextval('public."e-wallet_e-wallet_ID_seq"'::regclass);
 A   ALTER TABLE public.ewallet ALTER COLUMN ewallet_id DROP DEFAULT;
       public          postgres    false    226    225            �           2604    35539    feedback feedback_id    DEFAULT     |   ALTER TABLE ONLY public.feedback ALTER COLUMN feedback_id SET DEFAULT nextval('public.feedback_feedback_id_seq'::regclass);
 C   ALTER TABLE public.feedback ALTER COLUMN feedback_id DROP DEFAULT;
       public          postgres    false    228    227            �           2604    35540    kamar kamar_id    DEFAULT     p   ALTER TABLE ONLY public.kamar ALTER COLUMN kamar_id SET DEFAULT nextval('public.kamar_kamar_id_seq'::regclass);
 =   ALTER TABLE public.kamar ALTER COLUMN kamar_id DROP DEFAULT;
       public          postgres    false    230    229            �           2604    35541    karyawan karyawan_id    DEFAULT     |   ALTER TABLE ONLY public.karyawan ALTER COLUMN karyawan_id SET DEFAULT nextval('public.karyawan_karyawan_id_seq'::regclass);
 C   ALTER TABLE public.karyawan ALTER COLUMN karyawan_id DROP DEFAULT;
       public          postgres    false    232    231            �           2604    35542 &   metode_pembayaran metode_pembayaran_id    DEFAULT     �   ALTER TABLE ONLY public.metode_pembayaran ALTER COLUMN metode_pembayaran_id SET DEFAULT nextval('public.metode_pembayaran_metode_pembayaran_id_seq'::regclass);
 U   ALTER TABLE public.metode_pembayaran ALTER COLUMN metode_pembayaran_id DROP DEFAULT;
       public          postgres    false    234    233            �           2604    35543    owner owner_id    DEFAULT     p   ALTER TABLE ONLY public.owner ALTER COLUMN owner_id SET DEFAULT nextval('public.owner_owner_id_seq'::regclass);
 =   ALTER TABLE public.owner ALTER COLUMN owner_id DROP DEFAULT;
       public          postgres    false    236    235            �           2604    35544    pelanggan user_id    DEFAULT     s   ALTER TABLE ONLY public.pelanggan ALTER COLUMN user_id SET DEFAULT nextval('public."User_user_id_seq"'::regclass);
 @   ALTER TABLE public.pelanggan ALTER COLUMN user_id DROP DEFAULT;
       public          postgres    false    216    215            �           2604    35545 "   pembayaran_bank pembayaran_bank_id    DEFAULT     �   ALTER TABLE ONLY public.pembayaran_bank ALTER COLUMN pembayaran_bank_id SET DEFAULT nextval('public.pembayaran_bank_pembayaran_bank_id_seq'::regclass);
 Q   ALTER TABLE public.pembayaran_bank ALTER COLUMN pembayaran_bank_id DROP DEFAULT;
       public          postgres    false    238    237            �           2604    35546 )   pembayaran_ewallet pembayaran_e-wallet_ID    DEFAULT     �   ALTER TABLE ONLY public.pembayaran_ewallet ALTER COLUMN "pembayaran_e-wallet_ID" SET DEFAULT nextval('public."pembayaran_e-wallet_pembayaran_e-wallet_ID_seq"'::regclass);
 Z   ALTER TABLE public.pembayaran_ewallet ALTER COLUMN "pembayaran_e-wallet_ID" DROP DEFAULT;
       public          postgres    false    240    239            �           2604    35547    pengeluaran pengeluaran_id    DEFAULT     �   ALTER TABLE ONLY public.pengeluaran ALTER COLUMN pengeluaran_id SET DEFAULT nextval('public.pengeluaran_pengeluaran_id_seq'::regclass);
 I   ALTER TABLE public.pengeluaran ALTER COLUMN pengeluaran_id DROP DEFAULT;
       public          postgres    false    242    241            �           2604    35548    perabotan perabotan_id    DEFAULT     �   ALTER TABLE ONLY public.perabotan ALTER COLUMN perabotan_id SET DEFAULT nextval('public.perabotan_perabotan_id_seq'::regclass);
 E   ALTER TABLE public.perabotan ALTER COLUMN perabotan_id DROP DEFAULT;
       public          postgres    false    244    243            �           2604    35549    transaksi transaksi_id    DEFAULT     �   ALTER TABLE ONLY public.transaksi ALTER COLUMN transaksi_id SET DEFAULT nextval('public.transaksi_transaksi_id_seq'::regclass);
 E   ALTER TABLE public.transaksi ALTER COLUMN transaksi_id DROP DEFAULT;
       public          postgres    false    246    245            �          0    35469    admin 
   TABLE DATA           S   COPY public.admin (admin_id, nama, no_telp, akun_akun_id, status_akun) FROM stdin;
    public          postgres    false    217   ب       �          0    35473    akun 
   TABLE DATA           G   COPY public.akun (akun_id, username, password, jenis_akun) FROM stdin;
    public          postgres    false    219   �       �          0    35477    bank 
   TABLE DATA           2   COPY public.bank (bank_id, nama_bank) FROM stdin;
    public          postgres    false    221   ��       �          0    35481    detail_kamar 
   TABLE DATA           _   COPY public.detail_kamar (detail_kamar_id, perabotan_perabotan_id, kamar_kamar_id) FROM stdin;
    public          postgres    false    223   ԩ       �          0    35485    ewallet 
   TABLE DATA           ;   COPY public.ewallet (ewallet_id, nama_ewallet) FROM stdin;
    public          postgres    false    225   �       �          0    35489    feedback 
   TABLE DATA           T   COPY public.feedback (feedback_id, tanggal, isi_feedback, user_user_id) FROM stdin;
    public          postgres    false    227   "�       �          0    35496    kamar 
   TABLE DATA           R   COPY public.kamar (kamar_id, nama_kamar, lantai, status_kamar, harga) FROM stdin;
    public          postgres    false    229   j�       �          0    35500    karyawan 
   TABLE DATA           V   COPY public.karyawan (karyawan_id, nama, no_telp, alamat, admin_admin_id) FROM stdin;
    public          postgres    false    231   ��       �          0    35504    metode_pembayaran 
   TABLE DATA           Z   COPY public.metode_pembayaran (metode_pembayaran_id, jenis_metode_pembayaran) FROM stdin;
    public          postgres    false    233   a�       �          0    35508    owner 
   TABLE DATA           7   COPY public.owner (owner_id, akun_akun_id) FROM stdin;
    public          postgres    false    235   ��       �          0    35465 	   pelanggan 
   TABLE DATA           W   COPY public.pelanggan (user_id, email, nama, nomer_hp, asal, akun_akun_id) FROM stdin;
    public          postgres    false    215   Ĭ       �          0    35512    pembayaran_bank 
   TABLE DATA           w   COPY public.pembayaran_bank (pembayaran_bank_id, no_rekening, nama_pemilik, metode_pembayaran_id, bank_id) FROM stdin;
    public          postgres    false    237   q�       �          0    35516    pembayaran_ewallet 
   TABLE DATA           �   COPY public.pembayaran_ewallet ("pembayaran_e-wallet_ID", nomor_ewallet, nama_pemilik, metode_pembayaran_id, ewallet_id) FROM stdin;
    public          postgres    false    239   !�       �          0    35520    pengeluaran 
   TABLE DATA           �   COPY public.pengeluaran (pengeluaran_id, tanggal, pengeluaran_air, pengeluaran_listrik, pengeluaran_wifi, admin_admin_id) FROM stdin;
    public          postgres    false    241   ��       �          0    35525 	   perabotan 
   TABLE DATA           <   COPY public.perabotan (perabotan_id, perabotan) FROM stdin;
    public          postgres    false    243   
�       �          0    35529 	   transaksi 
   TABLE DATA           �   COPY public.transaksi (transaksi_id, tanggal, nominal, status_pembayaran, metode_pembayaran_id, kamar_kamar_id, user_user_id) FROM stdin;
    public          postgres    false    245   P�       �           0    0    User_user_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."User_user_id_seq"', 5, true);
          public          postgres    false    216            �           0    0    admin_admin_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.admin_admin_id_seq', 3, true);
          public          postgres    false    218            �           0    0    akun_akun_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.akun_akun_id_seq', 20, true);
          public          postgres    false    220            �           0    0    bank_bank_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.bank_bank_id_seq', 5, true);
          public          postgres    false    222            �           0    0     detail_kamar_detail_kamar_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.detail_kamar_detail_kamar_id_seq', 75, true);
          public          postgres    false    224            �           0    0    e-wallet_e-wallet_ID_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public."e-wallet_e-wallet_ID_seq"', 4, true);
          public          postgres    false    226            �           0    0    feedback_feedback_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.feedback_feedback_id_seq', 2, true);
          public          postgres    false    228            �           0    0    kamar_kamar_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.kamar_kamar_id_seq', 15, true);
          public          postgres    false    230            �           0    0    karyawan_karyawan_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.karyawan_karyawan_id_seq', 4, true);
          public          postgres    false    232            �           0    0 *   metode_pembayaran_metode_pembayaran_id_seq    SEQUENCE SET     X   SELECT pg_catalog.setval('public.metode_pembayaran_metode_pembayaran_id_seq', 9, true);
          public          postgres    false    234            �           0    0    owner_owner_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.owner_owner_id_seq', 1, true);
          public          postgres    false    236            �           0    0 &   pembayaran_bank_pembayaran_bank_id_seq    SEQUENCE SET     T   SELECT pg_catalog.setval('public.pembayaran_bank_pembayaran_bank_id_seq', 4, true);
          public          postgres    false    238            �           0    0 .   pembayaran_e-wallet_pembayaran_e-wallet_ID_seq    SEQUENCE SET     ^   SELECT pg_catalog.setval('public."pembayaran_e-wallet_pembayaran_e-wallet_ID_seq"', 5, true);
          public          postgres    false    240            �           0    0    pengeluaran_pengeluaran_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.pengeluaran_pengeluaran_id_seq', 3, true);
          public          postgres    false    242            �           0    0    perabotan_perabotan_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.perabotan_perabotan_id_seq', 5, true);
          public          postgres    false    244            �           0    0    transaksi_transaksi_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.transaksi_transaksi_id_seq', 9, true);
          public          postgres    false    246            �           2606    35551    pelanggan User_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.pelanggan
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (user_id);
 ?   ALTER TABLE ONLY public.pelanggan DROP CONSTRAINT "User_pkey";
       public            postgres    false    215            �           2606    35553    admin admin_no_telp_un 
   CONSTRAINT     T   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_no_telp_un UNIQUE (no_telp);
 @   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_no_telp_un;
       public            postgres    false    217            �           2606    35555    admin admin_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (admin_id);
 :   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_pkey;
       public            postgres    false    217            �           2606    35557    akun akun_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.akun
    ADD CONSTRAINT akun_pkey PRIMARY KEY (akun_id);
 8   ALTER TABLE ONLY public.akun DROP CONSTRAINT akun_pkey;
       public            postgres    false    219            �           2606    35559    akun akun_username_un 
   CONSTRAINT     T   ALTER TABLE ONLY public.akun
    ADD CONSTRAINT akun_username_un UNIQUE (username);
 ?   ALTER TABLE ONLY public.akun DROP CONSTRAINT akun_username_un;
       public            postgres    false    219            �           2606    35561    bank bank_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.bank
    ADD CONSTRAINT bank_pkey PRIMARY KEY (bank_id);
 8   ALTER TABLE ONLY public.bank DROP CONSTRAINT bank_pkey;
       public            postgres    false    221            �           2606    35563    detail_kamar detail_kamar_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.detail_kamar
    ADD CONSTRAINT detail_kamar_pkey PRIMARY KEY (detail_kamar_id);
 H   ALTER TABLE ONLY public.detail_kamar DROP CONSTRAINT detail_kamar_pkey;
       public            postgres    false    223            �           2606    35565    ewallet e-wallet_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.ewallet
    ADD CONSTRAINT "e-wallet_pkey" PRIMARY KEY (ewallet_id);
 A   ALTER TABLE ONLY public.ewallet DROP CONSTRAINT "e-wallet_pkey";
       public            postgres    false    225            �           2606    35567    feedback feedback_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT feedback_pkey PRIMARY KEY (feedback_id);
 @   ALTER TABLE ONLY public.feedback DROP CONSTRAINT feedback_pkey;
       public            postgres    false    227            �           2606    35569    kamar kamar_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.kamar
    ADD CONSTRAINT kamar_pkey PRIMARY KEY (kamar_id);
 :   ALTER TABLE ONLY public.kamar DROP CONSTRAINT kamar_pkey;
       public            postgres    false    229            �           2606    35666    karyawan karyawan_no_telp_un 
   CONSTRAINT     Z   ALTER TABLE ONLY public.karyawan
    ADD CONSTRAINT karyawan_no_telp_un UNIQUE (no_telp);
 F   ALTER TABLE ONLY public.karyawan DROP CONSTRAINT karyawan_no_telp_un;
       public            postgres    false    231            �           2606    35573    karyawan karyawan_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.karyawan
    ADD CONSTRAINT karyawan_pkey PRIMARY KEY (karyawan_id);
 @   ALTER TABLE ONLY public.karyawan DROP CONSTRAINT karyawan_pkey;
       public            postgres    false    231            �           2606    35575 (   metode_pembayaran metode_pembayaran_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.metode_pembayaran
    ADD CONSTRAINT metode_pembayaran_pkey PRIMARY KEY (metode_pembayaran_id);
 R   ALTER TABLE ONLY public.metode_pembayaran DROP CONSTRAINT metode_pembayaran_pkey;
       public            postgres    false    233            �           2606    35577    owner owner_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_pkey PRIMARY KEY (owner_id);
 :   ALTER TABLE ONLY public.owner DROP CONSTRAINT owner_pkey;
       public            postgres    false    235            �           2606    35579 %   pembayaran_bank pembayaran_bank_id_un 
   CONSTRAINT     s   ALTER TABLE ONLY public.pembayaran_bank
    ADD CONSTRAINT pembayaran_bank_id_un PRIMARY KEY (pembayaran_bank_id);
 O   ALTER TABLE ONLY public.pembayaran_bank DROP CONSTRAINT pembayaran_bank_id_un;
       public            postgres    false    237            �           2606    35581 ,   pembayaran_ewallet pembayaran_e_wallet_id_un 
   CONSTRAINT     �   ALTER TABLE ONLY public.pembayaran_ewallet
    ADD CONSTRAINT pembayaran_e_wallet_id_un PRIMARY KEY ("pembayaran_e-wallet_ID");
 V   ALTER TABLE ONLY public.pembayaran_ewallet DROP CONSTRAINT pembayaran_e_wallet_id_un;
       public            postgres    false    239            �           2606    35583    pengeluaran pengeluaran_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.pengeluaran
    ADD CONSTRAINT pengeluaran_pkey PRIMARY KEY (pengeluaran_id);
 F   ALTER TABLE ONLY public.pengeluaran DROP CONSTRAINT pengeluaran_pkey;
       public            postgres    false    241            �           2606    35585    perabotan perabotan_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.perabotan
    ADD CONSTRAINT perabotan_pkey PRIMARY KEY (perabotan_id);
 B   ALTER TABLE ONLY public.perabotan DROP CONSTRAINT perabotan_pkey;
       public            postgres    false    243            �           2606    35587    transaksi transaksi_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_pkey PRIMARY KEY (transaksi_id);
 B   ALTER TABLE ONLY public.transaksi DROP CONSTRAINT transaksi_pkey;
       public            postgres    false    245            �           2606    35589     pelanggan user_email_nomer_hp_un 
   CONSTRAINT     f   ALTER TABLE ONLY public.pelanggan
    ADD CONSTRAINT user_email_nomer_hp_un UNIQUE (email, nomer_hp);
 J   ALTER TABLE ONLY public.pelanggan DROP CONSTRAINT user_email_nomer_hp_un;
       public            postgres    false    215    215            �           2606    35590    admin admin_akun_fk    FK CONSTRAINT     {   ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_akun_fk FOREIGN KEY (akun_akun_id) REFERENCES public.akun(akun_id);
 =   ALTER TABLE ONLY public.admin DROP CONSTRAINT admin_akun_fk;
       public          postgres    false    217    4806    219            �           2606    35595 "   detail_kamar detail_kamar_kamar_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.detail_kamar
    ADD CONSTRAINT detail_kamar_kamar_fk FOREIGN KEY (kamar_kamar_id) REFERENCES public.kamar(kamar_id);
 L   ALTER TABLE ONLY public.detail_kamar DROP CONSTRAINT detail_kamar_kamar_fk;
       public          postgres    false    223    4818    229            �           2606    35600 &   detail_kamar detail_kamar_perabotan_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.detail_kamar
    ADD CONSTRAINT detail_kamar_perabotan_fk FOREIGN KEY (perabotan_perabotan_id) REFERENCES public.perabotan(perabotan_id);
 P   ALTER TABLE ONLY public.detail_kamar DROP CONSTRAINT detail_kamar_perabotan_fk;
       public          postgres    false    243    4834    223            �           2606    35605    pembayaran_ewallet e-wallet_FK    FK CONSTRAINT     �   ALTER TABLE ONLY public.pembayaran_ewallet
    ADD CONSTRAINT "e-wallet_FK" FOREIGN KEY (ewallet_id) REFERENCES public.ewallet(ewallet_id);
 J   ALTER TABLE ONLY public.pembayaran_ewallet DROP CONSTRAINT "e-wallet_FK";
       public          postgres    false    239    4814    225            �           2606    35610    feedback feedback_user_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.feedback
    ADD CONSTRAINT feedback_user_fk FOREIGN KEY (user_user_id) REFERENCES public.pelanggan(user_id);
 C   ALTER TABLE ONLY public.feedback DROP CONSTRAINT feedback_user_fk;
       public          postgres    false    227    4798    215            �           2606    35615    karyawan karyawan_admin_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.karyawan
    ADD CONSTRAINT karyawan_admin_fk FOREIGN KEY (admin_admin_id) REFERENCES public.admin(admin_id);
 D   ALTER TABLE ONLY public.karyawan DROP CONSTRAINT karyawan_admin_fk;
       public          postgres    false    4804    231    217            �           2606    35620 $   pembayaran_bank metode_pembayaran_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.pembayaran_bank
    ADD CONSTRAINT metode_pembayaran_fk FOREIGN KEY (metode_pembayaran_id) REFERENCES public.metode_pembayaran(metode_pembayaran_id);
 N   ALTER TABLE ONLY public.pembayaran_bank DROP CONSTRAINT metode_pembayaran_fk;
       public          postgres    false    4824    233    237            �           2606    35625 )   pembayaran_ewallet metode_pembayaran_fkv2    FK CONSTRAINT     �   ALTER TABLE ONLY public.pembayaran_ewallet
    ADD CONSTRAINT metode_pembayaran_fkv2 FOREIGN KEY (metode_pembayaran_id) REFERENCES public.metode_pembayaran(metode_pembayaran_id);
 S   ALTER TABLE ONLY public.pembayaran_ewallet DROP CONSTRAINT metode_pembayaran_fkv2;
       public          postgres    false    239    4824    233            �           2606    35630    owner owner_akun_fk    FK CONSTRAINT     {   ALTER TABLE ONLY public.owner
    ADD CONSTRAINT owner_akun_fk FOREIGN KEY (akun_akun_id) REFERENCES public.akun(akun_id);
 =   ALTER TABLE ONLY public.owner DROP CONSTRAINT owner_akun_fk;
       public          postgres    false    235    4806    219            �           2606    35635 '   pembayaran_bank pembayaran_bank_bank_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.pembayaran_bank
    ADD CONSTRAINT pembayaran_bank_bank_fk FOREIGN KEY (bank_id) REFERENCES public.bank(bank_id);
 Q   ALTER TABLE ONLY public.pembayaran_bank DROP CONSTRAINT pembayaran_bank_bank_fk;
       public          postgres    false    237    4810    221            �           2606    35640     pengeluaran pengeluaran_admin_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.pengeluaran
    ADD CONSTRAINT pengeluaran_admin_fk FOREIGN KEY (admin_admin_id) REFERENCES public.admin(admin_id);
 J   ALTER TABLE ONLY public.pengeluaran DROP CONSTRAINT pengeluaran_admin_fk;
       public          postgres    false    241    4804    217            �           2606    35645    transaksi transaksi_kamar_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_kamar_fk FOREIGN KEY (kamar_kamar_id) REFERENCES public.kamar(kamar_id);
 F   ALTER TABLE ONLY public.transaksi DROP CONSTRAINT transaksi_kamar_fk;
       public          postgres    false    4818    229    245            �           2606    35650 (   transaksi transaksi_metode_pembayaran_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_metode_pembayaran_fk FOREIGN KEY (metode_pembayaran_id) REFERENCES public.metode_pembayaran(metode_pembayaran_id);
 R   ALTER TABLE ONLY public.transaksi DROP CONSTRAINT transaksi_metode_pembayaran_fk;
       public          postgres    false    233    4824    245            �           2606    35655    transaksi transaksi_user_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaksi
    ADD CONSTRAINT transaksi_user_fk FOREIGN KEY (user_user_id) REFERENCES public.pelanggan(user_id);
 E   ALTER TABLE ONLY public.transaksi DROP CONSTRAINT transaksi_user_fk;
       public          postgres    false    215    4798    245            �           2606    35660    pelanggan user_akun_fk    FK CONSTRAINT     ~   ALTER TABLE ONLY public.pelanggan
    ADD CONSTRAINT user_akun_fk FOREIGN KEY (akun_akun_id) REFERENCES public.akun(akun_id);
 @   ALTER TABLE ONLY public.pelanggan DROP CONSTRAINT user_akun_fk;
       public          postgres    false    219    4806    215            �   /   x�3����,�2�.�M�+��4�0545363077�4J��qqq ��      �   n   x�3��/�K-���F���cJnf�	�\Ɯ!ŉ��iP
$ZTn�����	!ᢦ�A�ii�.j��X�Y��	���朎%���.j��	��Д�Ǝ���� j]5W      �   /   x�3�t
��2�t���2��M�K�,��2�trv�2�t
������ ��%      �      x��˵%!�ַ�������Ǩzcm����_h3��(��b�����2��)��-E��� �8
K"�D)�ǆb [��@j/P�|���}��N��Ǘ���s�!�-"�m"w�"w��C��:��$`� +Zg��\pux���K�iBi���\�D.�"����l]������M�&W|�b�\��/է	�=��"re���\�g�5�F����B��Ҡ�F}�U?�4�Ǘ�ӄ�rc����XE���I~      �   .   x�3����2�tq�s�2�t�p��2���/HMH������ �C�      �   8   x�3�4202�50�50��L�T�I��/�4�2���d3��S�J38��b���� h��      �   }   x�e�1
�0�9=�'��ժgput� �A�?!�����{���=Z��<����E�HL��\�nҩt �J�T��eP@F�dR�@��S�[0hVW�� f�%��7���!dm�s/�c7      �   Z   x�3��,�TJ��M��4�0�455�06�����M�KOOT���342�4�2�t��T.-N�+��55�5���,*N,������� cq      �   2   x�3�tJ���2�PƜ���99�%\&�)�iQg����X"Db���� �h      �      x�3�4����� ]      �   �   x�M���0Dg�cP��I��ʄ#K��*�%"�ҿ��T��ޝ�`��7��a
q<���= ����k��Mm������6V��p��bOF�:lF9��Zۅ7����2�Cd9��z��[Akc�<��m�������Pw
���a����;|���F{      �   �   x����0���+�f�-P���E<�xi�bR��߻x��a���.��ǭ����5_o��SL��2���!�S\�x��8~�a��������,��i3V�<�\K�\�M��:���=9�l�\s\���Ǧ�W��^�e�����,,      �   �   x�U�1�0C�S��?!aD�JU��]�R�����o�.�����!θZj����0M���ƜG�c�=��� !�����#l�ڴͯ/,���x��9�,�j��R�blD�9�P�+�?�	�T)w?�q۔�~RJ}�Q-�      �   :   x�3�4202�50�50�46 NS�rA՘���EMLQ���1�a�W� 0�w      �   6   x�3��I�M,��2��N,.-�2��M�J�2��.-*��2�tN-�������� -�P      �   �   x�}ϱ�0���/T����� !QQ1 �/�R�A�y|:;&,��s$�����~��4�1q%mHd���%1�i��e��o���%N���(�:�֛ۃ�I�k�5���,�Ͱ�xdF��p� � �zDV     