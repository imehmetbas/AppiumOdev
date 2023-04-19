Hepsiburada Mobil Uygulaması
=====================
Created by testinium on 18.04.2023

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.


Hepsiburada_Acilis_Kontrol
----------------------
Tags: Uygulama acilma kontrolu

* Hepsiburada uygulamasi acilir, uygulamanin acildigi kontrol edilir


Login_Kontrol
----------------------
Tags: Login kontrol

* Hesabim butonuna tiklanir,giris yap butonuna tiklanir,giris sayfası acildigi kontrol edilir
* Mail adresi girilir,giris yap butonuna tıklanır
* Sifre girilir,giris yap butonuna basılır,sayfadaki elementler kontrol edilir
* Basarili giris yapildi hosgeldiniz mesajı goruntulenir

ProductListDetail_Kontrol
----------------------
Tags: Product listesi ve urun detay kontrol

* Arama cubuguna tiklanir, "Oyuncak" aranir
* "Oyuncak" kelimesinde listelenen ürünler kontrol edilir,rastgele urun secilir
* Urun detay sayfası kontrol edilir


FavoritePage_Kontrol
----------------------
Tags: Favorilere ekleme ve silme kontrolu

* Urun favori ekleme butonuna tıklanir,favori ekleme kontrol edilir
* Anasayfaya donulur
* Favori sayfasına gidilir,sayfanin geldigi kontrol edilir
* Favori detay sayfasına gidilir
* Favori silme islemi yapilir
* Favori silme basarili mesajı goruntulenir
* Anasayfaya donulur


ProductListDetail_Kontrol2
----------------------
Tags: Product listesi ve urun detay kontrol

* Arama cubuguna tiklanir, "Oyuncak" aranir
* "Oyuncak" kelimesinde listelenen ürünler kontrol edilir,rastgele urun secilir
* Urun detay sayfası kontrol edilir

AddBasket_Kontrol
----------------------
Tags: Sepete urun ekleme ve urun silme

* Urun sepete eklenir,eklendigi kontrol edilir,sepete git butonuna tıklanır
* Sepetteki urun silinir,silinen urun geri al butonu ile tekrar sepete eklenir
* Alisverisi tamamla butona tiklanir, sayfanin acildigi kontrol edilir

AddAdress_Kontrol
----------------------
Tags: Adres ekleme ve kaydetme kontrolu

* Adres ekle butonuna tıklanır, sayfanın yuklendigi kontrol edilir
* Adres bilgileri girilir
* Adres kaydet butonuna tıklanır,kayıt edildigi kontrol edilir

OrderConfirmation_Kontrol
----------------------
Tags: Siparis onaylama ve hata mesajı kontrolu

* Kart bilgileri girilmeden siparis onayla butonuna tiklanir, hata mesaji geldigi kontrol edilir




