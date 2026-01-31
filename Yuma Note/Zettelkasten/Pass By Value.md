---
title: Pass By Value
tags:
  - Technology
created: 2026-01-31T16:57
updated: 2026-01-31T17:02
---
- Beda dengan [[Pass By Reference]], dimana metode ini langsung melakukan variable copy dan langsung di kirim ke fungsi / prosedur dan tidak sebagai argumen.
- sehingga variabel asli tetap aman dan tidak berubah karena nilai nya disalin sehingga yang asli tidak berubah

```c
void ubah(int x) {
    x = 10;
}

int main() {
    int a = 5;
    ubah(a);
    // a tetap 5
}

```

---
⌛ *Created Saturday, 31 January 2026 - 16:57*
