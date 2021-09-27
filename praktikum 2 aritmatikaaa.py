# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 13:10:20 2021

@judul : praktikum 2, Operasi Aritmatika pada Python
@hari tanggal : 27-09-2021
@NIM : 065002100002
@Nama : Nabilah Putri
"""

import math
print("menghitung aritmatika")
g=float(input("masukan nilai umur kamu:"))
h=float(input("masukan nilai umur dia:"))
print("jumlah umur kamu ditambah umur dia adalah:",g+h)
print("selisih umur kamu dan dia adalah:",abs(g-h))
print("jumlah dari umur kamu dikali umur dia adalah:",g*h)
print("jumlah dari umur kamu dibagi umur dia adalah:",g/h)
print("jumlah sisa pembagian dari hasil umur kamu dibagi umur dia adalah:",g%h)
print("hasil dari log (umur kamu)",math.log10(g))
print("hasil umur kamu pangkat umur dia adalah:",g**h)