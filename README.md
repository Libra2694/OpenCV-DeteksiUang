# 💵 Deteksi Uang Rupiah dengan Python & OpenCV

> *Deteksi uang kertas & koin Indonesia secara otomatis dari gambar atau kamera real-time menggunakan OpenCV!* 🇮🇩

---

## 📌 Fitur Utama

✅ Deteksi **uang kertas**:
- Rp1.000, Rp2.000, Rp5.000, Rp10.000, Rp20.000, Rp50.000, Rp100.000

✅ Deteksi **uang koin**:
- Rp100, Rp200, Rp500, Rp1.000

✅ Sumber input:
- 🖼️ Gambar (`foto.py`)
- 📷 Kamera/Webcam (`kamera.py`)

✅ Output:
- Gambar/video dengan label nilai uang terdeteksi
- Tampilan real-time jika pakai webcam

---

## 🧠 Teknologi yang Digunakan

| Library           | Kegunaan                                |
|-------------------|------------------------------------------|
| `OpenCV (cv2)`    | Deteksi warna HSV, lingkaran, dan kamera |
| `NumPy`           | Manipulasi array dan matrix              |
| `imutils` (opsional) | Resize, konversi tambahan gambar     |

---

## 📁 Struktur Folder

```bash
deteksi-uang/
├── kamera.py            # Webcam detection
├── foto.py              # Image detection
├── image/
│   ├── 100.png
│   ├── 5000.png
│   └── ...
├── assets/              # Screenshot hasil deteksi
└── README.md


---

## 🛠️ Cara Instalasi & Menjalankan

### 1. Clone Repositori

```bash
git clone https://github.com/Libra2694/OpenCV-DeteksiUang.git
cd OpenCV-DeteksiUang

### 2. (Opsional) Buat Virtual Environment
``` bash
python -m venv env
env\Scripts\activate   # Windows
source env/bin/activate # Mac/Linux
