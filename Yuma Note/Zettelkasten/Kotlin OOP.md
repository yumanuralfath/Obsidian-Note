---
title: Kotlin OOP
tags:
  - Technology
  - Tool
created: 2026-01-23T08:16
updated: 2026-01-24T09:56
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
```kotlin
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

```kotlin
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
```kotlin
//abstract class biasa digunakan sharing untuk kode yang umum antar class 
abstract class Vehicle {
  abstract val type: String
  abstract fun move()
  fun startEngine() {
    println("$type engine started")
  }
}

class Car(val model: String) : Vehicle() {
  override val type: String = "Car"
  override fun move() {
    println("$model Car is Moving")
  }
}

fun main() {
  val car = Car("Honda")
  car.startEngine()
  car.move()
}
```

- abstract kelas tidak bisa dibuat langsung object nya seperti <mark style="background: #FF5582A6;">val vehicle = Vehicle()</mark> ❌
- interface baik digunakan hanya untuk murni kontrak ter-khusus ketika dibutuhkan multiple inheritance.
- abstract class ditujukan untuk scenario oleh shared state atau partial implementation

- Contoh penggabungan keduanya:

```kotlin
interface Loggable {
	fun log()
}

abstract class Machine {
	abstract fun operate()  //fungsi atau value yang wajib di turunkan harus ada 
							// keyword abstract
}

//class turunan 
class Robot: Machine(), Loggable {
	override fun operate(){
		println("Robot operating")		
	}
	override fun log() {
		println("Robot log")
	}
}

fun main(){
	val robot = Robot()
	robot.operate()
	robot.log
}
```

## Null Safety and Smart casts

- Berbeda dengan java kotlin ada fitur *Null Safety*
- Di kotlin secara default variable *non-nullable*
```kotlin
var name: String = "Alice" //tidak bisa di assigned null
```
untuk memperbolehkan *null* harus di handle agar tidak crash saat runtime:
```kotlin
val length = name?.length
```
- safe call operator "?" ini menghasilkan null jika memang return nya null sehingga tidak menyebabkan crash
- bisa di buat *function scope* juga:
```kotlin
name?.let {
	println("Name Length: ${it.length}")
}
```

- Smart cast juga fitur yang bagus di kotlin tidak perlu manual casting type
- kedua fitur merupakan critical di android jika berurusan dengan unpredictable data source , misal fetch user data lebih safe dan juga smart cast untuk *age*:
```kotlin
data class User(val name: String? , val age: Int)
val user: User? = getUserFromApi()
val displayName = user?.name?: "Unkown"
user?.let{
	if (it.age > 18) {
		println("Adult: $displayName")
	}
}
```
























---
⌛ *Created Friday, 23 January 2026 - 08:16*