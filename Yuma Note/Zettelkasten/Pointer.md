---
title: Pointer
tags:
  - Technology
created: 2026-01-31T16:28
updated: 2026-01-31T16:51
---
- **Pointer** merupakan suatu variabel yang dapat menyimpan alamat memori
- Di beberapa bahasa pemrograman pointer di handle secara eksplisit seperti di [[C]]
- Pointer tidak menyimpan nilai langsung biasa dipakai sebagai *[[Pass By Reference]]* 
- Di bahasa pemrograman ada dua konsep penting yang *[[Pass By Reference]]* dan *[[Pass By Value]]*
- Menggunakan pointer tidak mengirim nilai atau value secara langsung tapi alamat memori dari variabel tersebut dan fungsi bisa langsung mengubah nilai tersebut.
```c
void tambah(int *p) {
    *p = *p + 1; // *p artinya "nilai di alamat p"
}

int main() {
    int a = 5;
    tambah(&a);  // &a artinya "alamat dari a"
    printf("%d", a); // sekarang 6
}
```

```c
#include <stdio.h>

void go_south_east(int *lat, int *lon) {
  *lat -= 1;
  *lon += 1;
}

int main() {
  int latitude = 32;
  int longitude = -64;
  go_south_east(&latitude, &longitude);
  printf("Avast! now at: [%i, %i]\n", latitude, longitude);
  return 0;
}

/*Gunakan pointer karena jika langsung seperti:
 * lat = lat - 1 maka ketika digunakan tidak mengubah value
 * karena ketika fungsi void go_south_east(int lat, int long) dipanggil
 * hanya akan mengcopy value bukan sebagai argument
 * sehingga dikirim pointer alamat nya intinya ubah
 * nilai ini dia disini gitu*/
//
// void ubah(int x) { x = 10; }
//
// int main() {
//   int a = 5;
//   ubah(a);
//   printf("%d\n", a); // tetap 5
// }

```


---
⌛ *Created Saturday, 31 January 2026 - 16:28*