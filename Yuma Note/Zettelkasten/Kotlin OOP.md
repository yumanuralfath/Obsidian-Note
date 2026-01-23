---
title: Kotlin OOP
tags:
  - Technology
  - Tool
created: 2026-01-23T08:16
updated: 2026-01-23T10:42
---
# Kotlin Object Oriented programming

> Dikarenakan beberapa hari belakang seperti di tulis di daily [[23.01.26.23]] saya sedang mencoba belajar Mobile Development terutama di [[Android]] karena ya saya hanya punya android,  dan sesuai [Google I/0 2017](https://id.wikipedia.org/wiki/Kotlin_(bahasa_pemrograman))  , Google mengumumkan dukungan kelas pertama untuk [[Kotlin]] pada android sehingga, saya mencoba belajar kotlin sebagai Android Developer. Langkah pertama saya di kotlin adalah belajar OOP walau sebenarnya sudah belajar di javascript, tapi jujur OOP di javascript terkesan dipaksakan sehingga boleh dikata *jelek* hehe. materi oop di kotlin yang di pelajari:

## Classes, Objects, and Inheritance

- ***class*** merupakan cetakan atau blueprint misal dia punya fungsi apa saja, contoh :
```kotlin
class Person{
	var name = "Name"
	
	fun SayHello(){
		println("Halo, nama saya $name")
	}
}
```
 - Di kotlin menggunakan Pascal case perbedaan tiap case bisa dilihat [disini](https://www.freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference/) 

 - ***Object*** merupakan hasil dari class, hasil dari cetakan:
```kotlin
fun main(){
	val yuma = person()
	yuma.name = "Yuma Nur Alfath"
	yuma.SayHello()
}
```
- output nya akan "Halo, nama saya Yuma Nur Alfath"

- ***Inheritance*** (pewarisan) dimana class anak mewarisi class induk
- ❗Di kotlin berbeda dengan Java class default nya **FINAL** dimana berarti class secara default tidak dapat mewarisi class induk sehingga harus ditambahkan *keyword* **Open**
```kotlin
// class induk
open Class Animal {   //harus ditambahkan "open"
	var name = "Name"
	
	open fun eat(){    //karena ingin bisa di override 
		println("$name Sedang Makan")
	}
}

//class anak
class Cat: Animal() {
	fun meow() {
		println("$name sedang Meong")
	}
} // 'cat' mewarisi Animal


//jadi bisa dipakai menjadi
//misal kucing namanya "tando"
fun main() {
	val kucing = cat()
	kucing.name = "Tando"
	kucing.eat()  // Tando sedang Makan  
	kucing.meow() // Tando sedang Meong
}
```

- misal ingin *override method*  dimana ingin merubah suatu fungsi dari induk class:
```Kotlin
class Dog: Animal() {
	override fun eat(){
		println("$name Sedang Makan dengan lahapnya")
	}
} 

fun main() {
	val anjing = Dog()
	anjing.name = "Hachiko"
	anjing.eat() // Hachiko Sedang Makan dengan Lahapnya
}
```

## Interfaces and Abstract classes

- ***Interface*** merupakan suatu kontrak/ janji
- bertujuan untuk membuat fungsi dan properties yang harus diikuti class 
- Berbeda dengan Inheritance yang boleh <mark style="background: #FF5582A6;">hanya 1 di kotlin</mark> 
- Interface dapat lebih dari satu di satu class.
- Interface di android development biasa dipakai untuk event listeners, seperti OnClickListener atau definisi dari repository data untuk memberi standar dari class tanpa mendikte implementasi-nya bagaimana.

```Kotlin
//buat kontrak dan class wajib ngikutin rule ini
interface Drivable {
	val maxSpeed: Int 
	fun drive(): String
	fun stop(){
		println("Vehicle Stopped")
	}
}

interface Repairable {
	fun repair()
}	

// buat class sesaui interface
class Car(val model: String): Drivable, Repairable //multi interface 
{
	override val maxSpeed: Int = 200
	override fun drive(): String = "$model is driving at $maxSpeed Km/h"
	override fun repair(){
		println("$model repaired")
	}
}

fun main() {
	val car = Car("Subaru")
	println(car.drive()) //Subaru is driving at 200 Km/h
	car.stop() //Vehicle Stopped
	car.repair() // Subaru repaired
}
```

- ***Abstract Class*** 












---
⌛ *Created Friday, 23 January 2026 - 08:16*