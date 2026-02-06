---
title: How Add Library at Android Studio Project
tags:
  - Technology
  - Tips
created: 2026-02-05T10:44
updated: 2026-02-05T10:44
---
- Di project [[Android]] studio  jikalau sudah menggunakan version catalog tambahkan versi nya dulu di `libs.versions.toml` hal ini agar versi dapat diatur di satu tempat 
![](https://res.cloudinary.com/dx8dogwhc/image/upload/v1770263194/image_ljwrte.jpg)

- lalu tambahkan di build script (`build.gradle.kts`)(:app) dan baru di sync untuk di download di gradle. 
![](https://res.cloudinary.com/dx8dogwhc/image/upload/v1770263266/image_wexjs4.jpg)




---
⌛ *Created Thursday, 5 February 2026 - 10:44*