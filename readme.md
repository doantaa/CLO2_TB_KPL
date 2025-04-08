# 🎮 Mini game berbasis CLI

Game ini memungkinkan pengguna memilih dan memainkan beberapa mini game berbasis Python. Setiap game berada dalam folder terpisah, dan bisa dikembangkan secara modular.


## 📜 Team 4

- Doanta Aloycius Ginting
- Lintang Suminar Tyas Weni
- Aufa Muhammad Isyfa'lana
- Rezky Pratiwi



## 📦 Daftar Game

| Game                 | Deskripsi                             | Lokasi File                    |
|----------------------|---------------------------------------|--------------------------------|
| ❌ Tic Tac Toe       | Permainan strategi dua pemain         | `tic_tac_toe/tic_tac_toe_main.py` |
| 🛡️ RPG Mini Game     | Game RPG sederhana berbasis teks      | `rpg/rpg_main.py`              |
| ⌨️ Typing Speed Game | Uji kecepatan mengetik dan tebak kata | `typing_speed/typing_speed_main.py` |

## 🚀 Cara Menjalankan Proyek

1. **Clone repository** ini:
   ```bash
   git clone https://github.com/doantaa/CLO2_TB_KPL.git
   cd CLO2_TB_KPL
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan menu utama:**
   ```bash
   python main.py
   ```

4. **Navigasi Menu:**
   - Gunakan tombol panah atas/bawah di keyboard
   - Tekan Enter untuk memilih game
   - Setelah selesai bermain, otomatis akan kembali ke menu utama

## 📁 Struktur Proyek

```
project-name/
├── main.py                  # Launcher utama
├── requirements.txt         # Dependensi project
├── tic_tac_toe/
│   └── tic_tac_toe_main.py
├── rpg/
│   └── rpg_main.py
├── typing_speed/
│   └── typing_speed_main.py
└── README.md                # Dokumentasi proyek
```

## 🧑‍💻 Contribution


### 1. Fork & Clone
```bash
git clone https://github.com/doantaa/CLO2_TB_KPL.git
cd CLO2_TB_KPL
```

### 2. Buat Branch Baru
Gunakan nama yang deskriptif dan gunakan konvensi prefix / tambahkan nama agar lebih mudah:
```bash
git checkout -b feat/bambang-rpg-leveling-system
```

### 3. Commit dengan Format Conventional Commits
```bash
git commit -m "feat(rpg): tambahkan sistem leveling karakter"
```

Prefix yang umum digunakan:
- `feat`: penambahan fitur
- `fix`: perbaikan bug
- `refactor`: perombakan kode tanpa mengubah perilaku
- `chore`: perubahan minor (mis. update dependencies)
- `docs`: perubahan dokumentasi
- `test`: penambahan/perbaikan unit test

### 4. Push & Pull Request
```bash
git push origin feat/bambang-rpg-leveling-system
```
Buka Pull Request ke branch `main` melalui GitHub dan sertakan deskripsi singkat perubahanmu.

## 🔧 Dependencies

Proyek ini menggunakan:
- Python 3.9+
- [simple-term-menu](https://pypi.org/project/simple-term-menu/)

Install dengan:
```bash
pip install simple-term-menu
```
