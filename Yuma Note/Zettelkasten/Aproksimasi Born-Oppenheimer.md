---
title: Aproksimasi Born-Oppenheimer
tags:
  - Science
  - Chemistry
created: 2026-01-12T09:16
updated: 2026-01-12T09:16
---
### Inti idenya

Dalam sebuah molekul, **inti atom (nukleus)** jauh lebih berat dan bergerak **jauh lebih lambat** dibandingkan **elektron**. Karena perbedaan kecepatan ini sangat besar, kita bisa **memisahkan gerak elektron dan inti** dalam perhitungan.

### Analogi sederhana

Bayangkan:

* **Inti atom** = gajah berjalan pelan
* **Elektron** = burung kecil yang terbang cepat di sekitarnya

Karena burung bergerak sangat cepat, kita bisa menganggap gajah **hampir diam** saat kita menganalisis gerakan burung. Setelah itu, baru kita lihat bagaimana gajah bergerak.

### Apa yang dilakukan aproksimasi Born–Oppenheimer?

1. **Inti dianggap diam sementara**
   Posisi inti atom “dikunci” pada titik tertentu.
2. **Elektron dihitung terlebih dahulu**
   Persamaan Schrödinger diselesaikan untuk elektron dengan inti yang tetap.
3. **Energi elektron membentuk permukaan energi potensial**
   Energi ini menjadi “landasan” bagi gerak inti.
4. **Gerak inti dihitung kemudian**
   Inti bergerak di atas permukaan energi tersebut.

### Mengapa ini sangat membantu kimia komputasi?

Tanpa aproksimasi ini:

* Persamaan kuantum untuk elektron **dan** inti harus diselesaikan sekaligus → sangat rumit dan hampir tidak mungkin untuk molekul nyata.

Dengan aproksimasi Born–Oppenheimer:

* Perhitungan jadi **jauh lebih sederhana**
* Memungkinkan metode seperti **Hartree–Fock, DFT, dan post-HF**
* Kita bisa menghitung **struktur molekul, energi ikatan, spektrum, dan reaksi kimia**

### Ringkasnya

> **Born–Oppenheimer = memisahkan gerak elektron (cepat) dan inti (lambat) agar perhitungan kimia kuantum menjadi praktis.**


---
⌛ *Created Monday, 12 January 2026 - 09:16*