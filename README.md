# Pengenal Pose Jari

Aplikasi web sederhana yang membuka kamera dan mengenali pose tangan secara langsung:
**pose lima jari** atau **pose tiga jari**. Modelnya dilatih dengan
[Teachable Machine](https://teachablemachine.withgoogle.com/) dan dijalankan di browser
memakai TensorFlow.js. Tidak ada data yang dikirim ke server.

Dibuat oleh Elsya Sagitha Damayanti .S S1 Ilmu Komputer, Universitas Halu Oleo.

## Demo online

Setelah GitHub Pages aktif, aplikasi bisa dibuka di:

[`https://elsya.github.io/NAMA-REPO/`](https://github.com/sagithadamayantielsya-source/IDENTIFIKASI-POSE-JARI.git)

Ganti `USERNAME` dan `NAMA-REPO` sesuai akun dan nama repositori Anda.

## Cara menjalankan di komputer

1. Unduh atau `git clone` repositori ini.
2. Klik dua kali `index.html` (Chrome atau Edge disarankan).
3. Tunggu status **Model siap**, lalu klik **Nyalakan kamera** dan izinkan akses kamera.

Butuh internet, karena TensorFlow.js dan font diambil dari CDN.

## Struktur proyek

```
.
├── index.html            Halaman utama (tampilan dan logika)
├── model-data.js         Model yang sudah dikemas jadi satu file (dibuat otomatis)
├── model/                Model asli dari Teachable Machine
│   ├── model.json
│   ├── metadata.json
│   └── weights.bin
├── tools/
│   └── buat-model-data.py   Skrip pembuat model-data.js
├── .gitignore
├── LICENSE
└── README.md
```

## Mengganti model

1. Latih model baru di Teachable Machine, lalu ekspor sebagai TensorFlow.js (Download).
2. Ganti tiga file di folder `model/` dengan hasil unduhan.
3. Jalankan: `python tools/buat-model-data.py`
4. Muat ulang `index.html`.

## Teknologi

- HTML, CSS, JavaScript
- [TensorFlow.js](https://www.tensorflow.org/js) 1.3.1
- [@teachablemachine/image](https://github.com/googlecreativelab/teachablemachine-community) 0.8.4

## Lisensi

MIT. Lihat berkas `LICENSE`.
