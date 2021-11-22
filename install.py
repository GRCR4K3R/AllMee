#!/bin/python

import os,sys,time

def bersih():
        os.system("clear")

def menu():
        print "\t Tools By Reza Alfauzan\n"
        print("1. Wajib update ya!!!")
        print("2. Info Script.")
        # input
        pilih = input("Masukkan pilihan : ")
        if pilih ==1:
                os.system("pkg update && pkg upgrade")
                os.system("pkg install nano")
                os.system("pkg install figlet")
                os.system("pkg install toilet")
                os.system("pkg install ruby")
                os.system("gem install lolcat")
                os.system("pkg install python")
                os.system("pip install requests")
                os.system("pip install mechanize")
                os.system("pip install --upgrade pip")
                os.system("pip2 install requests")
                os.system("pip2 install mechanize")
                os.system("pip2 install --upgrade pip")
        if pilih ==2:
                os.system("figlet Rzaa Ajaa")
                logo = """
                      ===============================================
                      = (+) Reza Yang Buat Scriptnya             (+)=
                      = (+) Github Gua :GRCR4K3R                 (+)=
                      = (+) Facebook   :Rzaa Ajaa                (+)=
                      = (+) Profil     :Stiker Pentol Itu gua!!  (+)=
                      ==================================================="""
                print logo
menu()
